from enum import Enum

import bpy

from .VersionUtils import get_version


class NodeGroupInput_Subtype(Enum):
    @property
    def Factor(self):
        return "Factor" if get_version() == [3, 6] else "FACTOR"


class PrincipledBSDF:
    class Inputs(Enum):
        @property
        def Emission(self):
            return "Emission" if get_version() == [3, 6] else "Emission Color"


def NT_clear_node_tree(node_tree: bpy.types.NodeTree):
    match get_version():
        case [3, 6]:
            node_tree.inputs.clear()
            node_tree.outputs.clear()
        case _:
            node_tree.interface.clear()


def NG_IO_new_input(node_group, name: str, socket_type: str):
    match get_version():
        case [3, 6]:
            return node_group.inputs.new(socket_type, name)
        case _:
            return node_group.interface.new_socket(
                name, in_out="INPUT", socket_type=socket_type
            )


def NG_IO_new_output(node_group, name: str, socket_type: str):
    match get_version():
        case [3, 6]:
            return node_group.outputs.new(socket_type, name)
        case _:
            return node_group.interface.new_socket(
                name, in_out="OUTPUT", socket_type=socket_type
            )


def NG_IO_set_subtype(nodegroup_socket, subtype: property):
    """subtype: class<NodeGroupInput_Subtype>"""
    match get_version():
        case [3, 6]:
            nodegroup_socket.bl_subtype_label = str(subtype.value)
        case _:
            nodegroup_socket.subtype = str(subtype.value)
