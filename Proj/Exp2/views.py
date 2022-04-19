from django.shortcuts import render, redirect
from .models import GeeksModel
from .forms import GeeksForm
from django.shortcuts import render, redirect

from .forms import GeeksForm
from .models import GeeksModel


# Create your views here.

def home(request):
    return render(request, 'Exp2/home.html', )


def register(request):
    return render(request, 'Exp2/register.html')
# relative import of forms


def create(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = GeeksForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_view')

    context['form'] = form
    return render(request, "Exp2/create.html", context)


def list_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["dataset"] = GeeksModel.objects.all()

    return render(request, "Exp2/list_view.html", context)


def detail_view(request, pk):
    dataset = GeeksModel.objects.filter(id=pk)
    return render(request, "Exp2/detail_view.html", {'dataset': dataset})


def update(request, pk):
    order = GeeksModel.objects.get(id=pk)
    form = GeeksForm(instance=order)

    if request.method == 'POST':
        form = GeeksForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('list_view')

    context = {'form': form}
    return render(request, "Exp2/update.html", context)

def neuralnet(request):
    return render(request, 'Exp2/neuralnet.html', )