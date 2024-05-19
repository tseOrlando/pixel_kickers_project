# -*- coding: utf-8 -*-
{
    'name': "Marqueting Digital",
    'summary': """
        Module for managing digital marketing records and emails.""",
    'description': """
        This module allows users to manage digital marketing campaigns and related emails.
    """,
    'author': "Ramon",
    'website': "https://www.yourwebsite.com",
    'category': 'Marketing',
    'version': '0.1',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/marqueting_digital_views.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}
