from odoo import models, fields


class ResPartner(models.Model):
    _inherit = "res.partner"


    lock_confirmed_po = fields.Boolean("Customer Invoice Double Validate")

