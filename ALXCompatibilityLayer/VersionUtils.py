import bpy


def get_version() -> tuple:
    return bpy.app.version[0:2]


def is_version(major: int, minor: int) -> bool:
    return get_version() == (major, minor)
