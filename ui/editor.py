import nodeitems_utils

from bl_ui import node_add_menu
from bpy.types import Menu
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem

from .nodes.console import MotorConsoleNode
from .nodes.nodetree import MotorNodeTree
from .nodes.onstart import MotorOnStartNode
from .nodes.sockets import MotorActionSocket, MotorAnySocket


class MotorNodeCategory(NodeCategory):
    @classmethod
    def poll(cls, context):
        return context.space_data.tree_type == MotorNodeTree.bl_idname


class MotorApplicationCategory(NodeCategory):
    @classmethod
    def poll(cls, context):
        return context.space_data.tree_type == MotorNodeTree.bl_idname

    @staticmethod
    def draw(_context, layout, _node):
        layout.menu(MotorLogCategoryMenu.bl_idname)


class MotorLogCategoryMenu(Menu):
    bl_idname = "NODE_MT_MotorLogCategoryMenu"
    bl_label = "Log"

    def draw(self, _context):
        layout = self.layout

        node_add_menu.add_node_type(layout, MotorConsoleNode.bl_idname, label=MotorConsoleNode.bl_label, poll=True)
        node_add_menu.draw_assets_for_catalog(layout, self.bl_label)


node_categories = [
    MotorNodeCategory(
        "APPLICATION_NODES", "Application", items={
            MotorApplicationCategory('LOG', 'Log')
        }
    ),
    MotorNodeCategory(
        "EVENTS_NODES", "Events", description="User, application and system events", items={
            NodeItem(MotorOnStartNode.bl_idname),
        }
    )
]

classes = (
    MotorNodeTree,
    MotorLogCategoryMenu,
    MotorActionSocket,
    MotorAnySocket,
    MotorOnStartNode,
    MotorConsoleNode,
)


def register():
    for cls in classes:
        register_class(cls)

    nodeitems_utils.register_node_categories('MOTOR_NODES', node_categories)


def unregister():
    nodeitems_utils.unregister_node_categories('MOTOR_NODES')

    for cls in reversed(classes):
        unregister_class(cls)
