# Hermes
# Contributor(s): Aaron Powell (aaron@lunadigital.tv)
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
class OBJECT_OT_select_all_meshes(Operator):
    bl_idname = "hermes.select_all_meshes"
    bl_label = "Mesh"

    @classmethod
    def poll(cls, context):
        return any(obj.type=='MESH' for obj in bpy.data.objects)

    def execute(self, context):
        engine.select_all_by_type('MESH')
        return {'FINISHED'}

class OBJECT_OT_select_all_curves(Operator):
    bl_idname = "hermes.select_all_curves"
    bl_label = "Curve"

    @classmethod
    def poll(cls, context):
        return any(obj.type=='CURVE' for obj in bpy.data.objects)

    def execute(self, context):
        engine.select_all_by_type('CURVE')
        return {'FINISHED'}

class OBJECT_OT_select_all_lamps(Operator):
    bl_idname = "hermes.select_all_lamps"
    bl_label = "Lamp"

    @classmethod
    def poll(cls, context):
        return any(obj.type=='LAMP' for obj in bpy.data.objects)

    def execute(self, context):
        engine.select_all_by_type('LAMP')
        return {'FINISHED'}

class OBJECT_OT_select_all_text(Operator):
    bl_idname = "hermes.select_all_text"
    bl_label = "Text"

    @classmethod
    def poll(cls, context):
        return any(obj.type=='FONT' for obj in bpy.data.objects)

    def execute(self, context):
        engine.select_all_by_type('FONT')
        return {'FINISHED'}

class OBJECT_OT_select_all_armatures(Operator):
    bl_idname = "hermes.select_all_armatures"
    bl_label = "Armature"

    @classmethod
    def poll(cls, context):
        return any(obj.type=='ARMATURE' for obj in bpy.data.objects)

    def execute(self, context):
        engine.select_all_by_type('ARMATURE')
        return {'FINISHED'}

class OBJECT_OT_select_all_lattices(Operator):
    bl_idname = "hermes.select_all_lattices"
    bl_label = "Lattice"

    @classmethod
    def poll(cls, context):
        return any(obj.type=='LATTICE' for obj in bpy.data.objects)

    def execute(self, context):
        engine.select_all_by_type('LATTICE')
        return {'FINISHED'}

class OBJECT_OT_select_all_empties(Operator):
    bl_idname = "hermes.select_all_empties"
    bl_label = "Empty"

    @classmethod
    def poll(cls, context):
        return any(obj.type=='EMPTY' for obj in bpy.data.objects)

    def execute(self, context):
        engine.select_all_by_type('EMPTY')
        return {'FINISHED'}

class OBJECT_OT_select_all_speakers(Operator):
    bl_idname = "hermes.select_all_speakers"
    bl_label = "Speaker"

    @classmethod
    def poll(cls, context):
        return any(obj.type=='SPEAKER' for obj in bpy.data.objects)

    def execute(self, context):
        engine.select_all_by_type('SPEAKER')
        return {'FINISHED'}

class OBJECT_OT_select_all_cameras(Operator):
    bl_idname = "hermes.select_all_cameras"
    bl_label = "Camera"

    @classmethod
    def poll(cls, context):
        return any(obj.type=='CAMERA' for obj in bpy.data.objects)

    def execute(self, context):
        engine.select_all_by_type('CAMERA')
        return {'FINISHED'}

# "Delete All By Type" Operators
class OBJECT_OT_delete_all_meshes(Operator):
    bl_idname = "hermes.delete_all_meshes"
    bl_label = "Mesh"

    @classmethod
    def poll(cls, context):
        return any(obj.type=='MESH' for obj in bpy.data.objects)

    def execute(self, context):
        engine.delete_all_by_type('MESH')
        return {'FINISHED'}

class OBJECT_OT_delete_all_curves(Operator):
    bl_idname = "hermes.delete_all_curves"
    bl_label = "Curve"

    @classmethod
    def poll(cls, context):
        return any(obj.type=='CURVE' for obj in bpy.data.objects)

    def execute(self, context):
        engine.delete_all_by_type('CURVE')
        return {'FINISHED'}

class OBJECT_OT_delete_all_lamps(Operator):
    bl_idname = "hermes.delete_all_lamps"
    bl_label = "Lamp"

    @classmethod
    def poll(cls, context):
        return any(obj.type=='LAMP' for obj in bpy.data.objects)

    def execute(self, context):
        engine.delete_all_by_type('LAMP')
        return {'FINISHED'}

class OBJECT_OT_delete_all_text(Operator):
    bl_idname = "hermes.delete_all_text"
    bl_label = "Text"

    @classmethod
    def poll(cls, context):
        return any(obj.type=='FONT' for obj in bpy.data.objects)

    def execute(self, context):
        engine.delete_all_by_type('FONT')
        return {'FINISHED'}

class OBJECT_OT_delete_all_armatures(Operator):
    bl_idname = "hermes.delete_all_armatures"
    bl_label = "Armature"

    @classmethod
    def poll(cls, context):
        return any(obj.type=='ARMATURE' for obj in bpy.data.objects)

    def execute(self, context):
        engine.delete_all_by_type('ARMATURE')
        return {'FINISHED'}

class OBJECT_OT_delete_all_lattices(Operator):
    bl_idname = "hermes.delete_all_lattices"
    bl_label = "Lattice"

    @classmethod
    def poll(cls, context):
        return any(obj.type=='LATTICE' for obj in bpy.data.objects)

    def execute(self, context):
        engine.delete_all_by_type('LATTICE')
        return {'FINISHED'}

