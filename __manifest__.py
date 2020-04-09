{
    'name': 'School Management',
    'version': '13.0.1.0.0',
    'category': 'Extra Tools',
    'author': 'Odoo Mates',
    'website': 'odoomates.com',
    'license': 'AGPL-3',
    'summary': """School Management Software""",
    'description': """Module to Manage School""",
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/student.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False
}