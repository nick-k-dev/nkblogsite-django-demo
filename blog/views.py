from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import dateformat, timezone
from django.contrib import messages
from .models import Post, Author

class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    
    def get_queryset(self):
        return Post.objects.order_by('-created_date')

class DetailView(generic.DetailView):
    model = Post
    template_name = 'blog/detail.html'

def newpost(request):
    authors = Author.objects.all()
    context = {
        'authors': authors,
    }
    return render(request, 'blog/postform.html', context)

def editpost(request, post_id):
    authors = Author.objects.all()
    post = Post.objects.get(pk=post_id)
    context = {
        'authors': authors,
        'post': post,
    }
    return render(request, 'blog/postform.html', context)
    
def addpost(request):
    try:
        post_data = request.POST.copy()
        author_id = post_data.getlist('author')
        author = Author.objects.get(pk=author_id[0])
        title = post_data.get('title')
        description = post_data.get('description')
        created_date = timezone.now()

        #Update if existing post otherwise create one
        if post_data.get('post_id'):
            post_id = post_data.get('post_id')
            post = Post.objects.get(pk=post_id)
            post.author = author
            post.title = title
            post.description = description
            msg = 'Post ' + post.title + ' has been updated - ' + dateformat.format(timezone.now(), 'Y-m-d H:i:s')
        else:
            post = Post(author=author, title=title, description=description, created_date=created_date)
            msg = 'New post ' + post.title + ' has been created - ' + dateformat.format(timezone.now(), 'Y-m-d H:i:s')

        post.save()
        success = True
        print(msg)
        messages.success(request, msg)
    except Exception as err:
        msg = 'Failed to create or update a new post...'
        print(msg)
        messages.error(request, msg)
        print(err)
        success = False
        
    if success:
        return HttpResponseRedirect(reverse('blog:detail', args=(post.id,)))
    else:
        return HttpResponseRedirect(reverse('blog:index'))

