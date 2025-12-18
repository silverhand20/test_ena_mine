from odoo import fields, models

class TckSp(models.Model):
    _name = "tck.sp"
    _description = "ТЦК та СП"

    name = fields.Char(string="Назва ТЦК та СП", required=True)
    code = fields.Char(string="Код")
    phone = fields.Char(string="Телефон")
