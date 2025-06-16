import bpy

class RunClothSimOperator(bpy.types.Operator):
    bl_idname = "inflatable.run_cloth_sim"
    bl_label = "Run Cloth Simulation"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        obj = context.active_object
        if not obj or obj.type != 'MESH':
            self.report({'ERROR'}, 'Active object must be a mesh')
            return {'CANCELLED'}

        if 'Cloth' not in obj.modifiers:
            mod = obj.modifiers.new(name='Cloth', type='CLOTH')
            cloth = mod.settings
            cloth.use_sewing_springs = True
            cloth.sewing_force_max = 10
        else:
            mod = obj.modifiers['Cloth']

        bpy.ops.object.modifier_apply(modifier=mod.name)
        self.report({'INFO'}, 'Cloth simulation applied')
        return {'FINISHED'}


def register():
    bpy.utils.register_class(RunClothSimOperator)


def unregister():
    bpy.utils.unregister_class(RunClothSimOperator)
