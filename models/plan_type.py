from odoo import models,fields

class PlanType(models.Model):
    _name = "m01.plan_type" # เปลี่ยนให้ตรงกับชื่อโปรเจ็คของแต่ละคน

    name = fields.Char("หัวข้อแผนงาน",required = True)
    is_enable = fields.Boolean("ยังใช้อยู่ไหม",default=True)
