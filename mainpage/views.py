from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .forms import IndexForm
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from .VSBLogic import get_class_JSON,get_date,formated

# Create your views here.
def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = IndexForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:

            return HttpResponse(form.cleaned_data.get("class_name"))

            #return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = IndexForm()

    return render(request, 'index.html', {'form': form})


def blue(request):
    return HttpResponse("Hello, world, text 0v0 if you can see this blue.")


def json(request):
    code = formated("","")
    print(code)
    return HttpResponse(code)


def date_test(request):
    return JsonResponse(get_date())
