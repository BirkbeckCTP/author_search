from django.urls import re_path

from plugins.author_search import views

urlpatterns = [
    re_path(
        r'^manager/$',
        views.author_search_manager,
        name='author_search_manager'
    ),
]
