# -*- coding: utf-8 -*-

from odoo import api, fields, models, _, tools
from odoo.exceptions import UserError

class MaintenanceEquipment(models.Model):
    _inherit = "maintenance.equipment"

    @tools.ormcache()
    def _get_default_category_id(self):
        return self.env.ref('product.product_category_all')

    # Comunes
    product_class = fields.Selection(string="Product class",
                                     selection=[
                                         ('is_vehicle', 'Is vehicle'),
                                         ('is_vehicle_equip', 'Is vehicle equipment'),
                                         ('is_internal_equip', 'Is internal equipment')
                                     ])
    sequence = fields.Integer()
    product_id = fields.Many2one(comodel_name='product.template', string='Associated Product', ondelete='cascade')

    @api.depends('equipment_images_ids')
    def _compute_img(self):
        for equip in self:
            if equip.equipment_images_ids:
                equip.img1 = equip.equipment_images_ids[0].image
                if len(equip.equipment_images_ids) > 1:
                    equip.img2 = equip.equipment_images_ids[1].image
                    if len(equip.equipment_images_ids) > 2:
                        equip.img3 = equip.equipment_images_ids[2].image
                    else:
                        equip.img3 = False
                else:
                    equip.img2 = False
                    equip.img3 = False
            else:
                equip.img1 = False
                equip.img2 = False
                equip.img3 = False

    img1 = fields.Binary(string='Img1', compute=_compute_img)
    img2 = fields.Binary(string='Img2', compute=_compute_img)
    img3 = fields.Binary(string='Img3', compute=_compute_img)

    categ_id = fields.Many2one(
        'product.category', 'Product Category',
        change_default=True, default=_get_default_category_id, group_expand='_read_group_categ_id',
        required=True, help="Select category for the current product")

    equipment_type_id = fields.Many2one(comodel_name='simple.domain', string='Equipment type',
                                        domain=[('type', '=', 'equipment_type')])
    equipment_brand_id = fields.Many2one(comodel_name='simple.domain', string='Equipment brand',
                                        domain=[('type', '=', 'equipment_brand')])
    equipment_model_id = fields.Many2one(comodel_name='simple.domain', string='Equipment model',
                                         domain=[('type', '=', 'equipment_model')])
    equipment_version = fields.Char(string="Version")
    warranty_end_date_supplier = fields.Date(string='Warranty end date (Supplier)')
    warranty_end_date_customer = fields.Date(string='Warranty end date (Customer)')
    purchase_date = fields.Date(string='Purchase date')
    fabrication_date = fields.Date(string='Fabrication date')
    associated_equipment_id = fields.Many2one(comodel_name='maintenance.equipment', string='Associated to')
    equipment_name_rel = fields.Char(string='Name', related='associated_equipment_id.name')
    equipment_serial_no_rel = fields.Char(string='Serial no', related='associated_equipment_id.serial_no')
    equipment_type_rel = fields.Many2one(string='Equipment type', related='associated_equipment_id.equipment_type_id')
    equipment_brand_rel = fields.Many2one(string='Equipment brand',
                                                   related='associated_equipment_id.equipment_brand_id')
    equipment_model_rel = fields.Many2one(string='Equipment model',
                                                   related='associated_equipment_id.equipment_model_id')
    equipment_version_rel = fields.Char(string='Equipment version',
                                                   related='associated_equipment_id.equipment_version')
    associated_equipment_ids = fields.Many2many(comodel_name='maintenance.equipment',
                                                relation='maintenance_equipment_associated_rel',
                                                column1='equipment_id',
                                                column2='associated_id',
                                                string='Associated equipments')

    equipment_images_ids = fields.One2many(comodel_name='equipment.images', inverse_name='equipment_id', string='Equipment images')
    # Extintor
    review_date = fields.Date(string='Review date')
    review_type = fields.Many2one(comodel_name='simple.domain', string='Review type',
                                         domain=[('type', '=', 'review_type')])

    # Caja de cambios
    gearbox_type = fields.Many2one(comodel_name='simple.domain', string='Gearbox type',
                                  domain=[('type', '=', 'gearbox_type')])

    # Motor
    fuel_type = fields.Many2one(comodel_name='simple.domain', string='Fuel type',
                                   domain=[('type', '=', 'fuel_type')])
    euro_regulation = fields.Many2one(comodel_name='simple.domain', string='Euro regulation',
                                domain=[('type', '=', 'euro_regulation')])
    cc = fields.Char(string='CC')
    kw = fields.Char(string='KW')

    # Vehiculo
    chassis_number = fields.Char(string="Chassis number", copy=False)
    last_hours_running= fields.Float(string='Last hours running')
    state = fields.Many2one(comodel_name='simple.domain', string='State',
                                  domain=[('type', '=', 'vehicle_state')])
    last_km = fields.Float(string='Last km')
    car_registration = fields.Char(string='Car registration')
    car_registration2 = fields.Char(string='Car registration 2')
    last_registration_date = fields.Date(string='Last registration date')
    current_customer = fields.Char(string='Current customer')
    id_webfleet = fields.Char(string='ID Webfleet')
    keys_code = fields.Char(string='Keys code')
    radio_code = fields.Char(string='Radio code')
    axles_no = fields.Integer(string='Axles no')
    axle_distance_1_2 = fields.Float(string='Axle distance 1-2 (mm)')
    axle_distance_2_3 = fields.Float(string='Axle distance 2-3 (mm)')
    width = fields.Float(string='Width (mm)')
    height = fields.Float(string='Height (mm)')
    length = fields.Float(string='Length')
    mma = fields.Integer(string='MMA')
    tachograph = fields.Boolean(string='Tachograph')
    exempt_tachograph = fields.Boolean(string='Exempt tachograph')
    exempt_itv = fields.Boolean(string='Exempt ITV')
    date_next_itv = fields.Date(string='Date next ITV')
    insurance_policy = fields.Boolean(string='Insurance policy')
    insurance_validity = fields.Boolean(string='Insurance validity')
    insurance_payment_receipt = fields.Boolean(string='Insurance payment receipt')
    ce_certificate = fields.Boolean(string='CE certificate')
    user_manual = fields.Boolean(string='User manual')
    driving_license = fields.Boolean(string='Driving license')
    exploded_manual = fields.Boolean(string='Exploded manual')
    data_sheet = fields.Boolean(string='Data sheet')
    tachograph_exemption_certificate = fields.Boolean(string='Tachograph exemption certificate')
    coc_1 = fields.Boolean(string='COC 1st phase')
    coc_2 = fields.Boolean(string='COC 2nd phase')


    def write(self, vals_list):
        res = super(MaintenanceEquipment, self).write(vals_list)
        if self.chassis_number:
            if len(self.chassis_number) != 17:
                raise UserError('The lenght of the chassis number is incorrectly')
        return res

    _sql_constraints = [
        (
            _('chassis_number_unique'),
            'unique(chassis_number)',
            _('Chassis number be unique for the equipment')
        ),
        (
            _('car_registration_unique'),
            'unique(car_registration)',
            _('Car registration be unique for the equipment')
        ),
        (
            _('car_registration2_unique'),
            'unique(car_registration2)',
            _('Car registration 2 be unique for the equipment')
        )
    ]

    @api.model
    def create(self, values):
        res = super(MaintenanceEquipment, self).create(values)
        if res.chassis_number:
            if len(res.chassis_number) != 17:
                raise UserError('The lenght of the chassis number is incorrectly')
        if res.product_class == 'is_vehicle':
            res.equipment_type_id = self.env.ref('wasterent_vehicles.product_template_equipment_type_vehicle').id
            fields = {'name': res.name,
                      'product_class': 'is_vehicle',
                      'type': 'product',
                      'categ_id': res.categ_id.id,
                      'equipment_id': res.id,
                      'equipment_type_id': res.equipment_type_id.id,
                      'equipment_brand_id': res.equipment_brand_id.id,
                      'equipment_model_id': res.equipment_model_id.id,
                      'equipment_version': res.equipment_version,
                      'equipment_chassis_number': res.chassis_number,
                      'state': res.state,
                      'location': res.location,
                      'last_km': res.last_km,
                      'car_registration': res.car_registration,
                      'current_customer': res.current_customer,
                      'id_webfleet': res.id_webfleet,
                      }
            res.product_id = self.env['product.template'].create(fields)
        return res
    '''
    def write(self, values):
        res = super(MaintenanceEquipment, self).write(values)
        if self.equipment_type_id.id == self.env.ref('wasterent_vehicles.product_template_equipment_type_vehicle').id:
            fields = {'name': self.name,
                      'is_vehicle': True,
                      'vehicle_id': self.id}
            self.product_id = self.env['product.template'].create(fields)
        return res
    '''

    @api.onchange('product_class')
    def check_class(self):
        if self.product_class:
            if self.product_class == 'is_vehicle':
                self.equipment_type_id = self.env.ref('wasterent_vehicles.product_template_equipment_type_vehicle').id
            elif self.product_class == 'is_internal_equip':
                self.equipment_type_id = self.env.ref('wasterent_vehicles.product_template_equipment_type_internal_equipment').id
    '''
    @api.onchange('equipment_type_id')
    def check_equipment_type_id(self):
        if self.equipment_type_id:
            if self.equipment_type_id.id in [self.env.ref('wasterent_vehicles.product_template_equipment_type_vehicle').id,self.env.ref('wasterent_vehicles.product_template_equipment_type_internal_equipment').id]:
                raise UserError('The equipment type for Vehicle equipment type cannot be "Vehicle" or "Internal equipment"')
    '''