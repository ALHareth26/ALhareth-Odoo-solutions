{
    'name': 'HR Professional',
    'version': '1.0',
    'author': 'Hareth Malik',
    'category': 'Human Resources',
    'depends': ['base', 'hr'], 
    'data': [
        'security/ir.model.access.csv',
        'views/employee_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}