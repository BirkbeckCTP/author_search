from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required

from submission import models


@staff_member_required
def author_search_manager(request):
    search_term = request.GET.get('search_term')
    frozen_authors = models.FrozenAuthor.objects.none()
    if search_term:
        frozen_authors = models.FrozenAuthor.objects.filter(
            institution__icontains=search_term,
        )
    template = 'author_search/index.html'
    context = {
        'frozen_authors': frozen_authors,
    }
    return render(
        request,
        template,
        context,
    )