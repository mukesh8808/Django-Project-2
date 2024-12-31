from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .models import Module
# Create your views here.

class Super_Admin_Panel(View):
    def get(self, request):
        modules = Module.objects.all()
        return render(request,"SuperAdmin/modules.html", {'modules': modules,'checkmodules': True})
    
class Register_Module(View):
    def get(self, request):
        modules = Module.objects.all()
        return render(request,'SuperAdmin/add_modules.html',{'modules': modules})
    def post(self,request):
        module = request.POST.get('module')
        if not module:
            messages.error(request,"Please enter module")
            return redirect("/super-admin/register-module/")
        status = request.POST.get('status')
        if not module:
            messages.error(request,"select status!")
            return redirect("/super-admin/register-module/")
        try:
            obj = Module.object.get(name = module)
            messages.error(request,"Does not inserted duplicate module!")
        except:
            obj = Module(name = module, status = status)
            # obj.save()
            # messages.error(request, "something events disturb!")
        finally:
            obj.save()
        return redirect('/super-admin/register-module/')
    
def company_List(request, id):
    try:
        obj = Module.objects.get(id = int(id))
        return render(request,'SuperAdmin/companies.html', {'company': True})
    except:
        pass
    return redirect('/super-admin/')
    
class Register_Company(View):
    def get(self, request):
        modules = Module.objects.filter(status = 'active')
        return render(request,'SuperAdmin/Company_registration.html',{'modules': modules})
    def post(self,request):
        pass
    
def company_List(request):
    return render(request,'SuperAdmin/companies.html', {'company': True})

def module_List(request, id):
    try:
        # print(id)
        modules = Module.objects.get(id = int(id))
        print(modules,type(modules))
        return render(request,'SuperAdmin/category_module.html', {'modules': modules, 'category': True})
    except:
        pass
    return redirect('/super-admin/')


        