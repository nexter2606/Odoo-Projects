{

    'name': 'Hospital Management',
    'version': '1.1',
    'summary': 'Hospital Management ',
    'description': """
hospital management system
  """,
    'website': 'https://www.odoo.com/page/billing',
    'depends': ['base','sale'],
    'data': [
        'security/ir.model.access.csv',
        'data/doctor_note_data.xml',
        'data/ir_sequence_data.xml',
        'wizards/appointment_wizard_views.xml',
        'wizards/doctor_visit_wizard_views.xml',
        'views/res_partner_views.xml',
        'views/medicine_views.xml',
        'views/appointment_views.xml',
        'views/doctor_views.xml',
        'views/doctor_visit_views.xml',
        'views/doctor_visit_line_views.xml',
        'views/doctor_notes_views.xml',
        
        

        
        
    ],
    'installable': True,
    'auto_install': False,

}

