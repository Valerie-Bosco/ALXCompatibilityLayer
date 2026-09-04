import bpy


def get_version() -> tuple:
    return bpy.app.version[0:2]


def is_version(major: int, minor: int) -> bool:
    return get_version() == (major, minor)


def lessthan_version(version: tuple[int, int]) -> bool:
    bl_version = get_version()

    return (bl_version[0] == version[0] and bl_version[1] < version[1]) or (
            bl_version[0] < version[0]
    )


def lessthanequal_version(version: tuple[int, int]) -> bool:
    bl_version = get_version()

    return (bl_version[0] == version[0] and bl_version[1] <= version[1]) or (
            bl_version[0] <= version[0]
    )
