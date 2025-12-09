# -*- coding: utf-8 -*-

from odoo import models, fields
from odoo import api


class MotsoftResPartner(models.Model):
    _inherit = 'res.partner'

    alternative_name = fields.Char(string="Nombre alternativo", store=True)
    customer = fields.Boolean('Es Cliente', default=False, store=True)
    supplier = fields.Boolean('Es Proveedor', default=False, store=True)
    bank_name = fields.Char(string="Nombre proporcionado por el banco", store=True)

    # def open_partner_form(self):
    #     self.ensure_one()
    #
    #     action_id = self.env.ref('contacts.action_contacts').read()[0]
    #
    #     if action_id:
    #         return {
    #             'id': action_id['id'],
    #             'name': action_id['name'],
    #             'type': action_id['type'],
    #             "res_model": "res.partner",
    #             'view_type': 'form',
    #             'view_mode': 'form',
    #             'search_view_id': action_id['search_view_id'],
    #             'help': action_id['help'],
    #             'res_id' : self._context.get('active_id'),
    #         }
    #
    #     return None

    # def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
    #     data = super(DeysankaResPartner, self)._name_search(name, args, operator=operator, limit=limit, name_get_uid=name_get_uid)
    # @api.model
    # def _name_search(self, name, domain=None, operator='ilike', limit=100, order=None):
    #     data = super(DeysankaResPartner, self)._name_search(name=name, domain=domain, operator=operator,
    #                                                         limit=limit, order=order)
    #
    #     if isinstance(data, list):
    #         data += self.env["res.partner"].search(["|",
    #                                                 ("bank_name", "ilike", name),
    #                                                 ("alternative_name", "ilike", name)]).ids
    #
    #     return data
