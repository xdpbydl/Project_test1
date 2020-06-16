from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("欢迎光临！……")


def index1(request):
    string = u"我在自强学堂学习Django，用它来建网站"
    # TutorialList = ["HTML", "CSS", "jQuery", "python", "Django"]
    # info_dict = {'site':u'自强学堂', 'content':u"各种IT技术教程 "}
    # return render(request, "home.html", {"info_dict": info_dict})
    List = map(str,range(100))
    return render(request, 'home.html', {'List': List})


def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))


def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))
