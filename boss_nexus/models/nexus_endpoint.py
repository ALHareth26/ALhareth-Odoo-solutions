from odoo import models, fields, api, _
from odoo.exceptions import UserError

class NexusEndpoint(models.Model):
    _name = 'nexus.endpoint'
    _description = 'API Command Endpoint'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Node Name", required=True, tracking=True)
    provider = fields.Selection([
        ('shopify', 'Shopify'),
        ('stripe', 'Stripe'),
        ('custom', 'Custom REST')
    ], default='custom', string="Type")
    
    endpoint_url = fields.Char(string="URL", required=True)
    api_key = fields.Char(string="API Key", password=True)
    status = fields.Selection([
        ('draft', 'Draft'),
        ('online', 'Online'),
        ('offline', 'Error')
    ], default='draft', tracking=True)

    health_score = fields.Float(string="Stability", compute="_compute_health")

    @api.depends('status')
    def _compute_health(self):
        for record in self:
            record.health_score = 100.0 if record.status == 'online' else 0.0

    def action_ping(self):
        self.ensure_one()
        if not self.api_key:
            self.status = 'offline'
            # Triggering a standard Odoo error if key is missing
            raise UserError(_("Security Key Missing!"))
        
        self.status = 'online'
        return {
            'effect': {
                'fadeout': 'slow',
                'message': "Nexus Link Online",
                'type': 'rainbow_man',
            }
        }