# Blender Add-on Template
# Contributor(s): Aaron Powell (aaron@aaronpowell.me)
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import bpy
from bpy.types import Panel, Operator

from . import engine

# "Select All By Type" Operators
# TODO:
# - Armature
# - Lattice
# - Empty
# - Speaker
# - Camera
class OBJECT_OT_select_all_meshes(Operator):
    bl_idname = "hermes.select_all_meshes"
    bl_label = "Mesh"

    def execute(self, context):
        engine.select_all_by_type('MESH')
        return {'FINISHED'}

class OBJECT_OT_select_all_curves(Operator):
    bl_idname = "hermes.select_all_curves"
    bl_label = "Curve"

    def execute(self, context):
        engine.select_all_by_type('CURVE')
        return {'FINISHED'}

class OBJECT_OT_select_all_lamps(Operator):
    bl_idname = "hermes.select_all_lamps"
    bl_label = "Lamp"

    def execute(self, context):
        engine.select_all_by_type('LAMP')
        return {'FINISHED'}

class OBJECT_OT_select_all_text(Operator):
    bl_idname = "hermes.select_all_text"
    bl_label = "Text"

    def execute(self, context):
        engine.select_all_by_type('FONT')
        return {'FINISHED'}

class OBJECT_OT_select_all_empties(Operator):
    bl_idname = "hermes.select_all_empties"
    bl_label = "Empty"

    def execute(self, context):
        engine.select_all_by_type('EMPTY')
        return {'FINISHED'}

# "Delete All By Type" Operators
# TODO:
# - Armature
# - Lattice
# - Empty
# - Speaker
# - Camera
class OBJECT_OT_delete_all_meshes(Operator):
    bl_idname = "hermes.delete_all_meshes"
    bl_label = "Mesh"

    def execute(self, context):
        engine.delete_all_by_type('MESH')
        return {'FINISHED'}

class OBJECT_OT_delete_all_curves(Operator):
    bl_idname = "hermes.delete_all_curves"
    bl_label = "Curve"

    def execute(self, context):
        engine.delete_all_by_type('CURVE')
        return {'FINISHED'}

class OBJECT_OT_delete_all_lamps(Operator):
    bl_idname = "hermes.delete_all_lamps"
    bl_label = "Lamp"

    def execute(self, context):
        engine.delete_all_by_type('LAMP')
        return {'FINISHED'}

class OBJECT_OT_delete_all_text(Operator):
    bl_idname = "hermes.delete_all_text"
    bl_label = "Text"

    def execute(self, context):
        engine.delete_all_by_type('FONT')
        return {'FINISHED'}

class OBJECT_OT_delete_all_empties(Operator):
    bl_idname = "hermes.delete_all_empties"
    bl_label = "Empty"

    def execute(self, context):
        engine.delete_all_by_type('EMPTY')
        return {'FINISHED'}

# Panels
class OBJECT_PT_select_all_tools(Panel):
    bl_label = 'Select All By Type'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = 'Hermes'

    def draw(self, context):
        col = self.layout.column(align=True)
        col.operator('hermes.select_all_meshes', icon='OUTLINER_OB_MESH')
        col.operator('hermes.select_all_curves', icon='OUTLINER_OB_CURVE')
        col.operator('hermes.select_all_lamps', icon='OUTLINER_OB_LAMP')
        col.operator('hermes.select_all_text', icon='OUTLINER_OB_FONT')

        col.operator('hermes.select_all_empties', icon='OUTLINER_OB_EMPTY')

class OBJECT_PT_delete_all_tools(Panel):
    bl_label = 'Delete All By Type'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = 'Hermes'

    def draw(self, context):
        col = self.layout.column(align=True)
        col.operator('hermes.delete_all_meshes', icon='OUTLINER_OB_MESH')
        col.operator('hermes.delete_all_curves', icon='OUTLINER_OB_CURVE')
        col.operator('hermes.delete_all_lamps', icon='OUTLINER_OB_LAMP')
        col.operator('hermes.delete_all_text', icon='OUTLINER_OB_FONT')

        col.operator('hermes.delete_all_empties', icon='OUTLINER_OB_EMPTY')


def register():
    # Operators: Select All By Type
    bpy.utils.register_class(OBJECT_OT_select_all_meshes)
    bpy.utils.register_class(OBJECT_OT_select_all_curves)
    bpy.utils.register_class(OBJECT_OT_select_all_lamps)
    bpy.utils.register_class(OBJECT_OT_select_all_text)
    bpy.utils.register_class(OBJECT_OT_select_all_empties)
    
    # Operators: Delete All By Type
    bpy.utils.register_class(OBJECT_OT_delete_all_meshes)
    bpy.utils.register_class(OBJECT_OT_delete_all_curves)
    bpy.utils.register_class(OBJECT_OT_delete_all_lamps)
    bpy.utils.register_class(OBJECT_OT_delete_all_text)
    bpy.utils.register_class(OBJECT_OT_delete_all_empties)

    # Panels
    bpy.utils.register_class(OBJECT_PT_select_all_tools)
    bpy.utils.register_class(OBJECT_PT_delete_all_tools)

def unregister():
    # Operators: Select All By Type
    bpy.utils.unregister_class(OBJECT_OT_select_all_meshes)
    bpy.utils.unregister_class(OBJECT_OT_select_all_curves)
    bpy.utils.unregister_class(OBJECT_OT_select_all_lamps)
    bpy.utils.unregister_class(OBJECT_OT_select_all_text)
    bpy.utils.unregister_class(OBJECT_OT_select_all_empties)

    # Operators: Delete All By Type
    bpy.utils.unregister_class(OBJECT_OT_delete_all_meshes)
    bpy.utils.unregister_class(OBJECT_OT_delete_all_curves)
    bpy.utils.unregister_class(OBJECT_OT_delete_all_lamps)
    bpy.utils.unregister_class(OBJECT_OT_delete_all_text)
    bpy.utils.unregister_class(OBJECT_OT_delete_all_empties)
    
    # Panels
    bpy.utils.unregister_class(OBJECT_PT_select_all_tools)
    bpy.utils.unregister_class(OBJECT_PT_delete_all_tools)
