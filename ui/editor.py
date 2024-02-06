import nodeitems_utils

from bpy.types import NodeTree, NodeSocket, Node
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem


class MotorNodeTree(NodeTree):
    bl_idname = 'MotorNodeTree'
    bl_label = "Logic Node Editor"
    bl_icon = 'NODETREE'
    bl_description = "Motor logic nodes"


class MotorActionSocket(NodeSocket):
    bl_idname = 'MotorActionSocket'
    bl_label = "Action Node Socket"

    @classmethod
    def draw_color_simple(cls):
        return 1, 1, 1, 1

    def draw(self, context, layout, node, text):
        if self.is_output or self.is_linked:
            layout.label(text=text)


class MotorOnStartNode(Node):
    bl_idname = 'MotorOnStartNode'
    bl_label = "On Start"
    bl_icon = 'AUTO'
    use_custom_color = True

    @classmethod
    def poll(cls, ntree):
        return ntree.bl_idname == MotorNodeTree.bl_idname

    def init(self, context):
        self.outputs.new('MotorActionSocket', "Action")


class MotorNodeCategory(NodeCategory):
    @classmethod
    def poll(cls, context):
        return context.space_data.tree_type == MotorNodeTree.bl_idname


node_categories = [
    MotorNodeCategory('EVENTS_NODES', 'Events', items={
        NodeItem('MotorOnStartNode'),
    })
]


classes = (
    MotorNodeTree,
    MotorActionSocket,
    MotorOnStartNode
)


def register():
    for cls in classes:
        register_class(cls)

    nodeitems_utils.register_node_categories('MOTOR_NODES', node_categories)


def unregister():
    nodeitems_utils.unregister_node_categories('MOTOR_NODES')

    for cls in reversed(classes):
        unregister_class(cls)
