import bpy
from bpy.props import (
    FloatProperty,
    BoolProperty,
    FloatVectorProperty,
    EnumProperty,
)

from . import pattern_generator, cloth_simulation
from . import dxf_svg_export, jpg_preview_export
from . import json_csv_export, plt_export_operator


class InflatableProperties(bpy.types.PropertyGroup):
    stitch_spacing: FloatProperty(
        name="Stitch Spacing (mm)",
        default=5.0,
        min=0.1,
    )
    seam_allowance: FloatProperty(
        name="Seam Allowance (mm)",
        default=10.0,
        min=0.0,
    )
    font_size: FloatProperty(
        name="Font Size",
        default=12.0,
        min=1.0,
    )
    font_thickness: FloatProperty(
        name="Font Thickness",
        default=1.0,
        min=0.1,
    )
    label_bg: FloatVectorProperty(
        name="Label BG",
        subtype='COLOR',
        size=3,
        min=0.0,
        max=1.0,
        default=(1.0, 1.0, 1.0),
    )
    export_format: EnumProperty(
        name="Format",
        items=[
            ('SVG', 'SVG', ''),
            ('DXF', 'DXF', ''),
            ('JPG', 'JPG', ''),
            ('PLT', 'PLT', ''),
        ],
        default='SVG'
    )
    show_seams: BoolProperty(name="Show Seams", default=True)
    show_labels: BoolProperty(name="Show Labels", default=True)
    show_cut: BoolProperty(name="Show Cut Lines", default=True)
    manual_symmetry: BoolProperty(name="Manual Symmetry", default=False)


class INFLATABLE_PT_main(bpy.types.Panel):
    bl_label = "Inflatable Sewing"
    bl_idname = "INFLATABLE_PT_main"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Inflatable'

    def draw(self, context):
        layout = self.layout
        props = context.scene.inflatable_props

        layout.operator(pattern_generator.GeneratePatternOperator.bl_idname)
        layout.operator(dxf_svg_export.ExportPatternOperator.bl_idname)
        layout.operator(cloth_simulation.RunClothSimOperator.bl_idname)

        layout.separator()
        layout.prop(props, "stitch_spacing")
        layout.prop(props, "seam_allowance")
        layout.prop(props, "font_size")
        layout.prop(props, "font_thickness")
        layout.prop(props, "label_bg")
        layout.prop(props, "export_format")
        layout.prop(props, "show_seams")
        layout.prop(props, "show_labels")
        layout.prop(props, "show_cut")
        layout.prop(props, "manual_symmetry")


def register():
    bpy.utils.register_class(InflatableProperties)
    bpy.types.Scene.inflatable_props = bpy.props.PointerProperty(type=InflatableProperties)
    bpy.utils.register_class(INFLATABLE_PT_main)

    pattern_generator.register()
    cloth_simulation.register()
    dxf_svg_export.register()
    jpg_preview_export.register()
    json_csv_export.register()
    plt_export_operator.register()


def unregister():
    plt_export_operator.unregister()
    json_csv_export.unregister()
    jpg_preview_export.unregister()
    dxf_svg_export.unregister()
    cloth_simulation.unregister()
    pattern_generator.unregister()
    bpy.utils.unregister_class(INFLATABLE_PT_main)
    del bpy.types.Scene.inflatable_props
    bpy.utils.unregister_class(InflatableProperties)
