from bpy.types import Node

from .nodetree import MotorNodeTree


class MotorOnStartNode(Node):
    bl_idname = "MotorOnStartNode"
    bl_label = "On Start"
    bl_icon = "AUTO"
    bl_description = "Entry point, called at the very beginning"
    use_custom_color = True

    @classmethod
    def poll(cls, ntree):
        return ntree.bl_idname == MotorNodeTree.bl_idname

    def init(self, context):
        self.outputs.new("MotorActionSocket", "Action")
