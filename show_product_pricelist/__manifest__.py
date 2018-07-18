# -*- coding: utf-8 -*-
##############################################################################
#
#    ODOO, Open Source Management Solution
#    Copyright (C) 2016 Steigend IT Solutions
#    For more details, check COPYRIGHT and LICENSE files
#
##############################################################################
{
    'name': "Show Price List MFH.",
    'summary': """Show Price List.""",
    'description': """
        - Show price list price in products and / or variants.
        - Define a default price list for the company.
        - If you change or add a price to the product / variant, the price list is modified.
    """,
    'author': "Falcon Solutions SpA",
    'maintainer': 'Falcon Solutions SpA',
    'website': 'http://www.falconsolutions.cl',
    'license': 'AGPL-3',
    'category': 'Sale',
    'version': '10.0.1',
    'depends': ['sale'],
    'data': [
        'views/res_company_view.xml',
        'views/product_view.xml',
    ],
      'images': ['static/description/banner.jpg'],
}
