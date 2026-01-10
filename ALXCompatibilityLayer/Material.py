import bpy

from VersionUtils import get_version


def clear_node_tree(node_tree: bpy.types.NodeTree):
    match get_version():
        case [3, 6]:
            node_tree.inputs.clear()
            node_tree.outputs.clear()
        case _:
            node_tree.interface.clear()


def NG_new_input(node_group, name: str, socket_type: str):
    match get_version():
        case [3, 6]:
            return node_group.inputs.new(socket_type, name)
        case _:
            return node_group.interface.new_socket(
                name, in_out="INPUT", socket_type=socket_type
            )
