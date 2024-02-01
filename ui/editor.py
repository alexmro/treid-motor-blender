import nodeitems_utils

from bpy.types import NodeTree
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem


class MotorNodeTree(NodeTree):
    bl_idname = 'MotorNodeEditor'
    bl_label = "Logic Node Editor"
    bl_icon = 'NODETREE'


class MotorNodeCategory(NodeCategory):
    @classmethod
    def poll(cls, context):
        return context.space_data.tree_type == 'MotorNodeEditor'


classes = (
    MotorNodeTree,
)


node_categories = [
    MotorNodeCategory('EVENTS_NODES', 'Events', items={
        NodeItem('On Start'),
    })
]


def register():
    for cls in classes:
        register_class(cls)

    nodeitems_utils.register_node_categories('MOTOR_NODES', node_categories)


def unregister():
    nodeitems_utils.unregister_node_categories('MOTOR_NODES')

    for cls in reversed(classes):
        unregister_class(cls)
