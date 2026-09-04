import bpy

from .VersionUtils import is_version, lessthanequal_version


class NodeGroupInput_Subtype:
    Factor = "Factor" if is_version(3, 6) else "FACTOR"


class PrincipledBSDF:
    class Inputs:
        Emission = "Emission" if is_version(3, 6) else "Emission Color"


def NT_clear_node_tree(node_tree: bpy.types.NodeTree) -> None:
    if node_tree is not None:
        if lessthanequal_version((3, 6)):
            if (__inputs := node_tree.inputs) is not None:
                __inputs.clear()
            if (__outputs := node_tree.outputs) is not None:
                __outputs.clear()
        else:
            if (__nodes := node_tree.nodes) is not None:
                __nodes.clear()


def NG_IO_new_input(_node_tree, name: str, _socket_type: str):
    if lessthanequal_version((3, 6)):
        return _node_tree.inputs.new(_socket_type, name)
    else:
        return _node_tree.interface.new_socket(
            name, in_out="INPUT", socket_type=_socket_type
        )


def NG_IO_new_output(node_group, name: str, socket_type: str):
    if lessthanequal_version((3, 6)):
        return node_group.outputs.new(socket_type, name)
    else:
        return node_group.interface.new_socket(
            name, in_out="OUTPUT", socket_type=socket_type
        )


def NG_IO_set_subtype(nodegroup_socket, subtype: property):
    """subtype: class<NodeGroupInput_Subtype>"""
    if lessthanequal_version((3, 6)):
        if (socket := nodegroup_socket) is not None:
            socket.bl_subtype_label = subtype
        else:
            nodegroup_socket.subtype = subtype
