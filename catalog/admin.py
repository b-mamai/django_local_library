from django.contrib import admin
from .models import Author, Genre, Book, BookInstance
#@admin.register(Book)==admin.site.register(Book)
admin.site.register(Genre)


class BookInline(admin.TabularInline):
    model = Book
    extra = 0


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['last_name', 'first_name', ('date_of_birth', 'date_of_death')]
    """в кортежі в філдс дата народження і смерті будуть відображатись горизонтально"""
    inlines = [BookInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    """додає фільтр справа"""
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )


"""розділили поля перегородкою 1 аргумент заголовок """
"""тобто спочатку 3 поля без заголовка потім заголовок авалібуліті і 2 поля  """




#додаємо  робимо додаткову панель з інтенсами, щоб додає її в форму фук через inlines = [BooksInstanceInline]
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0  #кількість  відображених інстенсів по замовчуванню


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]
#inlines =додали в кінці бук набір інстансів

