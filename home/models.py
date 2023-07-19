
from django.db import models

# Create your models here.
class Department(models.Model):
    dep_name = models.CharField(max_length=100)
    dep_decription = models.TextField()
     
    def  __str__(self):
      return self.dep_name

class Doctors(models.Model):
    
    doc_name =models.CharField(max_length=225,default='SOME STRING')
    doc_spec =models.CharField(max_length=225)
    dep_name =models.ForeignKey(Department, on_delete=models.CASCADE)
    doc_image =models.ImageField(upload_to = 'doctors')

    def  __str__(self):
       return  self.doc_name  + '- (' + self.doc_spec + ')'
    
       
    


class Booking(models.Model):
    p_name = models.CharField( max_length=350,default="")
    p_phone = models.CharField(max_length=20)
    p_mail = models.EmailField()
    doc_name = models.ForeignKey(Doctors,on_delete=models.CASCADE)
    booking_date=models.DateField()
    booked_on =models.DateField(auto_now=True)
