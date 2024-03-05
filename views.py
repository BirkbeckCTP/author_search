from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required

from submission import models
from core import models as core_models


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
        'search_term': search_term,
    }
    return render(
        request,
        template,
        context,
    )


@staff_member_required
def editorial_board_search(request):
    search_term = request.GET.get('search_term')
    ed_members = core_models.EditorialGroupMember.objects.none()
    if search_term:
        ed_members = core_models.EditorialGroupMember.objects.filter(
            user__institution__icontains=search_term,
        )
    template = 'author_search/ed_members.html'
    context = {
        'ed_members': ed_members,
        'search_term': search_term,
    }
    return render(
        request,
        template,
        context,
    )