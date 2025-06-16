bl_info = {
    "name": "Inflatable Sewing System",
    "author": "Codex",
    "version": (1, 0, 0),
    "blender": (4, 0, 0),
    "location": "View3D > Sidebar > Inflatable",
    "description": "Tools for generating and exporting inflatable sewing patterns",
    "category": "Mesh",
}

import importlib
from . import panel_ui, pattern_generator, cloth_simulation
from . import dxf_svg_export, jpg_preview_export
from . import json_csv_export, plt_export_operator

modules = [
    panel_ui,
    pattern_generator,
    cloth_simulation,
    dxf_svg_export,
    jpg_preview_export,
    json_csv_export,
    plt_export_operator,
]


def register():
    for module in modules:
        importlib.reload(module)
        if hasattr(module, "register"):
            module.register()


def unregister():
    for module in modules:
        if hasattr(module, "unregister"):
            module.unregister()

if __name__ == "__main__":
    register()
