from odoo import models, fields, api
from datetime import date

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    employment_date = fields.Date(string="Start of Employment")
    end_of_employment = fields.Date(string="End of Employment")
    hr_notes = fields.Text(string="Professional Notes")
    employment_status = fields.Selection([
        ('active', 'Active'),
        ('terminated', 'Terminated')
    ], string="Status", compute="_compute_status", store=True)

    @api.depends('end_of_employment')
    def _compute_status(self):
        for rec in self:
            if rec.end_of_employment and rec.end_of_employment <= date.today():
                rec.employment_status = 'terminated'
            else:
                rec.employment_status = 'active'