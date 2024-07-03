from odoo import models, fields, api

class Department(models.Model):
    _inherit = 'hr.department'

    total_status = fields.Integer(string='Total status', compute='_compute_total_status')
    status_ids = fields.One2many('hr.employee.status', 'department_id', string='Statuses')
    
    @api.depends('status_ids.name')
    def _compute_total_status(self):
        for department in self:
            unique_statuses = department.status_ids.mapped('name')
            department.total_status = len(unique_statuses)

    def action_update_total_status(self):
        for department in self:
            unique_statuses = department.status_ids.mapped('name')
            department.total_status = len(unique_statuses)
