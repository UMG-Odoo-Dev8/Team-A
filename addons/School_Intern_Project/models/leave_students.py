from re import L
import string
from odoo import api, fields, models,_,exceptions
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
    leave_select=fields.Selection([('hl','Half Leave'),('fl','Full Leave')])

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
                    # leave.number_of_days = 0.5
                    leave_date = datetime.strptime(str(leave.request_date_from), '%Y-%m-%d')
                    leave_dates = str(leave_date.date())
                    print('leave date', leave_dates)
                    print(type(leave_dates))
                    checks=self.env['attendance.students'].search(['&',('student_id','=',self.student_id),('check_in_date', '=', leave_dates)])
                    print(checks)
                    print(type(self.leave_select))
                    if self.leave_select=="fl":
                        leave.number_of_days = 1
                    else:
                        if checks.attendance_hours <= 3:
                            leave.number_of_days = 0.5
                        else:
                            leave.number_of_days = 0    
                    for check in checks:
                        check_date = check.check_in.date()
                        leave_date = leave.request_date_from
                        if check_date==leave_date:
                            print('hi'*100)
                            if check.check_in and check.check_out:
                                if check.attendance_hours <= 3:
                                    leave.number_of_days =0.5
                                else:
                                    leave.number_of_days=0
                            
                    
    @api.constrains('number_of_days')
    def _check_validity_leave(self):
        """ verifies if check_in is earlier than check_out. """
        for leave in self:
            if  leave.number_of_days==0:
                raise exceptions.ValidationError(_('No take Leave. This Date is Full Day Attendance Day!'))
