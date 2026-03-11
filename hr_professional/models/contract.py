from odoo import models, fields, api

class HrContract(models.Model):
    _inherit = 'hr.contract'

    @api.model
    def create(self, vals):
        res = super(HrContract, self).create(vals)
        if res.employee_id and res.date_start:
            res.employee_id.employment_date = res.date_start
        return res