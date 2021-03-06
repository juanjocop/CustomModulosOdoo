# -*- coding: utf-8 -*-
{
    'name': "Testimonios",

    'summary': """
        Modulo para testimonios de clientes de ecoWORLD""",

    'description': """
        Este modulo esta diseñado para mostrar en la web los testimonios de los clientes de ecoWORLD
    """,

    'author': "ecoWORLD",
    'website': "https://www.eco-world.es",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'ecoWORLD',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website', 'ecoworld'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    # Añadimos para que aparezca en aplicaicones a la primera
    'application': True,
}
