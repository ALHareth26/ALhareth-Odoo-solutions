{
    'name': 'Financial Intelligence Pro',
    'version': '1.0',
    'author': 'Al Hareth Kamal',
    'category': 'Accounting',
    'summary': 'Double-entry Liquidity and Solvency Analysis',
    'depends': ['account', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/ratio_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'account_financial_intelligence/static/src/components/ratio_dashboard.js',
            'account_financial_intelligence/static/src/components/ratio_dashboard.xml',
        ],
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}