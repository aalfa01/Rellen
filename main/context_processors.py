from main.models import Category

def category(request):
	return {
		'category' : Category.objects.all()
	}