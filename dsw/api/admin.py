from django.contrib import admin

from api import models 
admin.site.register(models.Students)
admin.site.register(models.ClassCodes)
admin.site.register(models.EnrolledStudentClasses)
admin.site.register(models.Classes)
admin.site.register(models.Feedbacks)
admin.site.register(models.Professors) 