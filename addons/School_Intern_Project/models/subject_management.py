import string
from odoo import models, fields

class Subject(models.Model):
    _name = "subject.management"
    _description = "All subject"
    _rec_name = "subjects"

    subjects = fields.Char()
    chapter = fields.Integer()
    start_date = fields.Date()
    end_date = fields.Date()
    