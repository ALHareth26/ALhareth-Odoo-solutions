from odoo import models, fields, api

class AnalyticsQuery(models.Model):
    _name = 'analytics.query.engine'
    _description = 'Manual Analytics Processor'

    name = fields.Char(string="Process Name", default="Main Data Sync")
    last_run = fields.Datetime(default=fields.Datetime.now)

    def action_refresh_data(self):
        self.env.cr.execute("ANALYZE analytics_data_cube;")
        return True