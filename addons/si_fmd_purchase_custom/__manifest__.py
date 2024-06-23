# -*- coding: utf-8 -*-
{
    'name': "SI FMD Purchase Customization",

    'summary': """SI FMD Purchase Customization""",

    'description': """
        SI develop app/module for FMD to customize purchase module
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
    'depends': ['base','purchase','stock','hr'],

    # always loaded
    'data': [
        'views/purchase_order_rm_views.xml',
        'actions/purchase_order_rm_actions.xml',
        'views/purchase_request_views.xml',
        'actions/purchase_request_actions.xml',
        'report/report_purchase_request.xml',
        'report/report_purchase_request_template.xml',
        'views/purchase_order_menu.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
    'installable': True,
	'auto_install': False,
	'application': True,
}
