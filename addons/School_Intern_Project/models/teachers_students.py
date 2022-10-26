from datetime import date, datetime
from email.policy import default
from sqlite3 import Date
import string,datetime
from xmlrpc.client import DateTime,_datetime
from odoo import models,fields,api

class SchoolInfo(models.Model):
    _name = "teachers.students"
    _description = "Testing for my Odoo project"
    _rec_name = 'name'

    name = fields.Char(required = True)
    avator = fields.Binary()
    date_of_birth = fields.Date(string = 'Date of Birth', required = True)
    age=fields.Char(string="Age", compute="_compute_age", readonly=True)
    gender = fields.Selection([("male", "Male"), ("female", "Female")], "Gender", required = True)
    father_name = fields.Char(required = True)
    degree = fields.Char()
    email = fields.Char()
    address = fields.Text()
    state = fields.Selection(selection=[
          ('teacher', 'Teacher'),
          ('teacher_head', 'Teacher HEAD'),
          ('student', 'Student'),
     ], string="Status", required = True, default = 'student')
    active = fields.Boolean(string = "Active", default = "True")
    subjects = fields.Many2one('subject.management', string = "Subjects")

    
    @api.depends("date_of_birth")
    def _compute_age(self):
        today_date=datetime.date.today()
        for rec in self:
            if rec.date_of_birth:
                date_of_birth=fields.Datetime.to_datetime(rec.date_of_birth).date()
                total_age=str(int((today_date-date_of_birth).days/365))
                rec.age=total_age
            else:
                rec.age="0"
