from django.db import models
from django.contrib.auth import get_user_model

UserModal = get_user_model()

class UpcomingEvent(models.Model):
    title = models.CharField(max_length=120, unique=True)
    description = models.CharField(max_length=280)
    user = models.ForeignKey(to=UserModal, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

# class StudentApplication(models.Model):
#     application = models.FileField(upload_to="student_application/")
#     created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
#     updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

# class CompanyHireEvent(models.Model):
#     title = models.CharField(max_length=120, unique=True)
#     description = models.CharField(max_length=280)
#     exp = models.IntegerField()
#     user = models.ForeignKey(to=UserModal, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
#     updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
#     eligibility = models.CharField(max_length=500)
#     students = models.ForeignKey(to=StudentApplication, on_delete=models.CASCADE, related_name="user_application")
