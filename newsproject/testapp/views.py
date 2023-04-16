from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'testapp/index.html')

def moviesinfo(request):
    head_msg ='Latest movie informaton'
    msg1 = 'sonali slowly get cured'
    msg2 ='modi is going to act some movie'
    msg3 ='modi is going to act some movie'
    my_dict = {'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,'testapp/news.html',context=my_dict)

def sportsinfo(request):
    head_msg ='Latest sports informaton'
    msg1 = 'Dhoni good cricketer'
    msg2 ='kohli good batsman'
    msg3 ='Dhoni good captain'
    my_dict = {'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,'testapp/news.html',context=my_dict)

def politicsinfo(request):
    head_msg ='Latest political informaton'
    msg1 = 'jaganmohanreddy very bad cm'
    msg2 ='modi is going to act some movie'
    msg3 ='chandra babu naidu is old person'
    my_dict = {'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,'testapp/news.html',context=my_dict)
