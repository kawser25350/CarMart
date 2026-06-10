from django.shortcuts import render
from django.views.generic import DetailView
from .models import Car,Comment
from .forms import CommentForm

# Create your views here.

class CarDetailView(DetailView):
    model=Car
    template_name='car/car_details.html'
    context_object_name="car"

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['comment_form']=CommentForm()
        context['comments']=Comment.objects.filter(car=self.object)
        return context
        
    def post(self,request,*args,**kwargs):
        self.object=self.get_object()
        
        form=CommentForm(request.POST)

        if form.is_valid():
            comment=form.save(commit=False)
            comment.car=self.object
            comment.user=request.user
            comment.save()
        return self.get(request,*args,**kwargs)
