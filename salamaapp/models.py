from django.db import models
import datetime
from datetime import datetime, date
import os

# Create your models here.
def filepath(request,filename):
    old_filename= filename
    timeNow= datetime.now().strftime('%y%m%d%H:%M:%S')
    filename= '%s%s' % (timeNow,old_filename)
    return os.path.join('uploads/', filename)





class January(models.Model):
   
    title= models.CharField( max_length=300)
    date= models.DateField( blank=True)

class Feburary(models.Model):
   
    title= models.CharField( max_length=300)
    date= models.DateField( blank=True)

class March(models.Model):
   
    title= models.CharField( max_length=300)
    date= models.DateField( blank=True)

class April(models.Model):
   
    title= models.CharField( max_length=300)
    date= models.DateField( blank=True)

class May(models.Model):
   
    title= models.CharField( max_length=300)
    date= models.DateField( blank=True)

class June(models.Model):
   
    title= models.CharField( max_length=300)
    date= models.DateField( blank=True)

class July(models.Model):
   
    title= models.CharField( max_length=300)
    date= models.DateField( blank=True)

class August(models.Model):
   
    title= models.CharField( max_length=300)
    date= models.DateField( blank=True)

class September(models.Model):
   
    title= models.CharField( max_length=300)
    date= models.DateField( blank=True)

class October(models.Model):
   
    title= models.CharField( max_length=300)
    date= models.DateField( blank=True)

class November(models.Model):
   
    title= models.CharField( max_length=300)
    date= models.DateField( blank=True)

class December(models.Model):
   
    title= models.CharField( max_length=300)
    date= models.DateField( blank=True)
    

class youthpost(models.Model):
    title= models.CharField(max_length=200)
    details= models.CharField(max_length=1000) 
    date= models.DateTimeField(default= datetime.now(), blank=False )
    image= models.ImageField(upload_to=filepath, null=True, blank=True)

class fileupload(models.Model):
    name= models.CharField(max_length=150)
    document= models.FileField(upload_to= filepath, blank=True)
    date= models.DateTimeField(default= datetime.now(), blank=False)

class audioMessage(models.Model):
    message= models.FileField(upload_to=filepath, null=False)

class pastorsCorner(models.Model):
    title=  models.CharField(max_length=200)
    message= models.CharField(max_length=1000)
    image= models.ImageField(upload_to= filepath,null=True, blank=True)
    date= models.DateTimeField(default=datetime.now(), blank=False)
