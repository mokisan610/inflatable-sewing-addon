import bpy
import bmesh

class GeneratePatternOperator(bpy.types.Operator):
    bl_idname = "inflatable.generate_pattern"
    bl_label = "Generate 2D Pattern & Label Corners"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        obj = context.active_object
        if not obj or obj.type != 'MESH':
            self.report({'ERROR'}, 'Active object must be a mesh')
            return {'CANCELLED'}

        # Duplicate mesh so original is preserved
        dup = obj.copy()
        dup.data = obj.data.copy()
        context.collection.objects.link(dup)

        # Make sure each face is separated by splitting vertices
        me = dup.data
        bm = bmesh.new()
        bm.from_mesh(me)
        bmesh.ops.split_edges(bm, edges=bm.edges)
        bm.to_mesh(me)
        bm.free()

        # Unwrap using seams
        bpy.ops.object.select_all(action='DESELECT')
        dup.select_set(True)
        context.view_layer.objects.active = dup
        bpy.ops.uv.smart_project(angle_limit=66)

        # Label corners using text objects
        for i, v in enumerate(dup.data.vertices):
            txt = bpy.data.curves.new(f"label_{i}", 'FONT')
            txt.body = f"A{i}"
            txt_obj = bpy.data.objects.new(f"label_{i}", txt)
            context.collection.objects.link(txt_obj)
            txt_obj.location = dup.matrix_world @ v.co
            txt_obj.parent = dup

        self.report({'INFO'}, 'Pattern generated')
        return {'FINISHED'}


def register():
    bpy.utils.register_class(GeneratePatternOperator)


def unregister():
    bpy.utils.unregister_class(GeneratePatternOperator)
