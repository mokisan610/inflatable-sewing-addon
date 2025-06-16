import bpy
import os

class ExportPatternOperator(bpy.types.Operator):
    bl_idname = "inflatable.export_pattern"
    bl_label = "Export Pattern"

    def execute(self, context):
        props = context.scene.inflatable_props
        obj = context.active_object
        if not obj or obj.type != 'MESH':
            self.report({'ERROR'}, 'Active object must be a mesh')
            return {'CANCELLED'}

        filepath = bpy.path.abspath("//pattern")
        if props.export_format == 'SVG':
            filepath += '.svg'
            export_svg(obj, filepath)
        elif props.export_format == 'DXF':
            filepath += '.dxf'
            export_dxf(obj, filepath)
        elif props.export_format == 'JPG':
            from .jpg_preview_export import export_jpg
            filepath += '.jpg'
            export_jpg(obj, filepath)
        elif props.export_format == 'PLT':
            from .plt_export_operator import export_plt
            filepath += '.plt'
            export_plt(obj, filepath)
        self.report({'INFO'}, f'Exported {filepath}')
        return {'FINISHED'}


def export_svg(obj, filepath):
    verts = [obj.matrix_world @ v.co for v in obj.data.vertices]
    with open(filepath, 'w') as f:
        f.write('<svg xmlns="http://www.w3.org/2000/svg" version="1.1">\n')
        for e in obj.data.edges:
            v1 = verts[e.vertices[0]]
            v2 = verts[e.vertices[1]]
            f.write(
                f'<line x1="{v1.x}" y1="{v1.y}" x2="{v2.x}" y2="{v2.y}" ' \
                'stroke="black" />\n')
        f.write('</svg>')


def export_dxf(obj, filepath):
    verts = [obj.matrix_world @ v.co for v in obj.data.vertices]
    with open(filepath, 'w') as f:
        f.write("0\nSECTION\n2\nENTITIES\n")
        for e in obj.data.edges:
            v1 = verts[e.vertices[0]]
            v2 = verts[e.vertices[1]]
            f.write("0\nLINE\n8\n0\n")
            f.write(f"10\n{v1.x*10}\n20\n{v1.y*10}\n30\n0.0\n")
            f.write(f"11\n{v2.x*10}\n21\n{v2.y*10}\n31\n0.0\n")
        f.write("0\nENDSEC\n0\nEOF\n")


def register():
    bpy.utils.register_class(ExportPatternOperator)


def unregister():
    bpy.utils.unregister_class(ExportPatternOperator)
