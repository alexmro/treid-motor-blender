from ui.editor import MotorLogicEditor

bl_info = {
    "name": "Build native 3D applications",
    "blender": (4, 0, 0),
    "category": "Engine",
}

logic_editor = MotorLogicEditor()


def register():
    logic_editor.register()


def unregister():
    logic_editor.unregister()


if __name__ == "__main__":
    register()
