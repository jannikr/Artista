from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView

from Profile.models import ShopUser
from Shop.models import Comment


class CommentsFlagView(ListView):
    model = Comment
    context_object_name = 'comments_with_flag'
    template_name = 'comments-flag.html'

    def get_context_data(self, **kwargs):
        # TODO get only flagged comments
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

    def post(self, request, *args, **kwargs):
        comment_id = request.POST['comment_id']
        if 'edit' in request.POST:
            return redirect('comment-edit', pk=comment_id)
        if 'delete' in request.POST:
            Comment.objects.get(id=comment_id).delete()
            return redirect('comments-flag')


class CommentEditView(UpdateView):
    model = Comment
    fields = ['text']
    template_name = 'comment-edit.html'
    success_url = reverse_lazy('comments-flag')

    def get_context_data(self, **kwargs):
        context = super(CommentEditView, self).get_context_data(**kwargs)
        user = self.request.user
        if not user.is_anonymous:
            can_delete = user.is_superuser or user.is_staff
            # Add if shopUser has its own types
            # shopUser = ShopUser.objects.get(user=user)
            # can_delete = shopUser.candelete()
            context['can_delete'] = can_delete
            return context
