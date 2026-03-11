from odoo import models, fields, api

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    # حقول الرواتب
    basic_salary = fields.Float(string="الراتب الأساسي")
    housing_allowance = fields.Float(string="بدل السكن")
    transport_allowance = fields.Float(string="بدل النقل")
    insurance_deduction = fields.Float(string="خصم التأمينات")
    net_salary = fields.Float(string="صافي الراتب", compute="_compute_net_salary", store=True)

    # حقول التقييم والبيانات
    performance_score = fields.Selection([
        ('1', 'ضعيف'),
        ('2', 'مقبول'),
        ('3', 'جيد'),
        ('4', 'ممتاز'),
        ('5', 'استثنائي')
    ], string="تقييم الأداء")
    
    registration_number = fields.Char(string="رقم الموظف الخاص")
    employment_document = fields.Binary(string="مرفق العقد/الهوية")

    @api.depends('basic_salary', 'housing_allowance', 'transport_allowance', 'insurance_deduction')
    def _compute_net_salary(self):
        for rec in self:
            total_allowances = rec.basic_salary + rec.housing_allowance + rec.transport_allowance
            rec.net_salary = total_allowances - rec.insurance_deduction