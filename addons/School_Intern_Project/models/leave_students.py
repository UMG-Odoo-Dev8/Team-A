import string
from odoo import api, fields, models
from datetime import datetime, timedelta


class LeaveStudents(models.Model):
    _name = 'leave.students'
    _description = 'Leave Detail'

    roll_no = fields.Many2one('create.session', string="Roll_NO", required=True, ondelete='cascade', index=True)
    student_id = fields.Char(string = 'Name')
    sections = fields.Char(string = 'Session Name')
    leave_month = fields.Char()
    leave_type = fields.Selection([('sick', 'Sick Leave'), ('parental', 'Parental Leave'), ('emergency', 'Emergency Leave')], string  = 'Leave Type')
    number_of_days = fields.Float(string = 'Date', store=True)
    request_date_from = fields.Date('Request Start Date')
    request_date_to = fields.Date('Request End Date')
    reason = fields.Text(required = True)
    percentage = fields.Float(string = 'Percent')

    @api.onchange('roll_no')
    def _onchange_roll_no(self):
        if self.roll_no:
            self.student_id= self.roll_no.student_id.name
            self.sections= self.roll_no.session_id.session_name

    @api.onchange('request_date_from', 'request_date_to', 'number_of_days')
    def calculate_date(self):
        if self.request_date_from and self.request_date_to:
            if self.request_date_from != self.request_date_to:
                d1 =  datetime.strptime(str(self.request_date_from),'%Y-%m-%d') 
                d2 = datetime.strptime(str(self.request_date_to),'%Y-%m-%d')
                d3 = d2-d1
                self.number_of_days = str(d3.days)
                self.percentage = str(d3.days)
            else:
                self.number_of_days = 0.5
                self.percentage = 0.5
        else:
            print('Hello Testing')