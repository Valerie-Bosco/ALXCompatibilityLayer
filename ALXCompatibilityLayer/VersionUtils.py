import bpy


def get_version():
    return bpy.app.version[0:2]

def is_version(major:int, minor:int):
    return bpy.app.version[0:2] == [major, minor]
