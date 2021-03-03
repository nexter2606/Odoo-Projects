# -*- coding: utf-8 -*-
{
    'name': "clinic_management",

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
    'depends': ['base','mail','account','sale','board','project'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/patient_views.xml',
        'views/doctor_views.xml',
        'views/appointment_views.xml',
        'views/visit_views.xml',
        'views/visit_line_views.xml',
        'views/medicine_views.xml',
        'views/invoice_views.xml',
        'views/invoice_line_views.xml',
        'views/doctor_team_views.xml',
        'views/mass_visits.xml',
        'views/project_config.xml',
        'views/dashboard.xml',
        'views/assets.xml',
        'views/sql_views.xml',
        'views/task_views.xml',
        'views/user_timesheet.xml',
        'views/user_timesheet_line.xml',
        'wizard/create_appointment_views.xml',
        'data/ir_sequence_data.xml',
        'reports/report.xml',
        'reports/visit_card.xml',
        'reports/visit_data.xml',
        'reports/invoice_card.xml',
        'reports/chatter_card.xml',
        'reports/appointment_card.xml',
        'data/email_template.xml',
        'wizard/appointment_report_views.xml',
        'wizard/save_wizard.xml',
        'wizard/csv_record_views.xml',
        
    ],

    'qweb': [
        'static/src/xml/*.xml'
    ],
    
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
