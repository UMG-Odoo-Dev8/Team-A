import string
from unittest import result
from odoo import models, fields, api

class ExamResult(models.Model):
    _name = 'exam.result'
    _description = 'Exam Result'
    _rec_name="stu_name"

    # roll_no=fields.Many2one('school.exam', string="Roll No")
    roll_no_id=fields.Many2one('calculate.percent', string="Roll No", ondelete='cascade')
    stu_name = fields.Char()
    total_score = fields.Integer(string = 'Total')
    result = fields.Char(string = 'Status')

    @api.onchange('roll_no_id')
    def _onchange_roll_no_id(self):
        if self.roll_no_id:
            self.stu_name = self.roll_no_id.roll_no_id.student_id.name

    @api.onchange('stu_name')
    def onchange_stu_name(self):
        print("*"*100)
        if self.stu_name:
            school_exam_ids = self.env['school.exam'].search([('roll_no.stu_name', '=', self.stu_name)])
            # print('/////////hello', school_exam_ids)
            # print(school_exam_ids)
            mark = 0
            chceck_status_fail = False
            check_status_pass = False
            check_status_distinction = 0
            for schoolo_exam in school_exam_ids:
                if schoolo_exam.exam_mark:
                    mark += schoolo_exam.exam_mark
                else:
                    mark  = mark

                if schoolo_exam.status == 'Fail':
                    chceck_status_fail = schoolo_exam.status
                else:
                    if schoolo_exam.status == 'Pass':
                        check_status_pass = schoolo_exam.status
                    else:
                        check_status_distinction += 1
            if chceck_status_fail:
                self.result = 'Exam Fail'
            elif check_status_distinction and check_status_pass:
                if check_status_distinction:
                    self.result =  check_status_distinction, ('Distinction Exam Pass')
                else:
                    self.result = 'Exam Pass'
            else:
                self.result = 'No result'

            self.total_score = mark

           