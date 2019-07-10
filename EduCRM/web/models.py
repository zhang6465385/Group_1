from django.db import models

# Create your models here.

class Professional(models.Model):
    professional_name = models.CharField(max_length=20)


class Teacher(models.Model):
    teacher_name = models.CharField(max_length=20)
    work_number = models.IntegerField(default=100000,auto_created=True,blank=True)
    password = models.CharField(max_length=30,default='')
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=11)
    id_card = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=1)
    position = models.CharField(max_length=20)
    professional = models.ForeignKey(Professional,related_name='p_teacher',on_delete=models.SET_NULL,null=True,blank=True)

class Classes(models.Model):
    classes_name = models.CharField(max_length=20)
    class_number = models.CharField(max_length=20)
    professional = models.ForeignKey(Professional,related_name='p_classes' ,on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher,related_name='t_classes',on_delete=models.SET_NULL,blank=True,null=True)


class Parents(models.Model):
    parents_name = models.CharField(max_length=5)
    user_name = models.CharField(max_length=12)
    password = models.CharField(max_length=255)
    id_card = models.CharField(max_length=18)
