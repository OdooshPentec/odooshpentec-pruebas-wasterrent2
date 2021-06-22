"""Model: Simple domain.
"""

from odoo import models, fields, _


class EquipmentModel(models.Model):
    _name = 'equipment.model'
    _description = _('Equipment model')
    _order = 'sequence'

    sequence = fields.Integer()
    name = fields.Char(
        string='Model',
        required=True
    )
    brand_id = fields.Many2one(comodel_name='equipment.brand', string='Brand')
    
    active = fields.Boolean(
        string='Active',
        default=True
    )
