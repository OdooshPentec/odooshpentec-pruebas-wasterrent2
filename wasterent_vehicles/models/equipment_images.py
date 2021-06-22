"""Model: Simple domain.
"""

from odoo import models, fields, _


class EquipmentImages(models.Model):
    _name = 'equipment.images'
    _description = _('Equipment images')
    _order = 'sequence'

    sequence = fields.Integer()
    name = fields.Char(
        string='Name',
        required=True
    )
    type_id = fields.Many2one(comodel_name='simple.domain', string='Type',
                                        domain=[('type', '=', 'equipment_images')])
    image = fields.Binary(string='Image')

    active = fields.Boolean(
        string='Active',
        default=True
    )
    equipment_id = fields.Many2one(comodel_name='maintenance.equipment', string='Equipment')

