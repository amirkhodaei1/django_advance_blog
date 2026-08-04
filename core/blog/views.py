from django.shortcuts import render
# Create your views here.
def indexView(request):
    context={"name":"Amirhossein"}
    return render(request,"blog/index.html",context)