from django.shortcuts import render
from events.models import Post, Category, Comment
from events.forms import CommentForm
import requests
# Create your views here.
def blog_index(request):
	posts = Post.objects.all().order_by('created')
	post1 = posts[0].geolocation.lat
	post2 = posts[0].geolocation.lon
	post3 = posts[1].geolocation.lat
	post4 = posts[1].geolocation.lon
	post5 = posts[2].geolocation.lat
	post6 = posts[2].geolocation.lon
	post7 = posts[3].geolocation.lat
	post8 = posts[3].geolocation.lon
	post9 = posts[4].geolocation.lat
	post10 = posts[4].geolocation.lon

	context = {"posts": posts, "post1": post1, "post2":post2, "post3":post3, "post4":post4, "post5":post5, "post6":post6, "post7":post7, "post8":post8, "post9":post9, "post10":post10}
	return render(request, 'blog_index.html', context)

def blog_detail(request, pk):
	post = Post.objects.get(pk=pk)
	geo = str(Post.objects.get(pk=pk).geolocation.lat)
	geol = str(Post.objects.get(pk=pk).geolocation.lon)
	ad = "https://api.breezometer.com/air-quality/v2/current-conditions?lat=" + geo +"&lon=" +geol + "&key=26d253d0e9ef431c8656762275de4471"
	form = CommentForm()
	form = CommentForm()
	response = requests.get(ad)
	data = response.json()
	data1 = data['data']
	data2 = data1['indexes']
	data3 = data2['baqi']
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = Comment(
               op=form.cleaned_data["name"],
               comment=form.cleaned_data["body"],
               category=form.cleaned_data["issues"],
               post=post
            )
			comment.save()
	comments = Comment.objects.filter(post=post)
	context = {"post": post,
	"comments": comments,
	"form":form,
	"datetime": data3['aqi']}
	return render(request, "post_detail.html", context)
def blog_category(request, category):
	posts = Post.objects.filter(
         categories__name__contains=category
              ).order_by(
         'created'
     )
	context = {
         "category": category,
         "posts": posts
     }
	return render(request, "blog_category.html", context)
