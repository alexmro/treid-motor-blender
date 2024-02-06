import bpy

from bpy.app.handlers import persistent

from ..ui.editor import MotorNodeTree


@persistent
def on_depsgraph_update_post(self):
    last_operator = getattr(bpy.context, 'active_operator', None)
    if last_operator is not None:
        on_operator_post(last_operator.bl_idname)


def on_operator_post(operator_id: str) -> None:
    if operator_id == "NODE_OT_new_node_tree":
        if bpy.context.space_data.tree_type == MotorNodeTree.bl_idname:
            bpy.context.space_data.edit_tree.name = "Logic Tree"


def register():
    bpy.app.handlers.depsgraph_update_post.append(on_depsgraph_update_post)


def unregister():
    bpy.app.handlers.depsgraph_update_post.remove(on_depsgraph_update_post)
