# wizards.py

# from odoo import models, fields, api
#
# class CustomMailTemplate(models.Model):
#     _name = 'custom.mail.template'
#     _inherit = 'mail.mail'


from odoo import models, fields, api


class CustomMailTemplate(models.Model):
    _inherit = 'mail.mail'

    @api.model
    def create_custom_mail(self, recipient_id, invoice_url):
        body_html = """
            <div>
                <p>
                    <strong>Dear Mitchell Admin,</strong>
                </p>
                <p>
                    An Invoice from <strong>Marc Demo</strong> is awaiting your approval to be posted.<br/> 
                    Please, access it from the button below:
                </p>
                <a href="{invoice_url}" style="background-color: green; color: white; border: none; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer;">
                    View Invoice
                </a>
            </div>
        """.format(invoice_url=invoice_url)

        mail_values = {
            'subject': 'Invoice Approval Request',
            'body_html': body_html,
            'email_to': recipient_id.email,
        }

        mail = self.create(mail_values)
        return mail


class ResPartner(models.Model):
    _inherit = 'res.partner'

    def send_invoice_approval_mail(self, invoice_url):
        mail_template = self.env['mail.mail']
        for partner in self:
            mail_template.create_custom_mail(partner, invoice_url)
