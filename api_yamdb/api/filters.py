import django_filters
from reviews.models import Category, Genre, Title


class TitleFilter(django_filters.FilterSet):
    category = django_filters.ModelChoiceFilter(
        field_name="category",
        to_field_name="slug",
        queryset=Category.objects.all(),
    )

    genre = django_filters.ModelChoiceFilter(
        field_name="genre", to_field_name="slug", queryset=Genre.objects.all()
    )

    name = django_filters.CharFilter(
        field_name="name", lookup_expr="icontains"
    )

    class Meta:
        model = Title
        fields = ("genre", "category", "year", "name")
