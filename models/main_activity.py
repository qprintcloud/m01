from odoo import models,fields

class MainActivity(models.Model):
    _name = "m01.main_activity" # เปลี่ยนให้ตรงกับชื่อโปรเจ็คของแต่ละคน

    name = fields.Char("ชื่อกิจกรรม",required = True)
    is_enable = fields.Boolean("ยังใช้อยู่ไหม",default=True)
