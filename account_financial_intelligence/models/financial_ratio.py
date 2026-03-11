from odoo import models, fields, api

class FinancialRatio(models.Model):
    _name = 'financial.ratio.analysis'
    _description = 'Accounting Ratio Engine'

    name = fields.Char(string="Analysis Period", required=True, default="Monthly Review")
    date = fields.Date(default=fields.Date.context_today)
    
    current_assets = fields.Float(compute="_compute_ratios", string="Current Assets")
    current_liabilities = fields.Float(compute="_compute_ratios", string="Current Liabilities")
    liquidity_ratio = fields.Float(compute="_compute_ratios", string="Current Ratio")

    @api.depends('date')
    def _compute_ratios(self):
        for rec in self:
            # Calculate Total Current Assets
            assets = self.env['account.move.line'].search([
                ('account_id.account_type', 'in', ['asset_current', 'asset_receivable']),
                ('parent_state', '=', 'posted')
            ])
            # Calculate Total Current Liabilities
            liabs = self.env['account.move.line'].search([
                ('account_id.account_type', 'in', ['liability_current', 'liability_payable']),
                ('parent_state', '=', 'posted')
            ])
            
            rec.current_assets = sum(assets.mapped('balance'))
            rec.current_liabilities = abs(sum(liabs.mapped('balance')))
            
            if rec.current_liabilities > 0:
                rec.liquidity_ratio = rec.current_assets / rec.current_liabilities
            else:
                rec.liquidity_ratio = 0.0