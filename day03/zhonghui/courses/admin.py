from django.contrib import admin

from .models import Teacher, Course, Student, TeacherAssistant


class TeacherAdmin(admin.ModelAdmin):
    # 界面要显示的内容
    list_display = ["nickname", "introduction", "fans"]
    # list_display_teacher = ["nickname", "introduction", "fans"]


# class StudentAdmin(admin.ModelAdmin):
#     list_display = ["course", "age", "gender"]  # 会报错，好像和上面的list_display冲突


# Register your models here.
admin.site.register(Teacher, TeacherAdmin)
# admin.site.register(Course)  # 不显示其它信息，只显示名字
admin.site.register(Course)
# admin.site.register(Student, StudentAdmin)
admin.site.register(Student)
admin.site.register(TeacherAssistant)
