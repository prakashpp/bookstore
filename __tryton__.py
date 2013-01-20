# -*- coding: UTF-8 -*-
# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

{
    'name': 'Book Store',
    'description': '''Book Store''',
    'version': '2.4.0.1',
    'author': 'Prakash Pandey',
    'email': 'prakashpp.pandey@gmail.com',
    'website': '',
    'depends': [
        'ir',
        'res',
        'party',
        'company',
        'product',
    ],
    'xml': [
        'product.xml',
        'party.xml',
        'bookstore.xml',
    ],
    'translation': [
    ],
}
