## [Unidad 6](../index.md)
# Practica 1
## Documento Views.xml
```
<odoo>
  <data>
    <!-- explicit list view definition -->

    <record model="ir.ui.view" id="gestion_productos.list">
      <field name="name">gestion_productos list</field>
      <field name="model">gestion_productos.gestion_productos</field>
      <field name="arch" type="xml">
        <tree>
          <field name="nombre"/>
          <field name="descripcion"/>
          <field name="codigo"/>
          <field name="imagen"/>
          <field name="categoria"/>
          <field name="tipo"/>
          <field name="precio"/>
          <field name="stock"/>
          <field name="fecha_creacion"/>
          <field name="fecha_ultima_actualizacion"/>
          <field name="activo"/>
          <field name="peso"/>
        </tree>
      </field>
    </record>


    <!-- actions opening views on models -->

    <record model="ir.actions.act_window" id="gestion_productos.action_window">
      <field name="name">gestion_productos window</field>
      <field name="res_model">gestion_productos.gestion_productos</field>
      <field name="view_mode">tree,form</field>
    </record>

    <!-- Top menu item -->

    <menuitem name="gestion_productos" id="gestion_productos.menu_root"/>

    <!-- menu categories -->

    <menuitem name="Menu 1" id="gestion_productos.menu_1" parent="gestion_productos.menu_root"/>
    <menuitem name="Menu 2" id="gestion_productos.menu_2" parent="gestion_productos.menu_root"/>

    <!-- actions -->

    <menuitem name="List" id="gestion_productos.menu_1_list" parent="gestion_productos.menu_1"
              action="gestion_productos.action_window"/>
    <menuitem name="Server to list" id="gestion_productos" parent="gestion_productos.menu_2"
              action="gestion_productos.action_window"/>

  </data>
</odoo>
```

## Documento models.py
```
# -*- coding: utf-8 -*-

from odoo import models, fields, api    #type:  ignore


class gestion_productos(models.Model):
    _name = 'gestion_productos.gestion_productos'
    _description = 'gestion_productos.gestion_productos'

    nombre = fields.Char()
    descripcion = fields.Text()
    codigo = fields.Integer(required=True)
    imagen = fields.Image()
    categoria = fields.Selection(
        [
            ('jardin', 'Jardin'),
            ('hogar', 'Hogar'),
            ('electrodomestico', 'Electrodomestico')
        ]
        )
    tipo = fields.Boolean(string="Destacable", help="Indica si es un producto destacable o no")
    precio = fields.Integer()
    stock = fields.Integer(help="Cantidad de unidades disponible")
    fecha_creacion = fields.Date(default=fields.Date.today)
    fecha_ultima_actualizacion = fields.Date()
    activo = fields.Boolean(default=True, help="Indica si el producto está disponible o no")
    peso = fields.Float(help="Un valor numérico con dos decimales de precisión")

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100

```

## Documento ir.model.access.csv
```
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_gestion_productos_gestion_productos,gestion_productos.gestion_productos,model_gestion_productos_gestion_productos,base.group_user,1,1,1,1
```

## Documento __manifest__.py
```
# -*- coding: utf-8 -*-
{
    'name': "gestion_productos",

    'summary': """
        Modulo que permite almacenar y gestionar productos
        """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Ivan",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
```