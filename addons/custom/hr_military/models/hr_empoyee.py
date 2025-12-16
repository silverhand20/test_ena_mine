from odoo import fields, models

class HrEmployee(models.Model):
    _inherit = "hr.employee"

    is_reserved = fields.Boolean(string="Бронювання")
    is_mobilized = fields.Boolean(string="Мобілізований")
    tck_sp_id = fields.Many2one("tck.sp", string="ТЦК та СП")
    edrpvr_number = fields.Char(string="№ в ЄДРПВР")
