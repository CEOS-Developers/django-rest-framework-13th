from django_filters import FilterSet, CharFilter, NumberFilter, BooleanFilter
from .models import Post, User, Profile


class PostFilter(FilterSet):
    user = NumberFilter(field_name='user')

    class Meta:
        model = Post
        fields = ['user']


class ProfileFilter(FilterSet):
    gender = CharFilter(field_name='gender')

    class Meta:
        model = Profile
        fields = ['gender']


class UserFilter(FilterSet):
    username = CharFilter(field_name='username')

    class Meta:
        model=User
        fields = ['username']