from odoo import models,fields

class ActivityCategory(models.Model):
    _name = "m01.activity_category" # เปลี่ยนให้ตรงกับชื่อโปรเจ็คของแต่ละคน

    name = fields.Char("ชื่อกิจกรรมหลัก",required = True)
    is_enable = fields.Boolean("ยังใช้อยู่ไหม",default=True)
    main_activity_ids = fields.Many2many("m01.main_activity")
