from django.urls import path

from library.views.categories import CategoryListCreateGenericView
from library.views.books import BookListGenericView


urlpatterns = [
    path('categories', CategoryListCreateGenericView.as_view()),
    path('books', BookListGenericView.as_view()),
    path('authors', CategoryListCreateGenericView.as_view()),
]
