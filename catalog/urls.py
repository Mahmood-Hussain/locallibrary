from django.urls import path
from catalog import views


urlpatterns = [
    # Handling the index or main page
    path('', views.index, name='index'),
    # the books page
    path('books/', views.BookListView.as_view(), name='books'),
    # the books detail page
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),

    # Handling the Author view
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    # the detailed view of author
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail')
]
