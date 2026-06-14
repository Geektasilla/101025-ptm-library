from rest_framework.generics import ListAPIView

from library.models import Book
from library.serializers.book import BookListSerializer


class BookListGenericView(ListAPIView):

    serializer_class = BookListSerializer

    def get_queryset(self):
        qs = Book.objects.all()

        year_from = self.request.query_params.get('year-from')
        category_name = self.request.query_params.get('category')

        if year_from:
            try:
                year_from = int(year_from)

                qs = qs.filter(published_date__year__gte=year_from)
            except ValueError:
                return qs.none()

        if category_name:
            qs = qs.filter(category__name=category_name)

        return qs
