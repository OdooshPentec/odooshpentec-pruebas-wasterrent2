"""Model: Simple domain.
"""

from odoo import models, fields, _


class EquipmentBrand(models.Model):
    _name = 'equipment.brand'
    _description = _('Equipment brand')
    _order = 'sequence'

    sequence = fields.Integer()
    name = fields.Char(
        string='Brand',
        required=True
    )
    equipment_type_id = fields.Many2one(comodel_name='simple.domain', string='Equipment type',
                                        domain=[('type', '=', 'equipment_type')])

    active = fields.Boolean(
        string='Active',
        default=True
    )
