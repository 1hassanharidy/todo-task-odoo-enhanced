from odoo import fields, models, api
from odoo.exceptions import ValidationError


class TodoTask(models.Model):
    _name = 'todo.task'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Todo Task table'
    _rec_name = 'task_name'

    task_name = fields.Char(required=True)
    description = fields.Char()
    due_date = fields.Date(tracking=True)
    status = fields.Selection([
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('closed', 'Closed'),
    ], default='new', tracking=True)
    estimated_time = fields.Integer()
    is_late = fields.Boolean(readonly=True)

    assign_to_id = fields.Many2one('res.partner', tracking=True)

    line_ids = fields.One2many('todo.task.line', 'task_id')

    active = fields.Boolean(default=True)

    @api.constrains('line_ids')
    def check_total_time_lines(self):
        for task in self:
            if task.estimated_time:
                total_time = sum(line.task_time for line in task.line_ids)
                if total_time > task.estimated_time:
                    raise ValidationError(
                        f"The total timesheet hours {total_time} cannot exceed the estimated hours {task.estimated_time} for this task."
                    )

    def action_close(self):
        for rec in self:
            rec.status = 'closed'

    def check_due_date(self):
        print('Inside check_due_date method')
        task_ids = self.search([])
        for rec in task_ids:
            if rec.status not in ['completed', 'closed']:
                if rec.due_date and rec.due_date < fields.date.today():
                    rec.is_late = True
            else:
                rec.is_late = False

class TodoTaskLine(models.Model):
    _name = 'todo.task.line'
    _description = 'Todo Tasks Timesheet'

    task_date = fields.Date()
    task_description = fields.Char()
    task_time = fields.Integer()

    task_id = fields.Many2one('todo.task')


