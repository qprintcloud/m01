from odoo import models,fields

class Problems(models.Model):
    _name ="m01.target_farmer"

    plan_type_id  = fields.Many2one("m01.plan_type")
    farmer_group = fields.Char("กลุ่มเกษตรกร")
    farmer_count = fields.Integer(string="จำนวนเกษตรกร")
    farm_area = fields.Float(string="พื้นที่")
    farm_province = fields.Selection([
        ("BKK","กรุงเทพมหานคร"),
        ("SRT","สุราษฎร์ธานี"),
        ("NAN","น่าน"),
        ("SMK","สมุทรสาคร")]
        ,default="BKK")