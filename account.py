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




from openerp.osv import fields, osv, orm
from openerp.tools.translate import _
import openerp.addons.decimal_precision as dp
from datetime import datetime


class account_invoice(osv.osv):
    _inherit = 'account.invoice'
    
    def write(self, cr, uid, ids, vals, context=None):
        result = super(account_invoice, self).write(cr, uid, ids, vals, context)
        if vals.get('state') == 'open':
            for invoice in self.browse(cr, uid, ids, context):
                if not invoice.type in ('in_invoice','in_refund'):
                    continue
                domain = []
                domain.append( ('commercial_partner_id','=',invoice.commercial_partner_id.id) )
                domain.append( ('type','=',invoice.type) )
                domain.append( ('date_invoice', '=', invoice.date_invoice) )
                domain.append( ('supplier_invoice_number', '=', invoice.supplier_invoice_number) )
                domain.append( ('state','in', ('open','done')) )
                invoice_ids = self.search(cr, uid, domain, context=context)
                if len(invoice_ids) > 1:
                    text = []
                    for invoice in self.browse(cr, uid, invoice_ids, context):
                        text.append( _('Partner: %s\nInvoice Reference: %s') % ( invoice.commercial_partner_id.name, invoice.supplier_invoice_number ) )
                    text = '\n\n'.join( text )
                    raise osv.except_osv( _('Validation Error'), _('The following supplier invoices have duplicated information:\n\n%s') % text)
        return result




# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
