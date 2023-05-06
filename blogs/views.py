from django.shortcuts import render, get_object_or_404
from .models import Blog


# Create your views here.
def blogPageFun(request):
    allBlogData = Blog.objects.all()
    print(allBlogData)
    for i in allBlogData:
        print(i.image)
    return render(request, 'blog/blog-grid.html', {'allBlogs': allBlogData})


def blog_description(request,id):
    blog_descp = get_object_or_404(Blog, id=id)
    # for i in blog_descp:
    #     print(i)
    print(blog_descp)
    return render(request, 'blog/blog_details.html', {"blog_descp": blog_descp})
