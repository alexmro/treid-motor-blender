import bpy

from bpy.types import Operator
from bpy.utils import register_classes_factory


def switch_interactive_mode(enabled):
    area = bpy.context.area
    window = bpy.context.window
    if area.type == 'VIEW_3D':
        if enabled:
            area.header_text_set("Press ESC to exit")
        else:
            area.header_text_set(None)

        area.spaces[0].overlay.show_axis_x = not enabled
        area.spaces[0].overlay.show_axis_y = not enabled
        area.spaces[0].overlay.show_cursor = not enabled
        area.spaces[0].overlay.show_fade_inactive = not enabled
        area.spaces[0].overlay.show_floor = not enabled
        area.spaces[0].overlay.show_freestyle_edge_marks = not enabled
        area.spaces[0].overlay.show_look_dev = not enabled
        area.spaces[0].overlay.show_object_origins = not enabled
        area.spaces[0].overlay.show_outline_selected = not enabled
        area.spaces[0].overlay.show_overlays = not enabled
        area.spaces[0].overlay.show_viewer_attribute = not enabled
        area.spaces[0].show_gizmo = not enabled
        area.spaces[0].show_region_toolbar = not enabled
        area.spaces[0].region_3d.view_perspective = 'CAMERA'

        for region in area.regions:
            if region.type == 'WINDOW':
                cx = region.width // 2
                cy = region.height // 2

                window.cursor_warp(region.x + cx, region.y + cy)

        with bpy.context.temp_override(window=window, area=area, region=None):
            if enabled:
                window.cursor_set("NONE")
            else:
                window.cursor_set("DEFAULT")

    if enabled:
        bpy.ops.view3d.view_center_camera()
    else:
        bpy.ops.view3d.view_lock_clear()


class MotorRunOperator(Operator):
    bl_idname = "motor.run"
    bl_label = "Enter interactive mode"
    bl_description = "Enter interactive mode and disable UI"

    def modal(self, context, event):
        if event.type in {'ESC'}:
            switch_interactive_mode(False)
            return {'CANCELLED'}

        return {'RUNNING_MODAL'}

    def invoke(self, context, event):
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}


classes = (
    MotorRunOperator,
)

register, unregister = register_classes_factory(classes)
