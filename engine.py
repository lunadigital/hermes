# #### BEGIN GPL LICENSE BLOCK ####
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
#
# Contributor(s): Aaron Powell (aaron@lunadigital.tv)
#
# #### END GPL LICENSE BLOCK ####

import bpy

# Things to add:
# - Remove all from group

def select_all_by_type(type=None):
    bpy.ops.object.select_all(action='DESELECT')
    for obj in bpy.data.objects:
        if obj.type == type:
            obj.select = True

def delete_all_by_type(type=None):
	select_all_by_type(type=type)
	bpy.ops.object.delete(use_global=False)
		
def add_all_to_group(group_name, prefix=None):
    for obj in bpy.data.objects:
        if prefix is None:
            bpy.context.scene.objects.active = obj
            bpy.ops.object.group_link(group=group_name)
        elif obj.name[:len(prefix)] == prefix:
            bpy.context.scene.objects.active = obj
            bpy.ops.object.group_link(group=group_name)

def dissolve_nth_verts():
    bpy.ops.mesh.select_nth()
    bpy.ops.mesh.dissolve_verts()