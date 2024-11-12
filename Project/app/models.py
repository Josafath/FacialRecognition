from django.db import models
from django.utils import timezone
# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=50)
    image = models.ImageField(upload_to='students/')
    

    def __str__(self):
        return self.name
    

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    check_in_time = models.DateTimeField(null=True, blank=True)
    check_out_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.student.name} --- {self.date}"
    
    def mark_checked_in(self):
        self.check_in_time = timezone.now()
        self.save()

    def mark_checked_out(self):
        if self.check_in_time:
            self.check_out_time = timezone.now()
            self.save()
        else:
            return ValueError("Cannot mark check out without check in")
        
    
    def calculate_duration(self):
        if self.check_in_time and self.check_out_time:
            duration = self.check_out_time - self.check_in_time
            hours, remainder = divmod(duration.total_seconds(), 3600)
            minutes, seconds = divmod(remainder, 60)
            return f"{int(hours)}h {int(minutes)}m {int(seconds)}s"
        return None
    
    def save(self, *args, **kwargs):
        if not self.pk:  # Only on creation
            self.date = timezone.now().date()
        super().save(*args, **kwargs)



class CameraConfiguration(models.Model):
    name = models.CharField(max_length=50, unique=True, help_text="Give a name to this camera configuration")
    camera_source = models.CharField(max_length=225, help_text="Camera index (0 for default webcam or RTSP/HTTP URL for IP camera)")
    threshold = models.FloatField(default=0.6, help_text="Face recognition confidence threshold")

    def __str__(self):
        return self.name