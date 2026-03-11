{
    'name': 'Super HR Management Pro',
    'version': '2.0',
    'author': 'Hareth Malik',
    'category': 'Human Resources',
    'summary': 'نظام احترافي لإدارة العهد والرواتب والتقييم الذكي',
    'depends': ['base', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/hr_assets_views.xml',
        'views/hr_employee_custom_views.xml',
    ],
    'application': True,
    'installable': True,
    'license': 'LGPL-3',
}