# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _



class AccountMove(models.Model):
    _inherit = 'account.move'

    from_date_empty = fields.Date(string="From Empty Date")
    to_date_empty = fields.Date(string="To Empty Date")

    def action_invoice_empty(self):
        print('fdgdf')
        for each in self.env['account.move'].search([('invoice_date', '<=', self.to_date_empty),('invoice_date', '>=', self.from_date_empty)]):
            print(each,'each')
            each.system_inv_no =False
