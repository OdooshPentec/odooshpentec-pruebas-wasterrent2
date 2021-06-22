"""Model: Simple domain.
"""

from odoo import models, fields, _


class SimpleDomain(models.Model):
    _name = 'simple.domain'
    _description = _('Simple domain')

    name = fields.Char(
        string='Name',
        required=True
    )
    code = fields.Char(
        string='Code',
        required=True
    )
    type = fields.Char(
        string='Type',
        required=True
    )
    description = fields.Char('Description')
    active = fields.Boolean(
        string='Active',
        default=True
    )

    _sql_constraints = [
        (
            _('Code field as unique'),
            'unique(code, type)',
            _('Field Code must be unique for the same type')
        )
    ]
