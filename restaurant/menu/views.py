from django.shortcuts import render
from .models import Menu, Category

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_menus = Menu.objects.all().count()
    num_categories = Category.objects.count()  # The 'all()' is implied by default.

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits+1
    
    context = {
        'num_menus': num_menus,
        'num_categories' : num_categories,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


from django.views import generic

class MenuListView(generic.ListView):
    model = Menu
    paginate_by = 10


class MenuDetailView(generic.DetailView):
    model = Menu


class CategoryListView(generic.ListView):
    """Generic class-based list view for a list of categories."""
    model = Category
    paginate_by = 10


class CategoryDetailView(generic.DetailView):
    """Generic class-based detail view for an category."""
    model = Category

from django.shortcuts import render, redirect
from menu.form import ContactForm
from django.http import HttpResponse 


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            pass
            return redirect('success')
    else:
        form = ContactForm()

    context = {
        'form': form
    }
    return render(request, 'menu/contact.html', context)

def success(request):
   return HttpResponse('Success!')

