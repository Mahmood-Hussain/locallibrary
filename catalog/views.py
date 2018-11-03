from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre
from django.views import generic


def index(request):
    # View function for home page of site

    # Generate counts of some of main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The all() is applied automatically
    num_authors = Author.objects.count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits
    }

    # Render the HTML template index.html with data in conxtext variable
    return render(request, 'catalog/index.html', context=context)

# class view for books
class BookListView(generic.ListView):
    model = Book
    paginate_by = 2

# detail view of book
class BookDetailView(generic.DetailView):
    model = Book

# class view of Author
class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 3

class AuthorDetailView(generic.DetailView):
    model = Author
