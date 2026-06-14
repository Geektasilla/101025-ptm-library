from rest_framework.generics import ListCreateAPIView

from library.models import Category
from library.serializers.category import CategorySerializer


class CategoryListCreateGenericView(ListCreateAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
