from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Menumaster,Submenu,Pagemaster,Coursemaster,Activitytype
from .forms import menuform,submenuform,coursemenuform

# display information

def displaymenu(request):
    menu_items=Menumaster.objects.all()
    sub_items=Submenu.objects.all()
    page_items=Pagemaster.objects.all()
    return render(request,"GLSApp/adminDashboard.html",context={"menu_items":menu_items,"sub_items":sub_items,"page_items":page_items})

def Index(request):
    menu_items=Menumaster.objects.all()
    sub_items=Submenu.objects.all()
    page_items=Pagemaster.objects.all()
    return render(request,"GLSApp/index.html",context={"menu_items":menu_items,"sub_items":sub_items,"page_items":page_items})

def menumaster(request):
    menu_items=Menumaster.objects.all()
    return render(request,"GLSApp/menumaster.html",{"menu_items":menu_items})

def submenumaster(request):
    sub_items=Submenu.objects.all()
    return render(request,"GLSApp/submenumaster.html",{"sub_items":sub_items})

def pagemaster(request):
    page_items=Pagemaster.objects.all()
    return render(request,"GLSApp/pagemaster.html",{"page_items":page_items})

def coursemaster(request):
    cousre_items=Coursemaster.objects.all()
    return render(request,"GLSApp/coursemaster.html",{"course_items":cousre_items})

def activitytype(request):
    activity_items=Activitytype.objects.all()
    return render(request,"GLSApp/activitytype.html",{"activity_items":activity_items})

#add,edit,delte menumaster 
def menumasterEdit(request,menuid):
    object= Menumaster.objects.get(menuid=menuid)
    return render(request,"GLSApp/menumasterEdit.html",{"object":object})

def menumasterUpdate(request,menuid):    
    dataget=Menumaster.objects.get(menuid=menuid)
    form=menuform(request.POST,instance=dataget)
    if form.is_valid:
        form.save()
        dataget=Menumaster.objects.all()
        return redirect('menumaster')
    # return render(request,"GLSApp/menumaster.html",{'dataget':dataget,'form':form})

def menumasterDelete(request,menuid):   
        Menumaster.objects.filter(menuid=menuid).delete()
        return redirect('menumaster')

def menumasterAdd(request):
    if request.method == "POST":
        menutitle=request.POST['menutitle']
        obj=Menumaster.objects.create(menutitle=menutitle)
        obj.save()
        return redirect('menumaster')
    # return render(request, 'GLSApp/menumasterAdd.html')

def menumasterSave(request):
    return render(request,"GLSApp/menumasterAdd.html")

# display,add,edit,delete submenu information

def submenumasterEdit(request,subMenuId):
    sub_object= Submenu.objects.get(subMenuId=subMenuId)
    menu_items = Menumaster.objects.all()
    page = Pagemaster.objects.all()
    return render(request,"GLSApp/submenumasterEdit.html",context={"object":sub_object,'menu_items':menu_items,'page':page})

def submenumasterUpdate(request, subMenuId):    
    dataget=Submenu.objects.get(subMenuId=subMenuId)
    data=Submenu.objects.all()
    if request.method=="POST":
        menuid=request.POST['menuid']
        menuTitle=request.POST['menuTitle']
        menuSequence=request.POST['menuSequence']
        pageId=request.POST['pageId']
        menu_master=Menumaster.objects.get(menuid=menuid)
        page_master=Pagemaster.objects.get(pageId=pageId)
        dataget.menuid=menu_master
        dataget.menuTitle=menuTitle
        dataget.menuSequence=menuSequence
        dataget.pageId=page_master
        dataget.save()
        return redirect('submenumaster')

def submenumasterDelete(request,subMenuId):
    Submenu.objects.filter(subMenuId=subMenuId).delete()
    return redirect('submenumaster')

