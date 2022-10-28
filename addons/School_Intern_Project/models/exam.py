from ast import Pass
from email.policy import default
import math
from odoo import models,fields,api

class SchoolExam(models.Model):
    _name= "school.exam"
    _description="Exam"
    _rec_name = 'stu_name'
   
    
    # stu_name=fields.Many2one('calculate.percent', string="Student Name")
    roll_no = fields.Many2one('calculate.percent', string = 'Roll No')
    stu_name = fields.Char(string = 'Student Name')
    sections = fields.Char(string = 'Section')
    subject_id = fields.Many2one('question.model', string='Course')
    sections = fields.Char()
    exam_ids = fields.One2many('school.exam.line', 'exam_id', string='Question', store=True)
    # total_mark=fields.Char() #first test
    status=fields.Char()
    # exam_marks=fields.Integer() #second test
    exam_mark=fields.Integer()
    # state=fields.Selection([
    #     ('draft','Draft'),
    #     # ('in_examination','In Examination'),
    #     ('done','Done'),
    #     ('cancel','Cancel')],default='draft', string="State", required=True)

    # def action_in_examination(self):
    #     for rec in self:
    #         rec.state="in_examination"
    
    # def action_done(self):
    #     for rec in self:
    #         rec.state="done"        

    # def action_cancel(self):
    #     for rec in self:
    #         rec.state="cancel"

    # def action_draft(self):
    #     for rec in self:
    #         rec.state="draft"

    @api.onchange('subject_id')
    def onchange_subject_id(self):
        if self.subject_id:
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

    # @api.onchange('stu_name')
    # def _onchange_stu_name(self):
    #     if self.stu_name:
    #         self.roll_no=self.stu_name.roll_no_id.roll_no
    #         self.sections= self.stu_name.sections.section_id.sections              

    @api.onchange('roll_no')
    def _onchange_roll_no(self):
        if self.roll_no:
            self.stu_name= self.roll_no.stu_name
            self.sections= self.roll_no.sections

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
        if mark>=0 and mark<=39:
            self.status="Fail"
        elif mark>=40 and mark<=79:
            self.status="Pass"
        elif mark>=80 and mark<=100:
            self.status="Pass with Distinction"
        else:
            self.status="Wrong Cridential!"  


class SchoolExamLine(models.Model):
    _name="school.exam.line"
    _description="School Exam Line"

    exam_id=fields.Many2one('school.exam')

    question_text=fields.Text()
    answer = fields.Char()
    exam_answer=fields.Selection([('true','True'),('false','False')], "Exam_Answer")
    score=fields.Integer()