import os

import bpy


def export(out_dir):
    blend_file_name = bpy.path.basename(bpy.context.blend_data.filepath)
    gltf_file_name = os.path.join(out_dir, blend_file_name.replace('.blend', '.gltf'))
    print('Exporting', blend_file_name, 'to', gltf_file_name)
    bpy.ops.export_scene.gltf(
        filepath=gltf_file_name,
        buffers_embed_data=True,
    )


if __name__ == '__main__':
    import sys
    sys.argv = [__file__] + (sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else [])
    export(sys.argv[1])
