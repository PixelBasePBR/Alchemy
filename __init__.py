import bpy

bl_info = {
    "name": "alchemy",
    "author": "Aurorah Harmony",
    "description": "",
    "blender": (3, 4, 0),
    "version": (0, 0, 1),
    "location": "",
    "warning": "",
    "category": "3D View",
}


# class SimpleEditor(bpy.types.Panel):
#     """A simple custom editor panel"""

#     bl_label = "Simple Editor"
#     bl_idname = "VIEW3D_PT_simple_editor"
#     bl_space_type = "VIEW_3D"
#     bl_region_type = "UI"
#     bl_category = "Custom"

#     def draw(self, context):
#         layout = self.layout
#         layout.label(text="Welcome to the Simple Editor!")


# def register():
#     bpy.utils.register_class(SimpleEditor)


# def unregister():
#     bpy.utils.unregister_class(SimpleEditor)


# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()
