# -*- coding: utf-8 -*-

{
    'name': "Total Number Of Products And Quantity On RFQ / Purchase Order",
    'author': 'Odoo Circle',
    'category': 'Purchases',
    'summary': """Display Total Number Of Products And Quantity On RFQ / Purchase Order""",
    'license': 'AGPL-3',
    'website': 'http://www.odoocircle.com',
    'description': """
""",
    'version': '19.0.0.1',
    'depends': ['base','purchase'],
    'data': ['security/purchase_order_security.xml',
             'views/purchase_order_view.xml',
             'report/purchase_report_templates.xml',
             'report/purchase_quotation_templates.xml'],
    'images': ['static/description/banner.jpg'],
    'installable': True,
    'application': True,
    'auto_install': False,
}




