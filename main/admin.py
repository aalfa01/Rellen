from django.contrib import admin
from main.models import Post,Category,relen, Ism, Properties, Image

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = [
		'id',
		'subject_uz',
		'subject_ru',
		'post'
	]
	list_display_links = [
		'id',
		'subject_uz',
		'subject_ru',
	]



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = [
		'id',
		'name_uz',
		'name_ru',
		'image'
	]
	list_display_links = [
		'id',
		'name_uz',
		'name_ru',
	]



@admin.register(relen)
class RelenAdmin(admin.ModelAdmin):
	list_display = [
		'id',
		'image',
		'header'
	]
	list_display_links = [
		'id',
		'image',
		'header'
	]




@admin.register(Ism)
class IsmAdmin(admin.ModelAdmin):
	list_display = [
		'id',
		'name',
		'phone',
		'message'
	]

admin.site.register(Properties)
admin.site.register(Image)
