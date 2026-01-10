import bpy

from VersionUtils import get_version


def clear_node_tree(node_tree:bpy.types.NodeTree):
    match get_version():
        case [3, 6]:
            node_tree.inputs.clear()
            node_tree.outputs.clear()
        case _:
            node_tree.interface.clear()