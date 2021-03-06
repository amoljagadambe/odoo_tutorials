from odoo import fields,models,api


class ClassInfo(models.Model):
    
    _name='cl.cl'
    _rec_name = 'class_display_name'
    
    name = fields.Char('Class Name', required=True)
    teacher_name = fields.Char('Teacher Name')
    division_name = fields.Char('Division Name')
    monitor_name = fields.Char('Monitor Name')
    class_display_name = fields.Char(compute="_class_display_name",store=True)
    student_ids = fields.One2many('stud.stud','class_id','Students')
    class_strength = fields.Integer(compute="_count_strength",string='Class Strength')
    
    @api.depends('student_ids')
    def _count_strength(self):
        for rec in self:
            rec.class_strength = len(rec.student_ids.ids)
    
    
    @api.depends('name','division_name')
    def _class_display_name(self):
        for rec in self:
            if rec.name and rec.division_name:
                display_rec_name = rec.name + ' - Div ' + rec.division_name
                rec.class_display_name = display_rec_name
    
    _sql_constraints = [
        ('class_display_name_uniq', 'unique(class_display_name)', 'Class Name and Division must be unique !'),
    ]
    