class OBJECT_OT_delete_all_empties(Operator):
    bl_idname = "hermes.delete_all_empties"
    bl_label = "Empty"

    @classmethod
    def poll(cls, context):
        return any(obj.type=='EMPTY' for obj in bpy.data.objects)

    def execute(self, context):
        engine.delete_all_by_type('EMPTY')
        return {'FINISHED'}

class OBJECT_OT_delete_all_speakers(Operator):
    bl_idname = "hermes.delete_all_speakers"
    bl_label = "Speaker"

    @classmethod
    def poll(cls, context):
        return any(obj.type=='SPEAKER' for obj in bpy.data.objects)

    def execute(self, context):
        engine.delete_all_by_type('SPEAKER')
        return {'FINISHED'}

class OBJECT_OT_delete_all_cameras(Operator):
    bl_idname = "hermes.delete_all_cameras"
    bl_label = "Camera"

    @classmethod
    def poll(cls, context):
        return any(obj.type=='CAMERA' for obj in bpy.data.objects)

    def execute(self, context):
        engine.delete_all_by_type('CAMERA')
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
        col.operator('hermes.select_all_armatures', icon='OUTLINER_OB_ARMATURE')
        col.operator('hermes.select_all_lattices', icon='OUTLINER_OB_LATTICE')
        col.operator('hermes.select_all_empties', icon='OUTLINER_OB_EMPTY')
        col.operator('hermes.select_all_speakers', icon='OUTLINER_OB_SPEAKER')
        col.operator('hermes.select_all_cameras', icon='OUTLINER_OB_CAMERA')

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
        col.operator('hermes.delete_all_armatures', icon='OUTLINER_OB_ARMATURE')
        col.operator('hermes.delete_all_lattices', icon='OUTLINER_OB_LATTICE')
        col.operator('hermes.delete_all_empties', icon='OUTLINER_OB_EMPTY')
        col.operator('hermes.delete_all_speakers', icon='OUTLINER_OB_SPEAKER')
        col.operator('hermes.delete_all_cameras', icon='OUTLINER_OB_CAMERA')

def register():
    # Operators: Select All By Type
    bpy.utils.register_class(OBJECT_OT_select_all_meshes)
    bpy.utils.register_class(OBJECT_OT_select_all_curves)
    bpy.utils.register_class(OBJECT_OT_select_all_lamps)
    bpy.utils.register_class(OBJECT_OT_select_all_text)
    bpy.utils.register_class(OBJECT_OT_select_all_armatures)
    bpy.utils.register_class(OBJECT_OT_select_all_lattices)
    bpy.utils.register_class(OBJECT_OT_select_all_empties)
    bpy.utils.register_class(OBJECT_OT_select_all_speakers)
    bpy.utils.register_class(OBJECT_OT_select_all_cameras)
    
    # Operators: Delete All By Type
    bpy.utils.register_class(OBJECT_OT_delete_all_meshes)
    bpy.utils.register_class(OBJECT_OT_delete_all_curves)
    bpy.utils.register_class(OBJECT_OT_delete_all_lamps)
    bpy.utils.register_class(OBJECT_OT_delete_all_text)
    bpy.utils.register_class(OBJECT_OT_delete_all_armatures)
    bpy.utils.register_class(OBJECT_OT_delete_all_lattices)
    bpy.utils.register_class(OBJECT_OT_delete_all_empties)
    bpy.utils.register_class(OBJECT_OT_delete_all_speakers)
    bpy.utils.register_class(OBJECT_OT_delete_all_cameras)

    # Panels
    bpy.utils.register_class(OBJECT_PT_select_all_tools)
    bpy.utils.register_class(OBJECT_PT_delete_all_tools)

def unregister():
    # Operators: Select All By Type
    bpy.utils.unregister_class(OBJECT_OT_select_all_meshes)
    bpy.utils.unregister_class(OBJECT_OT_select_all_curves)
    bpy.utils.unregister_class(OBJECT_OT_select_all_lamps)
    bpy.utils.unregister_class(OBJECT_OT_select_all_text)
    bpy.utils.unregister_class(OBJECT_OT_select_all_armatures)
    bpy.utils.unregister_class(OBJECT_OT_select_all_lattices)
    bpy.utils.unregister_class(OBJECT_OT_select_all_empties)
    bpy.utils.unregister_class(OBJECT_OT_select_all_speakers)
    bpy.utils.unregister_class(OBJECT_OT_select_all_cameras)

    # Operators: Delete All By Type
    bpy.utils.unregister_class(OBJECT_OT_delete_all_meshes)
    bpy.utils.unregister_class(OBJECT_OT_delete_all_curves)
    bpy.utils.unregister_class(OBJECT_OT_delete_all_lamps)
    bpy.utils.unregister_class(OBJECT_OT_delete_all_text)
    bpy.utils.unregister_class(OBJECT_OT_delete_all_armatures)
    bpy.utils.unregister_class(OBJECT_OT_delete_all_lattices)
    bpy.utils.unregister_class(OBJECT_OT_delete_all_empties)
    bpy.utils.unregister_class(OBJECT_OT_delete_all_speakers)
    bpy.utils.unregister_class(OBJECT_OT_delete_all_cameras)
    
    # Panels
    bpy.utils.unregister_class(OBJECT_PT_select_all_tools)
    bpy.utils.unregister_class(OBJECT_PT_delete_all_tools)
