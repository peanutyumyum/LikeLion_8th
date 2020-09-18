from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from .models import Post, Comment
from .forms import CommentForm

class IndexView(generic.ListView):
    template_name = 'home.html'
    context_object_name = 'post'
    def get_queryset(self): #ListView에서 사용-표시 하려는 개체 목록을 결정한다. 
        return Post.objects.all()

class DetailView(generic.DetailView):
    model = Post #queryset = Post.objects.all()이랑 같은 기능
    template_name = 'detail.html'
    context_object_name='ppost'

    def get_context_data(self, **kwargs): # **kwargs는 pk를 받아오는 기능임
        context_data = super(DetailView, self).get_context_data(**kwargs) # super는 상속임 여기서는 인자인 DetailView를 상속하고 있음
        context_data['form'] = CommentForm() # 'form'을 써서 html에 띄울 수 있음
        context_data['comment'] = self.object.comment_set.all() # Post 모델이 자신이 참조된 모델이 어딘지 알려주는 것이라고 함 Post.Comment_set.all() 여기서는 뭐 이런식으로 쓰여져 있는 것이겠지? (self.object가 Post이다)
        return context_data

def comment_create(request, post_id):
    if not request.user.is_anonymous: # 로그인 안했냐
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post_id = post_id
            comment.save()
        else:
            messages.info(request, "삐빅 올바르지 않은 댓글 형식이네요")
    else:
        messages.info(request, "삐빅 로그인을 안하셨군요")
    return HttpResponseRedirect(reverse('detail', args=(post_id,)))

def comment_update(request, comment_id, post_id):
    comment_model = Comment.objects.get(pk=comment_id)
    if request.user == comment_model.author:
        updated_form = CommentForm(request.POST)
        if updated_form.is_valid():
            comment_model.delete()
            update_comment = updated_form.save(commit=False)
            update_comment.author = request.user
            update_comment.post_id = post_id
            update_comment.save()
            return redirect('detail', post_id)


def comment_delete(request, comment_id, post_id):
    comment_model = Comment.objects.get(pk=comment_id)
    if request.user == comment_model.author:
        comment_model.delete()
        return redirect('detail', post_id)
    else:
        raise PermissionDenied