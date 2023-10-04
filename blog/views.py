from django.shortcuts import redirect, render

from blog.models import Blog


# Create your views here.
def blog_view(request, slug):
    blog = Blog.objects.get(slug=slug)
    if blog.status == "False":
        return redirect("home_page")
    return render(request, "blog.html", {"blog": blog})
