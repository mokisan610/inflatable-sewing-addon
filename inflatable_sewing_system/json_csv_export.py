import bpy
import json
import csv


def export_json_csv(obj, json_path, csv_path):
    data = []
    for poly in obj.data.polygons:
        poly_data = {
            'id': poly.index,
            'verts': [list(obj.data.vertices[v].co) for v in poly.vertices]
        }
        data.append(poly_data)

    with open(json_path, 'w') as jf:
        json.dump(data, jf, indent=2)

    with open(csv_path, 'w', newline='') as cf:
        writer = csv.writer(cf)
        writer.writerow(['id', 'verts'])
        for d in data:
            writer.writerow([d['id'], d['verts']])

def register():
    pass


def unregister():
    pass
