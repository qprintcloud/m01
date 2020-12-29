from odoo import fields,models

class SubProject(models.Model):
    _name ="m01.sub_project"

    name = fields.Char("โครงการรอง")

class Project(models.Model):
    _name ="m01.project"

    name = fields.Char("โครงการหลัก")
    sub_project_id = fields.Many2one("m01.sub_project")

    