from odoo import models, fields

class AccountMove(models.Model):
    _inherit = 'account.move'

    state = fields.Selection(
        selection_add=[
            ('draft', 'Draft'),
            ('to_approve', 'To Approve'),
            ('posted', 'Posted')
        ],
        string='State',
        ondelete={'to_approve': 'set default'}
    )

    def action_post(self):
        self.state = 'to_approve'