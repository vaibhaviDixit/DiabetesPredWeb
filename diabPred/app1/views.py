from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import webbrowser
import os

@login_required(login_url="login")
def HomePage(request):
	return render(request,'index.html')

def SignupPage(request):
	if request.method=='POST':
		uname=request.POST.get('username');
		email=request.POST.get('email');
		pwd1=request.POST.get('password1');
		pwd2=request.POST.get('password2');

		if pwd1!=pwd2:
			return HttpResponse("Password not matching!")
		else:
			my_user=User.objects.create_user(uname,email,pwd1)
			my_user.save()
			return redirect("login")
		

	return render(request,'register.html')

def LoginPage(request):
	if request.method=='POST':
		uname=request.POST.get('username');
		pwd=request.POST.get('password');
		user=authenticate(request,username=uname,password=pwd)

		if user is not None:
			login(request,user)
			return redirect("home")
		else:
			return HttpResponse("Invalid Credentials!")

	return render(request,'login.html')

#prediction
@login_required(login_url="login")
def PredictPage(request):
    labels = ["Pregnancies", "Glucose", "Blood Pressure", "Skin Thickness", "Insulin", "BMI", "Diabetes Pedigree Function", "Age"]
    if request.method == 'POST':
        try:
            inputs = [float(request.POST.get(f'input_{i}')) for i in range(8)]
        except ValueError:
        	return render(request, 'popup.html',{'invalid': True})
            

        df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'static', 'app1', 'diabetes.csv'))  # Update with your dataset path
        X = df.drop('Outcome', axis=1)
        y = df['Outcome']

        clf = DecisionTreeClassifier()
        clf.fit(X, y)

        prediction = clf.predict([inputs])

        if prediction[0] == 1:
        	return render(request, 'popup.html',{'diabetes': True})
        else:
        	return render(request, 'popup.html',{'diabetes': False})
    else:
        return render(request, 'predict.html',{'labels': labels})



def LogoutPage(request):
	logout(request)
	return redirect('login')




















