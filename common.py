from bpy import context
from bpy import data
from bpy import ops

# remove all from group

def select_all_by_type(type=None):
	for obj in data.objects:
		if obj.type == type:
			obj.select = True

def remove_all_by_type(type=None):
	select_all_by_type(type=type)
	ops.object.delete(use_global=False)
		
def add_all_to_group(group_name, prefix=None):
    for obj in data.objects:
        if prefix is None:
            context.scene.objects.active = obj
            ops.object.group_link(group=group_name)
        elif obj.name[:len(prefix)] == prefix:
            context.scene.objects.active = obj
            ops.object.group_link(group=group_name)