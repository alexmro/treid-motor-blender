import bpy

bl_info = {
    "name": "Build native 3D applications",
    "blender": (4, 0, 0),
    "category": "Engine",
}


def register():
    print("Registered")


def unregister():
    print("Unregistered")


if __name__ == "__main__":
    register()
