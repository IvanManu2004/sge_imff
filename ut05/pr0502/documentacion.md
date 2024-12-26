## [Unidad 5](../index.md)
# Practica 2


Para poder crear un modulo con 2 modelos, debemos crear 2 archivos de modelos en la carpeta 'models' que sean '.py' para manejarlos en python, y para las vistas hemos creado 3 archivos 2 de ellos son para cada modelo y el tercero lleva todo lo relacionado con los menus. Por ultimo debemos añadir una nueva linea en el archivo de configuracion de seguridad, debe haber 1 linea por cada modelo:


## Modelo Gestion_autor.py
```
# -*- coding: utf-8 -*-

from odoo import models, fields, api    #type:  ignore


class gestion_autor(models.Model):
    _name = 'gestion_libreria.gestion_autor'
    _description = 'gestion_libreria.gestion_autor'

    nombre = fields.Char()
    fecha_de_nacimiento = fields.Date()
    biografia = fields.Text()
    libros = fields.Text()

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

```

## Modelo Gestion_libro.py
```
# -*- coding: utf-8 -*-

from odoo import models, fields, api    #type:  ignore


class gestion_libro(models.Model):
    _name = 'gestion_libreria.gestion_libro'
    _description = 'gestion_libreria.gestion_libro'

    nombre = fields.Char()
    autor = fields.Char()
    fecha_de_publicacion = fields.Date()
    isbn = fields.Integer()
    sinopsis = fields.Text()

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

```

## Vista gestion_autor_views.xml
```
<odoo>
  <data>
    <record model="ir.ui.view" id="gestion_libreria.gestion_autor_list">
      <field name="name">gestion_libreria.autor.list</field>
      <field name="model">gestion_libreria.gestion_autor</field>
      <field name="arch" type="xml">
        <tree>
          <field name="nombre"/>
          <field name="fecha_de_nacimiento"/>
          <field name="biografia"/>
          <field name="libros"/>
        </tree>
      </field>
    </record>

    <!-- actions opening views on models -->

    <record model="ir.actions.act_window" id="gestion_libreria.autor_action">
      <field name="name">gestion_libreria_autor window</field>
      <field name="res_model">gestion_libreria.gestion_autor</field>
      <field name="view_mode">tree,form</field>
    </record>
  </data>
</odoo>
```

## Vista gestion_libro_views.xml
```
<odoo>
  <data>
    <record model="ir.ui.view" id="gestion_libreria.gestion_libro_list">
      <field name="name">gestion_libreria.libro.list</field>
      <field name="model">gestion_libreria.gestion_libro</field>
      <field name="arch" type="xml">
        <tree>
          <field name="nombre"/>
          <field name="autor"/>
          <field name="fecha_de_publicacion"/>
          <field name="isbn"/>
          <field name="sinopsis"/>
        </tree>
      </field>
    </record>

    <!-- actions opening views on models -->

    <record model="ir.actions.act_window" id="gestion_libreria.libro_action">
      <field name="name">gestion_libreria_libro window</field>
      <field name="res_model">gestion_libreria.gestion_libro</field>
      <field name="view_mode">tree,form</field>
    </record>
  </data>
</odoo>
```

## Vista gestion_menu_views.xml
```
<odoo>
  <data>
    <!-- Top menu item -->

    <menuitem name="gestion_libreria" id="gestion_libreria.menu_root"/>

    <!-- menu categories -->

    <menuitem name="Libros" id="gestion_libreria.libros" parent="gestion_libreria.menu_root"/>
    <menuitem name="Autores" id="gestion_libreria.autores" parent="gestion_libreria.menu_root"/>

    <!-- actions -->

    <menuitem name="Libro" id="gestion_libreria.menu_libros" parent="gestion_libreria.libros"
              action="gestion_libreria.libro_action"/>
    <menuitem name="Autor" id="gestion_libreria.menu_autores" parent="gestion_libreria.autores"
              action="gestion_libreria.autor_action"/>

  </data>
</odoo>
```

## Archivo de configuracion de seguridad
```
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_gestion_libreria_gestion_libro,gestion_libreria.gestion_libro,model_gestion_libreria_gestion_libro,base.group_user,1,1,1,1
access_gestion_libreria_gestion_autor,gestion_libreria.gestion_autor,model_gestion_libreria_gestion_autor,base.group_user,1,1,1,1
```