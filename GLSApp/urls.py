from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('adminDashboard/',views.displaymenu,name='displaymenu'),
    path('Index/',views.Index,name='index'),
    path('menumaster/',views.menumaster,name="menumaster"),
    path('submenumaster/',views.submenumaster,name="submenumaster"),
    path('pagemaster/',views.pagemaster,name="pagemaster"),
    path('coursemaster/',views.coursemaster,name="coursemaster"),
    path('activitytype/',views.activitytype,name="activitytype"),
    path('menumasterAdd/',views.menumasterAdd,name="menumasterAdd"),
    path('menumasterSave/',views.menumasterSave,name="menumasterSave"),
    path('menumasterEdit/<int:menuid>/',views.menumasterEdit,name="menumasterEdit"),
    path('menumasterUpdate/<int:menuid>/',views.menumasterUpdate,name="menumasterUpdate"),
    path('menumasterDelete/<int:menuid>',views.menumasterDelete,name="menumasterDelete"),
    path('submenumasterSave/',views.submenumasterSave,name="submenumasterSave"),
    path('submenumasterAdd/',views.submenumasterAdd,name="submenumasterAdd"),
    path('submenumasterEdit/<int:subMenuId>/',views.submenumasterEdit,name="submenumasterEdit"),
    path('submenumasterUpdate/<int:subMenuId>/',views.submenumasterUpdate,name="submenumasterUpdate"),
    path('submenumasterDelete/<int:subMenuId>/',views.submenumasterDelete,name="submenumasterDelete"),
    path('pagemasterAdd',views.pagemasterAdd,name="pagemasterAdd"),
    path('pagemasterSave',views.pagemasterSave,name="pagemasterSave"),
    path('pagemasterEdit/<int:pageId>/',views.pagemasterEdit,name="pagemasterEdit"),
    path('pagemasterUpdate/<int:pageId>/',views.pagemasterUpdate,name="pagemasterUpdate"),
    path('pagemasterDelete/<int:pageId>/',views.pagemasterDelete,name="pagemasterDelete"),
    path('coursemasterAdd/',views.coursemasterAdd,name="coursemasterAdd"),
    path('coursemasterSave/',views.coursemasterSave,name="coursemasterSave"),
    path('coursemasterEdit/<int:courseId>/',views.coursemasterEdit,name="coursemasterEdit"),
    path('coursemasterUpdate/<int:courseId>/',views.coursemasterUpdate,name="coursemasterUpdate"),
    path('coursemasterDelete/<int:courseId>/',views.coursemasterDelete,name="coursemasterDelete"),
    path('activityAdd/',views.activityAdd,name="activityAdd"),
    path('activitySave/',views.activitySave,name="activitySave"),
    path('activityEdit/<int:activityId>/',views.activityEdit,name="activityEdit"),
    path('activityUpdate/<int:activityId>/',views.activityUpdate,name="activityUpdate"),
    path('activityDelete/<int:activityId>/',views.activityDelete,name="activityDelete")
]
