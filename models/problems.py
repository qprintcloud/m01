from odoo import models,fields

class Problems(models.Model):
    _name ="m01.problem"

    plan_type_id  = fields.Many2one("m01.plan_type")
    problem = fields.Html("ปัญหา-อุปสรรค")
    suggest = fields.Html("ขอเสนอแนะแนวทางแก้ไข")