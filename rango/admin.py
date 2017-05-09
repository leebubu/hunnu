from django.contrib import admin

# Register your models here.
from rango.models import Category, Subject, Campus

class CampusAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}
	list_display = ('name', 'name_ch')

class SubjectAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('title',)}
	list_display = ('title', 'title_ch', 'campus')

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}
	list_display = ('name', 'name_ch', 'subject')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Campus, CampusAdmin)
