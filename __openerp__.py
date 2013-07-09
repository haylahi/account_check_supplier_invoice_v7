# -*- coding: utf-8 -*-
##############################################################################
#
#    account_group_invoice_lines module for OpenERP, Change method to group invoice lines in account
#    Copyright (C) 2013 CREATIVE PLUS)
#              Haythem Lahmadi <cplus.contact@gmail.com>
#
#    This file is a part of account_group_invoice_lines
#
#    account_group_invoice_lines is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    account_group_invoice_lines is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Account Check Supplier invoice',
    'version': '1.0',
    "category": 'Accounting & Finance',
    'complexity': "easy",
    'description': """Check Duplicate Supplier Invoice
    """,
    'author': 'Haythem Lahmadi',
    'website': 'cplus.contact@gmai.com',
    'depends': [
        'base',
        'account',
    ],

    'data': ['account_view.xml'
        
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
