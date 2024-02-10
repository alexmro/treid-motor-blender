import bpy

from bpy.types import Node

from .nodetree import MotorNodeTree


class MotorConsoleNode(Node):
    bl_idname = "MotorConsoleNode"
    bl_label = "Console"
    bl_icon = "CONSOLE"
    bl_description = "Output data or text to the console window"
    use_custom_color = True

    type_items = [
        ("INFO", "Info", "", 1),
        ("WARNING", "Warning", "", 2),
        ("ERROR", "Error", "", 3),
    ]

    show_time_prop: bpy.props.BoolProperty()
    type_prop: bpy.props.EnumProperty(items=type_items)

    @classmethod
    def poll(cls, ntree):
        return ntree.bl_idname == MotorNodeTree.bl_idname

    def init(self, context):
        self.inputs.new("MotorAnySocket", "Anything")

    def draw_buttons(self, context, layout):
        layout.prop(self, "show_time_prop", text="Show date and time")
        layout.prop(self, "type_prop", text="Type")

    def draw_buttons_ext(self, context, layout):
        layout.prop(self, "show_time_prop", text="Show date and time")
        layout.prop(self, "type_prop", text="Type")
