from django.contrib import admin
from catalog.models import Author, Language, Genre, Book, BookInstance

# Register your models here.
# admin.site.register(Book)
admin.site.register(Language)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)


# Inline editing of associated records
class BooksInline(admin.TabularInline):
    model = Book


# Define the admin class
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    # customising the widget
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline]


# Inline editing of associated records
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance


# Register the Admin classes for Book using decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]


# Register the Admin classes for BookInstance using decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('book', 'status', 'borrower', 'due_back', 'id')
    # sectioning the detail view
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower',)
        }),
    )
    # Change the what __str__(self) returns
    list_display = ('id', 'book', 'status', 'due_back')
