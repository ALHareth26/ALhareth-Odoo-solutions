{
    'name': 'Advanced Data Analytics Pro',
    'version': '1.0',
    'author': 'Al Hareth Kamal',
    'category': 'Analytics',
    'summary': 'Full-stack SQL and OWL Analytics for Odoo 19',
    'depends': ['sale', 'web', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/analytics_views.xml',
        'views/menu_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'advanced_data_analytics/static/src/components/kpi_card.js',
            'advanced_data_analytics/static/src/components/kpi_card.xml',
        ],
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}