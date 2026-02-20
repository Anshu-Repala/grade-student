from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def add(request):
    if(request.method=="POST"):
        num1=int(request.POST.get('num1'))
        num2=int(request.POST.get('num2'))
        inputs=[[28],[35],[55],[60],[74],[100]]
        outputs=['fail','pass','second class','firstclass','just miss','distinction',]
        from sklearn.svm import SVC
        model=SVC()
        model.fit(inputs,outputs)
        res=model.predict([[num1],[num2]])
        return render(request,'index.html',{'s1': res[0],'s2':res[1]})
    else:
        return render(request,'index.html')
    
        username=request.POST.get('username')
        pasword=render.POST.get('pasword')
        if(username=='admin'and pasword=='1234'):
            return render(request,"home.html")
        else:
            return render(request,"login.html")

      #  uname=request.POST.get('uname')
       # pwd=request.POST.get('pwd')
       # if(uname="admin" and pwd="1234"):
        ##    return render(request,"home.html")
       # else:
          #  return render(request,"login.html")
#