# -*- coding: utf-8 -*-
{
    'name': "SI FMD Inventory Customization",

    'summary': """SI FMD Inventory Customization""",

    'description': """
        SI develop app/module for FMD to customize inventory module
    """,

    'author': "SI",
    'website': "https://sense-infinite.com/about-us",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'SI',
    'version': '1.0.0',
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base','purchase','stock'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/sag_type_views.xml',
        'actions/sag_type_actions.xml',
        'menus/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
    'installable': True,
	'auto_install': False,
	'application': True,
}
