import string
from odoo import api, fields, models
from datetime import datetime, timedelta
from ast import IsNot



class LeaveStudents(models.Model):
    _name = 'leave.students'
    _description = 'Leave Detail'
    _rec_name="student_id"

    roll_no = fields.Many2one('create.session', string="Roll No", required=True, ondelete='cascade', index=True)
    student_id = fields.Char(string = 'Name')
    sections = fields.Char(string = 'Section Name')
    leave_month = fields.Char()
    leave_type = fields.Selection([('sick', 'Sick Leave'), ('parental', 'Parental Leave'), ('emergency', 'Emergency Leave')], string  = 'Leave Type')
    number_of_days = fields.Float(string = 'Date', store=True, compute = '_compute_leave_hours')
    request_date_from = fields.Date('Request Start Date')
    request_date_to = fields.Date('Request End Date')
    reason = fields.Text(required = True)

    @api.onchange('request_date_from')
    def _onchange_request_date_from_month(self):
        if self.request_date_from:
            check_month = self.request_date_from
            self.leave_month = check_month.month
        else:
            self.leave_month = 'No Month'

    @api.onchange('roll_no')
    def _onchange_roll_no(self):
        if self.roll_no:
            self.student_id= self.roll_no.student_id.name
            self.sections= self.roll_no.session_id.session_name

    @api.depends('request_date_from', 'request_date_to')
    def _compute_leave_hours(self):
        for leave in self:
            if leave.request_date_from and leave.request_date_to:
                if leave.request_date_from != leave.request_date_to:
                    d1 =  datetime.strptime(str(leave.request_date_from),'%Y-%m-%d') 
                    d2 = datetime.strptime(str(leave.request_date_to),'%Y-%m-%d')
                    d3 = d2-d1
                    leave.number_of_days = int(str(d3.days)) + 1.0
                else:
                    leave.number_of_days = 0.5