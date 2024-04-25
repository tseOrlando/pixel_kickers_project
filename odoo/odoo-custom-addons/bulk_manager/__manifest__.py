# -*- coding: utf-8 -*-
{
    'name': "bulk_manager",

    'summary': """
        Keep things tidy!""",

    'description': """
    This app will be used to organize all the bulks used for the Pixel Kickers Project
    """,

    'author': "Tesé Orlando Araujo Sagardoy",
    'website': "",
    
    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base'],

    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    
    'demo': [
        'demo/demo.xml',
    ],
}
