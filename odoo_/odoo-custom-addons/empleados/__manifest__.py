# __manifest__.py
{
    'name': 'Empleados',
    'version': '1.0',
    'summary': 'Manage employees in your company',
    'sequence': -100,
    'description': """Module to manage employees""",
    'category': 'Human Resources',
    'author': 'Your Name',
    'website': 'http://www.yourcompany.com',
    'depends': ['base'],
    'data': [
        'views/views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'empleados/static/src/css/employee_styles.css',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
}
