import nodeitems_utils
from bpy.types import NodeTree, Node, NodeSocket, NodeTreeInterfaceSocket
from bpy.utils import register_class, unregister_class


class MotorLogicTree(NodeTree):
    bl_idname = 'LogicNodeEditor'
    bl_label = "Logic Node Editor"
    bl_icon = 'NODETREE'


class MotorLogicEditor:
    classes = (
        MotorLogicTree,
    )

    def register(self):
        for cls in self.classes:
            register_class(cls)

    def unregister(self):
        nodeitems_utils.unregister_node_categories('CUSTOM_NODES')

        for cls in reversed(self.classes):
            unregister_class(cls)
