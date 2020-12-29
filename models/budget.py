from odoo import models,fields,api

class BudgetType(models.Model):
    _name = 'm01.budget_type'

    name = fields.Char("ประเภทงบประมาณ")

class Budget(models.Model):
    _name = "m01.budget"

    plan_type_id = fields.Many2one("m01.plan_type",string="แผนงาน")
    budget_type_id = fields.Many2one("m01.budget_type",string="ประเภทงบประมาณ")
    budget_amount = fields.Float(string="งบที่ได้รับการจัดสรร",default=1.0)
    disburse_report_date = fields.Date(string="ณ เดือนที่รายงาน")
    disburse_accumulate = fields.Float(string="สะสม",default=1.0)
    percentage_disburse = fields.Float(compute="_compute_percentage_disburse",string="ร้อยละการเบิกจ่าย")


    @api.depends('budget_amount','disburse_accumulate')
    def _compute_percentage_disburse(self):
        if self.budget_amount != 0.0:
            if self.disburse_accumulate != 0.0:
                    for record in self:
                        record.percentage_disburse = (float(record.disburse_accumulate) * 100) / float(record.budget_amount)
        

