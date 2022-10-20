from ast import Pass
import math
from odoo import models,fields,api

class SchoolExam(models.Model):
    _name= "school.exam"
    _description="Exam"
   
    
    # student_id=fields.Many2one('section.line.model', string="Student Name")
    student_id=fields.Char()
    roll_no=fields.Many2one('create.session', string="Roll No")
    session=fields.Char(string="Section",  readonly=True)

    subject_id = fields.Many2one('question.model', string='Subject')

    exam_ids = fields.One2many('school.exam.line', 'exam_id', string='Question', store=True)
    # total_mark=fields.Char() #first test
    status=fields.Char()
    # exam_marks=fields.Integer() #second test
    exam_mark=fields.Char()
    
    
    @api.onchange('roll_no')
    def onchange_roll_no(self):
        if self.roll_no:
            self.session= self.roll_no.session_id.session_name
            self.student_id=self.roll_no.student_id.student_id
    

    @api.onchange('subject_id')
    def onchange_subject_id(self):
        # global answer_list
        # answer_list=[]
        self.exam_ids=[(5,0,0)]
        questions = self.env['question.model.line'].search([])
        # print(subject_id)
        if questions:
            for ques in questions:
                # print(".....",subj)
                # print(".....",subj.question_text)
                # print(".....",subj.answer)
                if self.subject_id.subject==ques.question_id.subject:
                    vals = {
                    'question_text': ques.question_text,
                    'score': ques.score,
                    'answer': ques.answer
                    }
                    self.update({'exam_ids':[(0, 0, vals)]})

    #Update Total Marks
    def exam_result(self):
        question_count=0
        mark=0
        for exam_id in self.exam_ids:
            question_count +=1
            if exam_id.answer==exam_id.exam_answer:
                mark +=1
        self.exam_mark=mark 
        if(mark>=math.ceil(question_count/2)):
            self.status='Pass'
        else:
            self.status='Fail'


class SchoolExamLine(models.Model):
    _name="school.exam.line"
    _description="School Exam Line"

    exam_id=fields.Many2one('school.exam')

    question_text=fields.Text()
    answer=fields.Char()
    exam_answer=fields.Selection([('true','True'),('false','False')], "Answer")
    score=fields.Integer()