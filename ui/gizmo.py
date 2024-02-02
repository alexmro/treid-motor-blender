from bpy.types import GizmoGroup, Operator
from bpy.utils import register_classes_factory


class MotorOperator(Operator):
    bl_idname = "motor.run"
    bl_label = "Run scene"
    bl_description = "Run scene"

    def execute(self, context):
        print("Run scene")
        return {'FINISHED'}


class MotorGizmoGroup(GizmoGroup):
    bl_idname = "MotorRunGizmos"
    bl_label = "Run scene"
    bl_space_type = "VIEW_3D"
    bl_region_type = "WINDOW"
    bl_options = {'PERSISTENT', 'SCALE'}

    @classmethod
    def poll(cls, context):
        return True

    def draw_prepare(self, context):
        self.gizmos[0].matrix_basis[0][3] = context.region.width - 30
        self.gizmos[0].matrix_basis[1][3] = 48

    def setup(self, context):
        mpr = self.gizmos.new("GIZMO_GT_button_2d")
        mpr.bl_idname = "MotorRunButton"
        mpr.icon = 'PLAY'
        mpr.draw_options = {'BACKDROP', 'OUTLINE'}
        mpr.target_set_operator(MotorOperator.bl_idname)
        mpr.alpha = 0.5
        mpr.color = 0.1, 0.5, 0.3
        mpr.color_highlight = 0.8, 1.0, 0.8
        mpr.alpha_highlight = 0.2
        mpr.scale_basis = (80 * 0.35) / 2
        mpr.use_tooltip = True
        mpr.show_drag = False


classes = (
    MotorOperator,
    MotorGizmoGroup,
)

register, unregister = register_classes_factory(classes)