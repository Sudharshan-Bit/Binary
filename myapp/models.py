from django.db import models

from django.db import models

class UploadedImage(models.Model):
    title = models.CharField(max_length=255)  # Image title
    image = models.ImageField(upload_to='uploads/')  # Upload directory
    binary = models.BinaryField()  # Set default value for new records
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Upload timestamp

    def __str__(self):
        return self.title

