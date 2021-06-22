# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class ProductTemplate(models.Model):
    _inherit = "product.template"

    # Comunes
    product_class = fields.Selection(string="Product class",
        selection=[
            ('is_vehicle', 'Is vehicle'),
            ('is_product', 'Is product'),
            ('is_vehicle_equip', 'Is vehicle equipment')
        ], default='is_product')

    # Equipo
    equipment_img1 = fields.Binary(related='equipment_id.img1')
    equipment_img2 = fields.Binary(related='equipment_id.img2')
    equipment_img3 = fields.Binary(related='equipment_id.img3')

    equipment_id = fields.Many2one(comodel_name='maintenance.equipment', string='Vehicle/Equipment', ondelete='cascade')
    equipment_type_id = fields.Many2one(related='equipment_id.equipment_type_id', string='Equipment type')
    equipment_category_id = fields.Many2one(related='equipment_id.categ_id', string='Equipment Category')
    equipment_brand_id = fields.Many2one(related='equipment_id.equipment_brand_id', string='Equipment brand')
    equipment_model_id = fields.Many2one(related='equipment_id.equipment_model_id', string='Equipment model')
    equipment_version = fields.Char(related='equipment_id.equipment_version', string="Version")
    equipment_serial_no = fields.Char(related='equipment_id.serial_no', string='Serial Number', copy=False, store=True)
    equipment_chassis_number = fields.Char(related='equipment_id.chassis_number',string="Chassis number", copy=False, store=True)

    # Vehiculo
    state = fields.Many2one(related='equipment_id.state', string='State')
    location = fields.Char(related='equipment_id.location', string='Location')
    last_km = fields.Float(related='equipment_id.last_km', string='Last km', readonly=False)
    car_registration = fields.Char(related='equipment_id.car_registration', string='Car registration')
    current_customer = fields.Char(related='equipment_id.current_customer', string='Current customer')
    id_webfleet = fields.Char(related='equipment_id.id_webfleet', string='ID Webfleet')

    _sql_constraints = [
        (
            _('chassis_number_unique'),
            'unique(equipment_chassis_number)',
            _('Chassis number be unique for the equipment')
        ),
        (
            _('equipment_serial_no_unique'),
            'unique(equipment_serial_no)',
            _('Serial number be unique for the equipment')
        )
        ]