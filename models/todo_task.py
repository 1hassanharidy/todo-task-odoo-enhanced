from odoo import fields, models

class TodoTask(models.Model):
    _name = 'todo.task'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Todo Task table'

    task_name = fields.Char(required=True)
    description = fields.Char()
    due_date = fields.Date(tracking=True)
    status = fields.Selection([
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ], default='new', tracking=True)

    assign_to_id = fields.Many2one('res.partner', tracking=True)
