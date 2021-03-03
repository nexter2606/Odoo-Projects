# -*- coding: utf-8 -*-
{
    'name': "aspl_product_commision",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','sale_crm','crm'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/commision_views.xml',
        'views/product_views.xml',
        'views/sale_views.xml',
        'views/lead_views.xml',
        'wizard/project.xml',
        'wizard/register_payment.xml',
        'views/templates.xml',
        'wizard/save_wizard.xml',
        'reports/report.xml',
        'reports/project_card.xml',
        'reports/project_data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
