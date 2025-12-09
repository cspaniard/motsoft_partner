# -*- coding: utf-8 -*-
{
    'name': "motsoft_partner",

    'summary': "Incrementa la funcionalidad de los contactos.",

    'description': """
Añade nuevos campos tanto para operativa como para mejor manejo de los contactos.
    * alternative_name: Nombre alternativo
    * customer: Es Cliente (True/False)
    * supplier: Es Proveedor (True/False)
    * bank_name: Nombre proporcionado por el banco en los extractos.

    """,

    'author': "David Sanromá",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '17.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/res_partner.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
