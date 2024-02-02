import bpy

from .ui import editor, gizmo

bl_info = {
    "name": "Build native 3D applications",
    "blender": (4, 0, 0),
    "category": "Engine",
}

addon_keymaps = []


def register():
    editor.register()
    gizmo.register()

    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(name='Window', region_type='WINDOW', space_type='EMPTY')
        kmi = km.keymap_items.new(gizmo.MotorOperator.bl_idname, type='P', value='PRESS')
        addon_keymaps.append((km, kmi))


def unregister():
    editor.unregister()
    gizmo.unregister()

    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()


if __name__ == "__main__":
    register()
