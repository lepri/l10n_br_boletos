# -*- encoding: utf-8 -*-
#                                                                            #
#   OpenERP Module                                                           #
#   Copyright (C) 2014 Gustavo Lepri <gustavolepri@gmail.com>                #
#                                                                            #
#   This program is free software: you can redistribute it and/or modify     #
#   it under the terms of the GNU Affero General Public License as           #
#   published by the Free Software Foundation, either version 3 of the       #
#   License, or (at your option) any later version.                          #
#                                                                            #
#   This program is distributed in the hope that it will be useful,          #
#   but WITHOUT ANY WARRANTY; without even the implied warranty of           #
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the            #
#   GNU Affero General Public License for more details.                      #
#                                                                            #
#   You should have received a copy of the GNU Affero General Public License #
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.    #
#                                                                            #

{
    "name": "Odoo Boletos",
    "version": "1.0a",
    "depends": [
        "l10n_br_account",
        "document",
    ],
    "author": "Gustavo Lepri",
    "category": "Account",
    "description": """
    Module to create brazilian boletos. It's base on boleto addon from Proge
    Company Boleto conf in menu Administration->Company->l10n_br->boletos
    Partner Boleto conf in Partner form.
    Wizard to generate boletos in Invoice form.
    In Sale Journal the field gera_financeiro must be checked.
    You have to instal pyboleto library(http://pypi.python.org/pypi/pyboleto), pip install pyboleto
    """,
    "init_xml": [],
    'update_xml': [
        'partner_view.xml',
        'company_view.xml',
        'wizard/boleto_create_view.xml',
    ],
    'demo_xml': [],
    'installable': True,
    'active': False,
}
