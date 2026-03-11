from odoo import models, fields, tools

class AnalyticsDataCube(models.Model):
    _name = 'analytics.data.cube'
    _description = 'High Performance Data Cube'
    _auto = False

    partner_id = fields.Many2one('res.partner', string="Customer", readonly=True)
    total_revenue = fields.Float(string="Total Revenue", readonly=True)
    order_count = fields.Integer(string="Orders", readonly=True)
    rfm_score = fields.Char(string="Segmentation", readonly=True)

    def init(self):
        tools.drop_view_if_exists(self.env.cr, self._table)
        self.env.cr.execute(f"""
            CREATE OR REPLACE VIEW {self._table} AS (
                SELECT 
                    min(so.id) as id,
                    so.partner_id,
                    COUNT(so.id) as order_count,
                    SUM(so.amount_total) as total_revenue,
                    CASE 
                        WHEN COUNT(so.id) > 5 THEN 'VIP'
                        ELSE 'Standard'
                    END as rfm_score
                FROM sale_order so
                WHERE so.state IN ('sale', 'done')
                GROUP BY so.partner_id
            )
        """)