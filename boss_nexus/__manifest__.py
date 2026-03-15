{
    'name': 'Boss Nexus: The Final Logic',
    'version': '1.0.0',
    'category': 'Technical/Integration',
    'summary': 'High-performance API Orchestrator and Command Center',
    'author': 'Alhareth Malik',
    'depends': ['base', 'web', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/nexus_views.xml',
        'views/nexus_menus.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'boss_nexus/static/src/components/**/*',
        ],
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}