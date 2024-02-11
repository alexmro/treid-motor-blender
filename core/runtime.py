import bpy

from datetime import datetime

from ..ui.nodes.nodetree import MotorNodeTree
from ..ui.nodes.onstart import MotorOnStartNode
from ..ui.nodes.console import MotorConsoleNode
from ..ui.nodes.sockets import MotorActionSocket


def run_scene():
    """Interpret the entire node tree and run the scene"""
    on_start_nodes = []

    for node_group in bpy.data.node_groups:
        if node_group.bl_idname == MotorNodeTree.bl_idname:
            for node in node_group.nodes:
                if node.bl_idname == MotorOnStartNode.bl_idname:
                    on_start_nodes.append(node)

    for start_node in on_start_nodes:
        for output in start_node.outputs:
            if output.enabled and output.is_output and output.is_linked:
                for link in output.links:
                    if link.to_node.bl_idname == MotorConsoleNode.bl_idname:
                        to_node = link.to_node
                        message = ""
                        if output.bl_idname == MotorActionSocket.bl_idname:
                            message = f"'{start_node.bl_label}' output '{output.bl_label}'"
                        show_time_prop = to_node.get("show_time_prop")
                        type_prop = to_node.get("type_prop")

                        if type_prop == 3:
                            message = "ERROR: " + message
                        elif type_prop == 2:
                            message = "WARNING: " + message
                        else:
                            message = "INFO: " + message

                        if show_time_prop:
                            now = datetime.now()
                            dt_string = now.strftime("[%d/%m/%Y %H:%M:%S] ")

                            message = dt_string + message

                        print(message)

    return True


def stop_scene():
    print("Scene stopped")
