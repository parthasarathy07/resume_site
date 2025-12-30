from django.db import models
import os

class Resume(models.Model):
    file = models.FileField(upload_to='resumes/')
    uploaded_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Resume"

    def save(self, *args, **kwargs):
        if self.pk:
            old_resume = Resume.objects.get(pk=self.pk)
            if old_resume.file and old_resume.file != self.file:
                if os.path.isfile(old_resume.file.path):
                    os.remove(old_resume.file.path)
        super().save(*args, **kwargs)
