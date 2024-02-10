from bpy.types import NodeTree


class MotorNodeTree(NodeTree):
    bl_idname = "MotorNodeTree"
    bl_label = "Logic Node Editor"
    bl_icon = "NODETREE"
    bl_description = "Motor logic nodes"
