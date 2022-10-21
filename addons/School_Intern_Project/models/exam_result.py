from unittest import result
from odoo import models, fields, api

class ExamResult(models.Model):
    _name = 'exam.result'
    _description = 'Exam Result'

    student_id = fields.Many2one('teachers.students', string = 'Student Name')
    total_score = fields.Integer(string = 'Total')
    result = fields.Char()
    exam_ids = fields.One2many('school.exam.result', 'result_id', string='Result', store=True)

class SchoolExamResult(models.Model):
    _name = 'school.exam.result'
    _description = 'School Exam Result'

    subject_id = fields.Char()
    marks = fields.Integer()
    result_all = fields.Char()
    result_id = fields.Many2one('exam.result')

    @api.onchange('student_id')
    def onchange_student_id(self):
        self.exam_ids=[(5,0,0)]
        datas = self.env['school.exam'].search([])
        if datas:
            for data in datas:
                if self.student_id.name == data.stu_name:
                    vals = {
                    'subject_id' : data.subject_id,
                    'marks': data.exam_mark,
                    'result_all': data.status,
                    }
                    self.update({'exam_ids':[(0, 0, vals)]})