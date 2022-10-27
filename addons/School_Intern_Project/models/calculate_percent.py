from re import search
import string
from unicodedata import name
from odoo import fields, models, api

class CalculatePercent(models.Model):
    _name = 'calculate.percent'
    _description = 'Calculate Percentage'
    _rec_name = 'roll_no_id'

    roll_no_id = fields.Many2one('create.session', string = 'Roll_No')
    stu_name = fields.Char(string = 'Student Name')
    sections = fields.Char(string = 'Section')
    check_month = fields.Char(string = 'Month')
    full_day = fields.Float(string = 'Full_Day')
    half_day = fields.Float(string = 'Half_day')
    leave = fields.Float(string = 'Leave')
    attendance_count = fields.Float(string = 'Attendance_Count', compute = '_compute_total')
    total_percent = fields.Float(string = 'Total Percent', compute = '_compute_total_per')
    status = fields.Char(string = 'Status')

    @api.onchange('roll_no_id')
    def _onchange_roll_no_id(self):
        if self.roll_no_id:
            self.stu_name= self.roll_no_id.student_id.name
            self.sections= self.roll_no_id.session_id.session_name
           
    @api.onchange('roll_no_id', 'check_month')
    def _onchange_percent(self):
        if self.roll_no_id:
            month = self.check_month
            name = self.roll_no_id.student_id.name
            self.full_day = self.env['attendance.students'].search_count(['&', '&', ('student_id', '=', name), ('today_month', '=', month), ('percentage', '=', 1.0)])
            self.half_day = self.env['attendance.students'].search_count(['&', '&', ('student_id', '=', name), ('today_month', '=', month), ('percentage', '=', 0.5)])
            check_leaves = self.env['leave.students'].search(['&', ('student_id', '=', name), ('leave_month', '=', month)])
            days=0
            for check_leave in check_leaves:
                if check_leave.number_of_days:
                    days+=check_leave.number_of_days
            if days<5:
                self.leave=days 
            else:
                self.leave=4  
                
    @api.depends("full_day", "half_day")
    def _compute_total(self):
        for record in self:
            record.attendance_count = (record.half_day /2) + record.full_day
    
    @api.depends("attendance_count")
    def _compute_total_per(self):
        for record in self:
            percent = (record.attendance_count /30) * 100
            if percent <= 79.0:
                if record.leave >0:
                    record.attendance_count += record.leave
                    record.total_percent =  (record.attendance_count /30) * 100
                else:
                    record.total_percent = percent
            else:
                record.total_percent = percent

    @api.onchange('total_percent', 'status')
    def _onchange_total_percent(self):
        for check in self:
            if check.total_percent:
                if check.total_percent >= 80.0:
                    check.status = 'Pass'
                else:
                    check.status = 'Fail'