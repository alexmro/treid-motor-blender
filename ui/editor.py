import nodeitems_utils

from bpy.types import NodeTree, Node, NodeSocket, NodeTreeInterfaceSocket
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem


class MotorNodesTree(NodeTree):
    bl_idname = 'MotorNodeEditor'
    bl_label = "Logic Node Editor"
    bl_icon = 'NODETREE'


class MotorNodeCategory(NodeCategory):
    @classmethod
    def poll(cls, context):
        return context.space_data.tree_type == 'MotorNodeEditor'


class MotorLogicEditor:
    classes = (
        MotorNodesTree,
    )

    # all categories in a list
    node_categories = [
        MotorNodeCategory('EVENTS_NODES', 'Events', items = {
            NodeItem('On Start'),
        })
    ]

    def register(self):
        for cls in self.classes:
            register_class(cls)

        nodeitems_utils.register_node_categories('MOTOR_NODES', self.node_categories)

    def unregister(self):
        nodeitems_utils.unregister_node_categories('MOTOR_NODES')

        for cls in reversed(self.classes):
            unregister_class(cls)
