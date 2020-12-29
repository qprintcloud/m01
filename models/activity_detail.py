from odoo import models,fields

class ActivityDetail(models.Model):
    _name ="m01.activity_detail"
    _description = "Model for activity Detail "

    activity_category_id = fields.Many2one("m01.activity_category", required=True, string="กิจกรรม")
    main_activity_id = fields.Many2one("m01.main_activity", requied=True)
    period = fields.Many2many("date.range")
    unit = fields.Many2one('uom.uom',string="หน่วยนับ")
    volume  = fields.Integer("ปริมาณ")
    report_date = fields.Datetime("ณ เดือนที่รายงาน")
    accumulate = fields.Float(string="สะสม")
    activity_report = fields.Html("รายละเอียดผลการปฏิบัติงานโดยสังเขป")