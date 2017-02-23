from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Json, Show
from .forms import JsonForm
# Create your views here.


class IndexView(generic.ListView):
    template_name = 'json2sql/index.html'
    context_object_name = 'json_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Json.objects.order_by("-id")


class DetailView(generic.DetailView):
    model = Json
    template_name = 'json2sql/detail.html'


def upload_file(request):
    if request.method == 'POST':
        form = JsonForm(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return HttpResponseRedirect('/success/url/')
    else:
        form = JsonForm()
    return render(request, 'json2sql/sometemplate.html', {'form': form})