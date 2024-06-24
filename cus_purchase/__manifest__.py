# -- coding: utf-8 --
{
    'name': 'Cus Purchase',
    'sequence': -500,
    'author': 'Cloud infosoft',
    'version': '17.0',
    'license': 'LGPL-3',
    'depends': ['base','purchase','account','mail','contacts'],
    'data': ['views/purchase.xml',
             'views/res_user.xml',
             'views/state_approve.xml',
             'views/custom_mail_template.xml'],
    'auto_install': False,
    'application': True,
    'installable': True,
}
