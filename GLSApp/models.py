from django.db import models

# Create your models here.
class Menumaster(models.Model):
    menuid = models.AutoField(primary_key=True)
    menutitle = models.CharField(max_length=50)
    def __str__(self):
        return str(self.menuid)

class Coursemaster(models.Model):
    courseId=models.AutoField(primary_key=True)
    courseName=models.CharField(max_length=50)
    def __str__(self):
        return str(self.courseId)

class Pagemaster(models.Model):
    pageId=models.AutoField(primary_key=True)
    pageName=models.CharField(max_length=50)
    pageContent=models.TextField()
    courseId=models.ForeignKey(Coursemaster,default=1,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.pageId)

class Submenu(models.Model):
    subMenuId=models.AutoField(primary_key=True)
    menuid=models.ForeignKey(Menumaster,on_delete=models.CASCADE)
    menuTitle=models.CharField(max_length=50)
    menuSequence=models.IntegerField()
    pageId=models.ForeignKey(Pagemaster,default=1,on_delete=models.CASCADE)

class Activitytype(models.Model):
    activityId=models.AutoField(primary_key=True)
    activityName=models.CharField(max_length=50)
    def __str__(self):
        return str(self.activityId)
   