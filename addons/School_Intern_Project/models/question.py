from email.policy import default
from odoo import models,fields

class QuestionModel(models.Model):
    _name= "question.model"
    _description="Question"
    _rec_name="subject"

    subject=fields.Many2one('subject.management',string="Course")
    question_ids = fields.One2many('question.model.line', 'question_id', string='Questions')
    

class QuestionModelLine(models.Model):
    _name="question.model.line"
    _description="Question Line"
    _rec_name="question_text"

    question_id = fields.Many2one('question.model', string='question') #to link question.model

    question_text= fields.Text("Question")
    answer=fields.Selection([('true','True'),('false','False')], "Answer")
    score=fields.Integer()
    active=fields.Boolean("Active",default="True")
    # subjects=fields.Char()