## [Unidad 6](../index.md)
# Practica 3


Para esta practica lo que hemos hecho es crear varios campos calculados y restricciones tanto sql como python.

Lo que hay que tener en cuenta a la hora de crear un campo calculado es que siempre empiezan poniendo de que campos dependen que esten rellenados y con la iteraccion de self. A la hora de operar con los campos siempre se llamaran 'record.NOMBRE_CAMPO'.

Para las restricciones SQL hay que añadir una linea debajo de la descripcion del modulo que se llama '_sql_constraints', que contendra una lista de las restricciones con este formato *('NOMBRE_RESTRICCION', OPERACION_RESTRICCION, 'MENSAJE DE ERROR')*.

Para las restricciones en python hay que definir la funcion que comprueba el valor que queremos, esta funcion sera igual que las de los campos calculados solo que contendra un if y si se cumple se muestra un mensaje de error asi: *raise ValidationError('Mensaje de error')*


## Archivo del modelo
```
# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class stock_product(models.Model):
    _name = 'stock_management.stock_product'
    _description = 'stock_management.stock_product'
    _sql_constraints = [
        ('unique_name', 'unique(name)', 'El nombre debe ser unico'),
        ('check_stock', 'CHECK(quantity >= 0)', 'La cantidad debe ser mayor o igual que 0')
    ]

    name = fields.Char()
    category = fields.Selection(
        [
            ('electronica', 'Electronica'),
            ('electrodomestico', 'Electrodomestico'),
            ('mueble', 'Mueble')
        ], required=True
    )
    price = fields.Float()
    quantity = fields.Integer()
    total_value = fields.Integer(compute='_valor_total')
    minimum_quantity = fields.Integer()
    stock_status = fields.Selection(
        [
            ('normal', 'Normal'),
            ('low_stock', 'Low Stock')
        ], compute='_estado_stock'
    )
    full_name = fields.Text(compute='_nombre_completo')

    @api.depends('price', 'quantity')
    def _valor_total(self):
        for record in self:
            record.total_value = record.price * record.quantity

    @api.depends('quantity', 'minimum_quantity')
    def _estado_stock(self):
        for record in self:
            if record.quantity > record.minimum_quantity:
                record.stock_status = 'normal'
            else:
                record.stock_status = 'low_stock'

    @api.depends('name', 'category')
    def _nombre_completo(self):
        for record in self:
            if record.name and record.category:
                record.full_name = f'{str(record.name)} ({record.category})'
            else :
                record.full_name = ''

    @api.constrains('price')
    def _precio_mayor_cero(self):
        for record in self:
            if record.price < 0:
                raise ValidationError('El precio debe ser >= 0')

    @api.constrains('quantity')
    def _cantidad_mayor_cero(self):
        for record in self:
            if record.quantity < 0:
                raise ValidationError('La cantidad debe ser >= 0')

    @api.constrains('price', 'quantity', 'total_value')
    def _valor_total_no_superior(self):
        for record in self:
            if record.total_value > 100000:
                raise ValidationError('El valor total del stock no puede ser superior a 100000 unidades monetarias')

    @api.constrains('category')
    def _check_category(self):
        for record in self:
            if not record.category:
                raise ValidationError('No se permiten productos sin categoría')
```

## Archivo de la vista
```
<odoo>
  <data>
    <!-- explicit list view definition -->

    <record model="ir.ui.view" id="stock_management.list">
      <field name="name">stock_management list</field>
      <field name="model">stock_management.stock_product</field>
      <field name="arch" type="xml">
        <tree>
          <field name="name"/>
          <field name="category"/>
          <field name="price"/>
          <field name="quantity"/>
          <field name="total_value"/>
          <field name="minimum_quantity"/>
          <field name="stock_status"/>
          <field name="full_name"/>
        </tree>
      </field>
    </record>


    <!-- actions opening views on models -->

    <record model="ir.actions.act_window" id="stock_management.action_window">
      <field name="name">stock_management window</field>
      <field name="res_model">stock_management.stock_product</field>
      <field name="view_mode">tree,form</field>
    </record>

    <!-- Top menu item -->

    <menuitem name="stock_management" id="stock_management.menu_root"/>

    <!-- menu categories -->

    <menuitem name="Productos" id="stock_management.menu_1" parent="stock_management.menu_root"/>

    <!-- actions -->

    <menuitem name="Ver Productos" id="stock_management.menu_1_list" parent="stock_management.menu_1"
              action="stock_management.action_window"/>

  </data>
</odoo>
```