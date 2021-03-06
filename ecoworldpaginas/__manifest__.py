# -*- coding: utf-8 -*-
{
    'name': "ecoWORLD Paginas",

    'summary': """
        Paginas basicas de la web de ecoWORLD""",

    'description': """
        Aqui estan las paginas basicas necesarias para la web como por ejemplo la pagina de inicio
    """,

    'author': "ecoWORLD",
    'website': "https://www.eco-world.es",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'ecoWORLD',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website'],

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
	# Anadimos para que aparezca en aplicaicones a la primera
    'application': True,
}