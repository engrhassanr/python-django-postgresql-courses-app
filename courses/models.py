from django.db import models

class Course(models.Model):
      image = models.ImageField(upload_to='images/', blank=True, null=True)
      summary = models.CharField(max_length=200)
      description = models.TextField(blank=True, null=True)  # Added description field

      def __str__(self):
            return self.summary
