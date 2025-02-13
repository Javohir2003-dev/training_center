
from django.shortcuts import render,redirect
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ContactForm



class Index_View(TemplateView):
	template_name = 'index.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['form'] = ContactForm()
		return context
	

	def post(self,request, *args, **kwargs):
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('keraksiz')
		return self.render_to_response({'form':form})
	


class Trainer_View(TemplateView):
	template_name = 'trainer.html'
	


class Why_View(TemplateView):
	template_name = 'why.html'
	


class Contact_View(TemplateView):
	template_name = 'contact.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['form'] = ContactForm()
		return context
	

	def post(self,request, *args, **kwargs):
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('keraksiz')
		return self.render_to_response({'form':form})



def keraksiz(request):
	
	return render(request, 'keraksiz.html')


