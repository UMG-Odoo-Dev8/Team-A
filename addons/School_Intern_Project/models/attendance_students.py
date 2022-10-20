from ast import IsNot
from asyncio.windows_events import NULL
import string
from unicodedata import name
from datetime import datetime, timedelta
from odoo import fields, models, api, exceptions, _

class Attendance(models.Model):
    _name = 'attendance.students'
    _description = 'Checking Attendance'

    roll_no = fields.Many2one('create.session', string="Roll_NO", required=True, ondelete='cascade', index=True)
    student_id = fields.Char(string = 'Name')
    months = fields.Selection([('1', 'Jan'), ('2', 'Feb'), ('3', 'Mar'), ('4', 'Apr'), ('5', 'May'), ('6', 'June'), ('7', 'July'), ('8', 'Aug'), ('9', 'Sep'), ('10', 'Oct'), ('11', 'Nov'), ('12', 'Dec')])
    check_in = fields.Datetime(string="Check In", default=fields.Datetime.now, required=True)
    check_out = fields.Datetime(string="Check Out", default=fields.Datetime.now)
    attendance_hours = fields.Float(string='Attendance Hours', compute='_compute_attendance_hours', store=True, readonly=True)
    percentage = fields.Float(string = 'Percent', compute = '_check_attendance_per_day', store=True, readonly=True)
    total_percent = fields.Float(compute = '_compute_total_percent')
    sections = fields.Char()

    @api.onchange('roll_no')
    def _onchange_roll_no(self):
        if self.roll_no:
            self.student_id= self.roll_no.student_id.name
            self.sections= self.roll_no.session_id.session_name

    @api.depends('check_in', 'check_out', 'attendance_hours')
    def _check_attendance_per_day(self):
        for attendance in self:
            if not attendance.check_out:
                attendance.percentage = 0.5
            else:
                if attendance.attendance_hours <= 3:
                    attendance.percentage = 0.5
                else:
                    attendance.percentage = 1.0

                                    

    @api.depends('check_in', 'check_out')
    def _compute_attendance_hours(self):
        for attendance in self:
            if attendance.check_out and attendance.check_in:
                delta = attendance.check_out - attendance.check_in
                attendance.attendance_hours = delta.total_seconds() / 3600.0
            else:
                attendance.attendance_hours = False

    @api.constrains('check_in', 'check_out')
    def _check_validity_check_in_check_out(self):
        """ verifies if check_in is earlier than check_out. """
        for attendance in self:
            if attendance.check_in and attendance.check_out:
                if attendance.check_out < attendance.check_in:
                    raise exceptions.ValidationError(_('"Check Out" time cannot be earlier than "Check In" time.'))

    @api.depends('check_in', 'check_out', 'percentage', 'total_percent')
    def _compute_total_percent(self):
        self.total_percent = False
        total_per = 0
        for total in self:
            if total.check_in and total.check_out:
                total_per += total.percentage
            else:
                print('Hello')
        self.total_percent = total_per

    def my_fun(self):
        pass