import bpy


def export_jpg(obj, filepath):
    uv = obj.data.uv_layers.active
    if not uv:
        return
    bpy.ops.object.select_all(action='DESELECT')
    obj.select_set(True)
    bpy.ops.uv.export_layout(filepath=filepath, mode='PNG', size=(2048, 2048))
    # Convert PNG to JPG using Blender image API
    img = bpy.data.images.load(filepath)
    img.filepath_raw = filepath
    img.file_format = 'JPEG'
    img.save()
    bpy.data.images.remove(img)

def register():
    pass


def unregister():
    pass