def submenumasterAdd(request):
    if request.method=="POST":
        menuid=request.POST['menuid']
        menuTitle=request.POST['menuTitle']
        menuSequence=request.POST['menuSequence']
        pageId=request.POST['pageId']
        menumaster = Menumaster.objects.get(menuid=menuid)
        page= Pagemaster.objects.get(pageId=pageId)
        obj=Submenu.objects.create(menuid=menumaster,menuTitle=menuTitle,menuSequence=menuSequence,pageId=page)
        obj.save()
        return redirect('submenumaster')

def submenumasterSave(request):
    menu_items=Menumaster.objects.all()
    page_items=Pagemaster.objects.all()
    return render(request,"GLSApp/submenumasterAdd.html",{'menu_items':menu_items,'page_items':page_items})

# display,add,edit,delte menumaster information

def pagemasterEdit(request,pageId):
    page_object=Pagemaster.objects.get(pageId=pageId)
    course_items=Coursemaster.objects.all()
    return render(request,"GLSApp/pagemasterEdit.html",{'page_object':page_object,'course_items':course_items})

def pagemasterUpdate(request,pageId):
    dataget=Pagemaster.objects.get(pageId=pageId)
    data=Pagemaster.objects.all()
    if request.method=="POST":
        pageName=request.POST['pageName']
        pageContent=request.POST['pageContent']
        courseId=request.POST['courseId']
        course=Coursemaster.objects.get(courseId=courseId)
        dataget.pageName=pageName
        dataget.pageContent=pageContent
        dataget.courseId=course
        dataget.save()
        return redirect('pagemaster')
    
def pagemasterDelete(request,pageId):
    Pagemaster.objects.filter(pageId=pageId).delete()
    return redirect('pagemaster')

def pagemasterAdd(request):
    if request.method=="POST":
        pageName=request.POST['pageName']
        pageContent=request.POST['pageContent']
        courseId=request.POST['courseId']
        course = Coursemaster.objects.get(courseId=courseId)
        obj=Pagemaster.objects.create(pageName=pageName,pageContent=pageContent,courseId=course)
        obj.save()
        return redirect('pagemaster')
  
def pagemasterSave(request):
    course_items=Pagemaster.objects.all()
    course=Coursemaster.objects.all()
    return render(request,"GLSApp/pagemasterAdd.html",{'course_items':course_items,'course':course})

#edit,delete,add course information

def coursemasterEdit(request,courseId):
    course_object=Coursemaster.objects.get(courseId=courseId)
    return render(request,"GLSApp/coursemasterEdit.html",{'course_object':course_object})

def coursemasterUpdate(request,courseId):    
    dataget=Coursemaster.objects.get(courseId=courseId)
    data=Coursemaster.objects.all()
    if request.method=="POST":
        courseName=request.POST['courseName']
        dataget.courseName=courseName
        dataget.save()
        return redirect('coursemaster')
        
def coursemasterAdd(request):
    if request.method=="POST":
        courseName=request.POST['courseName']
        obj=Coursemaster.objects.create(courseName=courseName)
        obj.save()
        return redirect('coursemaster')
  
def coursemasterSave(request):
    return render(request,"GLSApp/coursemasterAdd.html")

def coursemasterDelete(request,courseId):
    Coursemaster.objects.filter(courseId=courseId).delete()
    return redirect('coursemaster')

#edit,delete,add activity information

def activityEdit(request,activityId):
    activity_object=Activitytype.objects.get(activityId=activityId)
    return render(request,"GLSApp/activityEdit.html",{'activity_object':activity_object})

def activityUpdate(request,activityId):    
    dataget=Activitytype.objects.get(activityId=activityId)
    data=Activitytype.objects.all()
    if request.method=="POST":
        activityName=request.POST['activityName']
        dataget.activityName=activityName
        dataget.save()
        return redirect('activitytype')
        
def activityAdd(request):
    if request.method=="POST":
        activityName=request.POST['activityName']
        obj=Activitytype.objects.create(activityName=activityName)
        obj.save()
        return redirect('activitytype')
  
def activitySave(request):
    return render(request,"GLSApp/activityAdd.html")

def activityDelete(request,activityId):
    Activitytype.objects.filter(activityId=activityId).delete()
    return redirect('activitytype')