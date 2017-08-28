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

class SelectAllEmpties(Operator):
    bl_idname = "hermes.select_all_empties"
    bl_label = "Empty"

    def execute(self, context):
        engine.select_all_by_type('EMPTY')

class SelectAllToolsPanel(Panel):
    bl_label = 'Select All'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = 'Hermes'

    def draw(self, context):
        row = self.layout.row()
        row.operator("hermes.select_all_empties", icon='OUTLINER_OB_EMPTY')

class DeleteAllToolsPanel(Panel):
    bl_label = 'Delete All'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = 'Hermes'

    def draw(self, context):
        row = self.layout.row()
        row.label("Hello")


def register():
    bpy.utils.register_class(SelectAllEmpties)
    bpy.utils.register_class(SelectAllToolsPanel)
    bpy.utils.register_class(DeleteAllToolsPanel)

def unregister():
    bpy.utils.unregister_class(SelectAllEmpties)
    bpy.utils.unregister_class(SelectAllToolsPanel)
    bpy.utils.unregister_class(DeleteAllToolsPanel)
