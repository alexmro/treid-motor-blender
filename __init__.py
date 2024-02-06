import bpy

from .ui import view
from .ui import editor, gizmo
from .utils import handlers

bl_info = {
    "name": "Build native 3D applications",
    "blender": (4, 0, 0),
    "category": "Engine",
}

addon_keymaps = []


def register():
    """Entry point, where everything is registered and prepared"""
    handlers.register()

    view.register()
    editor.register()
    gizmo.register()

    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(name='Window', region_type='WINDOW', space_type='EMPTY')
        kmi = km.keymap_items.new(gizmo.MotorGizmoOperator.bl_idname, type='P', value='PRESS')
        addon_keymaps.append((km, kmi))


def unregister():
    """Everything registered at the beginning is unregistered here in the inverse order"""
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

    gizmo.unregister()
    editor.unregister()
    view.unregister()

    handlers.unregister()


if __name__ == "__main__":
    register()
