from django.shortcuts import render,redirect
from .models import Post,Category,relen, Ism, Image
from django.views.generic import View,CreateView
from django.core.paginator import Paginator
from django.utils.translation import gettext_lazy as _
from .forms import ContactForm


def main_index(request,id=None):
	form = ContactForm()
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()

		return redirect('main:index')

	query = Post.objects.order_by('?')
	request.title = _("Bosh sahifa")
	if id is not None:
		query = query.filter(post_id=id)
		
	paginator = Paginator(query.all(),10)
	page = paginator.get_page(request.GET.get('page'))

	return render(request,"main/index.html",{
		'object_list' : page.object_list,
		'page_obj' : page,
		'relen' : relen.objects.all(),
		'form' : form
	})

		
		



def main_view_post(request,id):
	request.title = _("Maqolalar")

	post = Post.objects.get(id=id)
	return render(request,"main/view.html",{
		'post' : post
	})


def main_cat(request,id):
	category = Category.objects.filter(id=id).all()

	return render(request, "main/cat.html", {
		'category': category,
		'object_list' : Post.objects.filter(post=id).all()
	})



def main_about(request):
	category = Category.objects.all()	
	ismlar = Ism.objects.all()
	request.title = _("Tovarlar")
	
	return render(request,"main/product.html",{
		'object_list' : Post.objects.all(),
		'category': category,
		"ismlar" : ismlar,
		'images' : Image.objects.all()

	})






