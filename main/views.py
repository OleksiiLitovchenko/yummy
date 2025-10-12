from django.shortcuts import render,redirect
from .models import Dish,DishCategory,Gallary,Chef
from django.views.generic import TemplateView
from .forms import ReservationForm




class MainPageView(TemplateView):
    template_name = "main.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = DishCategory.objects.filter(is_visible=True)
        context['gallery'] = Gallary.objects.filter(is_visible=True)
        context['booking_form'] = ReservationForm()
        context['chef'] = Chef.objects.filter(is_visible=True)
        return context

    def post(self, request, *args, **kwargs):
        reservation_form = ReservationForm(request.POST)
        if reservation_form.is_valid():
            reservation_form.save()
            return redirect('main:home')


        context = super().get_context_data(**kwargs)
        context['booking_form'] = reservation_form
        return render(request, self.template_name, context)
