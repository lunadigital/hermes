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

bl_info = {
        "name": "Hermes",
        "description": "A collection of common functions used at Luna Digital.",
        "author": "Aaron Powell",
        "version": (0, 1, 0),
        "blender": (2, 78, 0),
        "location": "Properties > 3D View > Toolbar",
        "warning": "", # used for warning icon and text in add-ons panel
        "wiki_url": "http://my.wiki.url",
        "tracker_url": "http://my.bugtracker.url",
        "support": "COMMUNITY",
        "category": "3D View"
        }

import bpy

def register():
    from . import properties
    from . import ui
    properties.register()
    ui.register()

def unregister():
    from . import properties
    from . import ui
    properties.unregister()
    ui.unregister()

if __name__ == '__main__':
    register()
