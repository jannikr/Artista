from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from Profile.models import ShopUser
from Shop.models import Comment


class CommentsFlagView(ListView):
    model = Comment
    context_object_name = 'comments_with_flag'
    template_name = 'comments-flag.html'

    def get_context_data(self, **kwargs):
        context = super(CommentsFlagView, self).get_context_data(**kwargs)
        can_delete = False
        user = self.request.user
        if not user.is_anonymous:
            can_delete = user.is_superuser or user.is_staff
            # Add if shopUser has its own types
            # shopUser = ShopUser.objects.get(user=user)
            # can_delete = shopUser.candelete()
            context['can_delete'] = can_delete
            return context