from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
# from datetime import datetime

# def home(request):
#     content = "<html><body><h1>Welcome to little lemon</h></body></html>"
#     return HttpResponse(content)


# def say_hello(request):
#     return HttpResponse("Hello all")

# def displayDate(request):
#     date_joined =datetime.today().year
#     return HttpResponse(date_joined)

# def menu(request):
#     text = """<h1 style="color: #F4CE14:">THIS IS LITTLE LEMON AGAIN!</h1>"""
#     return HttpResponse(text)


# creating request and response
# def home(request):
#     path = request.path
#     scheme = request.scheme
#     method = request.method
#     address = request.META['REMOTE_ADDR']
#     user_agent = request.META['HTTP_USER_AGENT']
#     path_info= request.path_info
    
#     response = HttpResponse()
#     response.headers['AGE'] = 20
    
#     msg = f"""<br>
#     <br>path: {path}
#     <br>scheme: {scheme}
#     <br>address: {address}
#     <br>method: {method}
#     <br>user_agent: {user_agent}
#     <br>path_info: {path_info}
#     <br> Response header: {response.headers}
    
#     """
   
   # return HttpResponse(msg, content_type='text/html', charset='utf-8')
    # return HttpResponse(path, content_type='text/html', charset='utf-8')

    #
    
# def index(request):
#     path=request.path
#     method=request.method
#     content = '''<center><h2>Testing django request response object<h2>
#     <p>Resquest path : "{}</p>
#     <p>Resquest Method :{}</p></center>
#     '''.format(path,method)
#     return HttpResponse(content)

def pathview(request, name, id):
    return HttpResponse("Name:{} UserID:{}".format(name,id))

def showroom(request):
    return render(request, "forms.html")