import bpy


def export_plt(obj, filepath):
    verts = [obj.matrix_world @ v.co for v in obj.data.vertices]
    with open(filepath, 'w') as f:
        f.write('IN;')
        for e in obj.data.edges:
            v1 = verts[e.vertices[0]]
            v2 = verts[e.vertices[1]]
            f.write(f'PU{v1.x*10},{v1.y*10};PD{v2.x*10},{v2.y*10};')
        f.write('IN;')

def register():
    pass


def unregister():
    pass
