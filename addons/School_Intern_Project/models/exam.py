from ast import Pass
import math
from odoo import models,fields,api

class SchoolExam(models.Model):
    _name= "school.exam"
    _description="Exam"
    _rec_name = 'stu_name'
   
    
    # student_id=fields.Many2one('section.line.model', string="Student Name")
    stu_name=fields.Many2one('calculate.percent', string="Student Name")

    subject_id = fields.Many2one('question.model', string='Course')

    exam_ids = fields.One2many('school.exam.line', 'exam_id', string='Question', store=True)
    # total_mark=fields.Char() #first test
    status=fields.Char()
    # exam_marks=fields.Integer() #second test
    exam_mark=fields.Integer()
    
    @api.onchange('subject_id')
    def onchange_subject_id(self):
        self.exam_ids=[(5,0,0)]
        questions = self.env['question.model.line'].search([])
        if questions:
            for ques in questions:
                if self.subject_id.subject==ques.question_id.subject:
                    vals = {
                    'question_text': ques.question_text,
                    'score': ques.score,
                    'answer': ques.answer
                    }
                    self.update({'exam_ids':[(0, 0, vals)]})

    #Update Total Marks
    # def exam_result(self):
    #     # question_count=0
    #     mark=0
    #     for result in self.exam_ids:
    #         # question_count +=1
    #         if result.answer==result.exam_answer:
    #             mark +=1
    #     self.exam_mark=mark 
    #     # if(mark>=math.ceil(question_count/2)):
    #     #     self.status='Pass'
    #     # else:
    #     #     self.status='Fail'

    def exam_result(self):
        mark = 0
        for ans in self:
            if ans.exam_ids:
                for result in ans.exam_ids:
                    if result.answer == result.exam_answer:
                        mark += result.score    
                    else:
                        mark = mark
            else:
                print('Hay! No question. Pls Try again')
        self.exam_mark = mark
        if(mark <= 39):
            self.status = 'Fail'
        elif(mark <= 79):
            self.status = 'Pass'
        elif(mark <= 99):
            self.status = 'Distinction'
        else:
            self.status = 'Perfect'

    


class SchoolExamLine(models.Model):
    _name="school.exam.line"
    _description="School Exam Line"

    exam_id=fields.Many2one('school.exam')

    question_text=fields.Text()
    answer = fields.Char()
    exam_answer=fields.Selection([('true','True'),('false','False')], "Exam_Answer")
    score=fields.Integer()