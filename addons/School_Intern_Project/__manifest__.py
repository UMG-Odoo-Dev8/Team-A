{
    'name' : 'School Info Data',
    # 'License' : 'LGPL-3',
    'depends': ['base', 'mail'],
    'data' : [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/subjects.xml',
        'views/session.xml',
        'views/attendance.xml',
        'views/leave.xml',
        'views/percnetage.xml',
        'views/exam_view.xml',
        'views/question_view.xml',
        'views/exam_result_view.xml',
    ]
}