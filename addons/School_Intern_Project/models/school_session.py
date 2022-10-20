import string
from odoo import fields, models, api

class SchoolSession(models.Model):
    _name = 'school.session'
    _description = 'School Session'

    session_name = fields.Char(string = 'Session')
    t_head = fields.Many2one('teachers.students', string = 'Teacher Head')
    teacher = fields.Many2many('teachers.students')
    student_ids = fields.One2many('create.session','session_id', string="Student")

class Session(models.Model):
    _name = 'create.session'
    _description = 'Session Create'
    _rec_name = 'roll_no'

    student_id = fields.Many2one('teachers.students', string = 'Student')
    session_id = fields.Many2one('school.session')
    roll_no = fields.Char(string = 'Roll_No')