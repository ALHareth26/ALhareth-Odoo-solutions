from odoo import models, fields

class HrEmployeeAssets(models.Model):
    _name = 'hr.employee.assets'
    _description = 'Employee Assets Management'

    name = fields.Char(string="اسم العهدة", required=True)
    employee_id = fields.Many2one('hr.employee', string="الموظف المستلم")
    serial_number = fields.Char(string="الرقم التسلسلي")
    issue_date = fields.Date(string="تاريخ التسليم", default=fields.Date.today)
    asset_value = fields.Float(string="قيمة العهدة")
    state = fields.Selection([
        ('draft', 'جديد'),
        ('assigned', 'تم التسليم'),
        ('returned', 'تم الاسترجاع')
    ], string="الحالة", default='draft')