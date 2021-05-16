from django_filters import FilterSet, CharFilter, NumberFilter, BooleanFilter
from django.db.models import Q
from .models import Post, User, Profile


class PostFilter(FilterSet):
    user = NumberFilter(field_name='user')

    class Meta:
        model = Post
        fields = ['user']


class ProfileFilter(FilterSet):
    gender = CharFilter(field_name='gender')
    bio_is_empty = BooleanFilter(field_name='bio', method='filter_bio_is_null')

    class Meta:
        model = Profile
        fields = ['gender']

    def filter_bio_is_null(self,queryset,bio,value):
        filtered_set_true = queryset.filter(bio__isnull = True )
        filtered_set_false = queryset.filter(bio__isnull = False)
        if value:
            return filtered_set_true
        else:
            return filtered_set_false


class UserFilter(FilterSet):
    username = CharFilter(field_name='username')

    class Meta:
        model=User
        fields = ['username']