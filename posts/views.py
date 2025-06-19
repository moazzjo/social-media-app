from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Tag
from bs4 import BeautifulSoup
import requests
from django.contrib import messages 
from .forms import postCreateFrom, postEditFrom
# Create your views here.

"""

This is the home page of the web

"""
def home(request, tag=None):
    if tag:
        posts = Post.objects.filter(tags__slug=tag)
        tag = get_object_or_404(Tag, slug=tag)
    else:
        posts= Post.objects.all()
        
    categories = Tag.objects.all()
    return render(request, "posts/home.html", {"posts": posts, 'categories':categories, 'tag':tag})


"""

This is the post view, We Handle Form and add to it some
Info for the picture from flickr through webscraping 


"""
def post_create_view(request):
    form = postCreateFrom()
    if request.method == "POST":
        form = postCreateFrom(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            #step
        try:
            # Step 1: Fetch the page
            url = form.data['url']
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Raise error for HTTP 4xx/5xx

            # Step 2: Parse the HTML
            soup = BeautifulSoup(response.text, 'html.parser')

            # Step 3: Extract the image
            image_tag = soup.select_one('meta[content^="https://live.staticflickr.com/"]')
            if image_tag and image_tag.has_attr('content'):
                post.image = image_tag['content']
            else:
                messages.error(request, 'Could not find a valid image from Flickr.')
                return redirect('post-create')

            # Step 4: Extract the title
            title_tag = soup.select_one('h1.photo-title')
            post.title = title_tag.text.strip() if title_tag else 'Untitled'

            # Step 5: Extract the artist
            artist_tag = soup.select_one('a.owner-name')
            post.artist = artist_tag.text.strip() if artist_tag else 'Unknown Artist'
            
            
        except requests.exceptions.RequestException:
            messages.error(request, 'Failed to connect to the URL. Please check the link.')
            return redirect('post-create')

        except Exception as e:
            messages.error(request, f'An error occurred: {str(e)}')
            return redirect('post-create')
        form.save()
        form.save_m2m()
        return redirect('home')
            
    return render(request, "posts/post_create.html", {"form":form})



def post_delete_view(request,pk):
    get_post = Post.objects.get(id=pk)
    if request.method == "POST":
       get_post.delete()
       messages.success(request, "Post has been Deleted Successfully.")
       return redirect('home')

    return render(request, "posts/post_delete.html", {'post':get_post})


def post_edit_view(request, pk):
    get_post = Post.objects.get(id=pk)
    form = postEditFrom(instance=get_post)
    if request.method == "POST":
        form = postEditFrom(request.POST, instance=get_post)
        if form.is_valid():
            form.save()
            messages.success(request, "post has been updated")
            get_post.save()
        return redirect('home')

    return render(request, "posts/post_edit.html", {'post':get_post, 'form':form})


def post_read_view(request, pk):
    get_post= get_object_or_404(Post, id=pk)
    return render(request, "posts/post_read.html",{'post': get_post})



