from django.contrib.auth import authenticate,login
def login_view(request,*args,**kwargs):
    if request.mothod=='POST':
        username=request.POST['username']
        password=request.POST['password']
#TODO
    user=authenticate(request,username=username,password=password)
    if user is not None:
        login(request,user)
    else:
        pass