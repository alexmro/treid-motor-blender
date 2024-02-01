from ui import editor, gizmo

bl_info = {
    "name": "Build native 3D applications",
    "blender": (4, 0, 0),
    "category": "Engine",
}


def register():
    editor.register()
    gizmo.register()


def unregister():
    editor.unregister()
    gizmo.unregister()


if __name__ == "__main__":
    register()
