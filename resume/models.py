from django.db import models
import os

class Resume(models.Model):
    file = models.FileField(upload_to='resumes/')
    uploaded_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return os.path.basename(self.file.name) if self.file else "Resume (no file)"

    def save(self, *args, **kwargs):
        if self.pk:
            old_resume = Resume.objects.get(pk=self.pk)
            if old_resume.file and old_resume.file != self.file:
                old_resume.file.delete(save=False)
        super().save(*args, **kwargs)
