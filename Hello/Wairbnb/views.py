from django.shortcuts import render

logid=[]
def index(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        logid.append(username)
        print(logid)
        context={ 'logid':logid,}
        print(username, " has logged in with password ", password)
        return render(request, "index.html" ,context)
    else:
        print("Without logging in")
        return render(request, "index.html")

def login(request):
    print("Request collected at login")
    return render(request, "login.html")

def shareproperty(request):
    return render(request, "shareproperty.html")

def rentproperty(request):
    return render(request, "rentproperty.html")
def profile(request):
    return render(request , "profile.html")

def stories(request):
    return render(request , "stories.html")
def registration(request):
    return render(request , "registration.html")