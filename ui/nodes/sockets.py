from bpy.types import NodeSocket


class MotorAnySocket(NodeSocket):
    bl_idname = "MotorAnySocket"
    bl_label = "Any Node Socket"

    @classmethod
    def draw_color_simple(cls):
        return 0.6, 0.8, 0.6, 1

    def draw(self, context, layout, node, text):
        if self.is_linked:
            layout.label(text=text)


class MotorActionSocket(NodeSocket):
    bl_idname = "MotorActionSocket"
    bl_label = "Action Node Socket"

    @classmethod
    def draw_color_simple(cls):
        return 1, 1, 1, 1

    def draw(self, context, layout, node, text):
        if self.is_output or self.is_linked:
            layout.label(text=text)
