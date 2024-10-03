from django.shortcuts import render
from django.views.generic import View
from myapp.forms import BmiForm,EmiForm,CalorieForm,CalorieManageForm
# Create your views here.


class AdditionView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"add.html") 

    def post(self,request,*args,**kwargs):
       num1=request.POST["box1"]
       num2=request.POST["box2"]
       result=int(num1)+int(num2) 

       data={
        "output":result
       }
       return render(request,"add.html",data)

class SubView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"sub.html")       

    def post(self,request,*args,**kwargs):
       num1=request.POST["box1"]
       num2=request.POST["box2"]
       result=int(num1)-int(num2) 

       data={
        "output":result
       }
       return render(request,"sub.html",data)

class MultiView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"multi.html")       

    def post(self,request,*args,**kwargs):
        num1=request.POST["box1"]
        num2=request.POST["box2"]
        result=int(num1)*int(num2)    

        data={
            "output":result
        }
        return render(request,"multi.html",data)

class DivView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"div.html")

    def post(self,request,*args,**kwargs):
        num1=request.POST["box1"]
        num2=request.POST["box2"]
        result=int(num1)/int(num2)

        data={
            "output":result
        }   
        return render(request,"div.html",data)

class PerfectView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"perfect.html")

    def post(self,request,args,*kwargs):
        num1=int(request.POST["box1"])
        
        fact_sum=sum([i for i in range(1,num1) if num1%i==0])
        if num1==fact_sum:

           data={
              "output":"perfect number"
               }   
        else:
        
            data={
                "output":"not perfect number"
            }
        return render(request,"perfect.html",data)

class ArmView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"arm.html")

    def post(self,request,args,*kwargs):
        num1=int(request.POST["box1"])
        
        fact_sum=sum([i for i in range(1,num1) if num1%i==0])
        if num1==fact_sum:

           data={
              "output":"armstrong number"
               }   
        else:
        
            data={
                "output":"not armstrong number"
            }
        return render(request,"arm.html",data)

class EmiView(View):
    def get(self,request,*args,**kwargs):
        form_instance=EmiForm()

        return render(request,'emi.html',{"form":form_instance})

    def post(self,request,*args,**kwargs):

        form_instance=EmiForm(request.POST)

        if form_instance.is_valid():

            amount=form_instance.cleaned_data.get("amount",0)

            interest=form_instance.cleaned_data.get("interest",0)

            tenure=form_instance.cleaned_data.get("tenure",0)

            EMI=(amount*interest*(1+interest)*tenure)/((1+interest)*tenure-1)

            data={

                "result":EMI,
                "form":form_instance
            }
            return render(request,"emi.html",data)


class BmiView(View):
    def get(self,request,*args,**kwargs):
        form_instance=BmiForm()

        return render(request,'bmi.html',{"form":form_instance})
    def post(self,request,*args,**kwargs):
        form_instance=BmiForm(request.POST)
        if form_instance.is_valid():
            height_in_cm=form_instance.cleaned_data.get("height",0)
            weight_in_kg=form_instance.cleaned_data.get("weight",0)
            height_in_m=height_in_cm/100
            Bmi=weight_in_kg/height_in_m**2
            data={
                "output":Bmi,
                "form":form_instance
            }
            return render(request,"bmi.html",data)
        else:
            data={"form":form_instance,}
            return render(request,'bmi.html',data)

class CalorieView(View):
    def get(self,request,*args,**kwargs):
        form_instance=CalorieForm()
        data={
             "form":form_instance
        }
        return render(request,'calorie.html',data)
    def post(self,request,*args,**kwargs):

        form_instance=CalorieForm(request.POST)

        if form_instance.is_valid():

            weight=form_instance.cleaned_data.get("weight")

            height=form_instance.cleaned_data.get("height")

            age=form_instance.cleaned_data.get("age")

            activity_level=form_instance.cleaned_data.get("activity_level")

            gender=form_instance.cleaned_data.get("gender")

            print(height,weight,age,activity_level,gender)

            if gender=="male":

                BMR=10*weight+6.25*height-5*age+5

            else:
                BMR=10*weight+6.25*height-5*age-161

            calorie=BMR*float(activity_level)


            data={
                "height":height,
                "weight":weight,
                "calorie":calorie,
                "form":form_instance
            }
            return render(request,"calorie.html",data)
        else:
            return render(request,'calorie.html',{"form":form_instance})

def calculate_daily_calorie(age,height,weight,activity_level,gender):

    if gender=="male":

        BMR=10*weight+6.25*height-5*age+5

    else:

        BMR=10*weight+6.25*height-5*age-161

    calorie=(BMR)*float(activity_level)


    return calorie

class CalorieManageView(View):
    def get(self,request,*args,**kwargs):

        form_instance=CalorieManageForm()

        return render(request,'calorie_manage.html',{"form":form_instance})

    def post(self,request,*args,**kwargs):
        
        form_instance=CalorieManageForm(request.POST)

        if form_instance.is_valid():

            weight=form_instance.cleaned_data.get("weight")

            height=form_instance.cleaned_data.get("height")

            age=form_instance.cleaned_data.get("age")

            activity_level=form_instance.cleaned_data.get("activity_level")

            gender=form_instance.cleaned_data.get("gender")

            target_weight=form_instance.cleaned_data.get("target_weight")

            duration=form_instance.cleaned_data.get("duration")

            weight_choices=form_instance.cleaned_data.get("weight_choices")

            calorie=calculate_daily_calorie(age,height,weight,activity_level,gender)

            calorie_deficit=target_weight*7700

            days=duration*7

            daily_calorie_deficit=calorie_deficit/days
            if int(weight_choices)==1:
                calorie+=daily_calorie_deficit
            else:
                calorie-=daily_calorie_deficit

            return render(request,"calorie_manage.html",{"form":form_instance,"calorie":calorie})

class IndexView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"index.html")



