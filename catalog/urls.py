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
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),

    # Viewing page based on current user
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),

    # Viewing page based on books borrowed to librarians only
    path('borrowed/', views.LoanedBooksByUserListViewForLibrarian.as_view(), name='all-borrowed'),

]
urlpatterns += [
    # renew the books by librarian
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
]


urlpatterns += [
    path('author/create/', views.AuthorCreate.as_view(), name='author_create'),
    path('book/create/', views.BookCreate.as_view(), name='book_create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author_update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),
]