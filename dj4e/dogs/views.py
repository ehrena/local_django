from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.template.loader import render_to_string

from dogs.models import Dog, Breed
from dogs.forms import BreedForm

# Create your views here.
class DogList(LoginRequiredMixin, View) :
    def get(self, request):
        bc = Breed.objects.all().count();
        dl = Dog.objects.all();

        ctx = { 'breed_count': bc, 'dog_list': dl };
        return render(request, 'dogs/dog_list.html', ctx)

class BreedView(LoginRequiredMixin,View) :
    def get(self, request):
        bl = Breed.objects.all();
        ctx = { 'breed_list': bl };
        return render(request, 'dogs/breed_list.html', ctx)

class BreedCreate(LoginRequiredMixin, View):
    template = 'dogs/breed_form.html'
    success_url = reverse_lazy('dogs')
    def get(self, request) :
        form = BreedForm()
        ctx = { 'form': form }
        return render(request, self.template, ctx)

    def post(self, request) :
        form = BreedForm(request.POST)
        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template, ctx)

        breed = form.save()
        return redirect(self.success_url)

class BreedUpdate(LoginRequiredMixin, View):
    model = Breed
    success_url = reverse_lazy('dogs')
    template = 'dogs/breed_form.html'
    def get(self, request, pk) :
        breed = get_object_or_404(self.model, pk=pk) 
        form = BreedForm(instance=breed)
        ctx = { 'form': form }
        return render(request, self.template, ctx)

    def post(self, request, pk) :
        breed = get_object_or_404(self.model, pk=pk) 
        form = BreedForm(request.POST, instance = breed)
        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template, ctx)
        form.save()
        return redirect(self.success_url)

class BreedDelete(LoginRequiredMixin, DeleteView):
    model = Breed
    success_url = reverse_lazy('dogs')
    template = 'dogs/breed_confirm_delete.html'

    def get(self, request, pk) :
        breed = get_object_or_404(self.model, pk=pk) 
        form = BreedForm(instance=breed)
        ctx = { 'breed': breed }
        return render(request, self.template, ctx)

    def post(self, request, pk) :
        breed = get_object_or_404(self.model, pk=pk) 
        breed.delete()
        return redirect(self.success_url)

class DogCreate(LoginRequiredMixin,CreateView):
    model = Dog
    fields = '__all__'
    success_url = reverse_lazy('dogs')

class DogUpdate(LoginRequiredMixin, UpdateView):
    model = Dog
    fields = '__all__'
    success_url = reverse_lazy('dogs')

class DogDelete(LoginRequiredMixin, DeleteView):
    model = Dog
    fields = '__all__'
    success_url = reverse_lazy('dogs')
