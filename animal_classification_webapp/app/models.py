from django.db import models

# Create your models here.

class StoreImage(models.Model):
    image=models.FileField(null=False,blank=False,upload_to='pictures/')
    prediction=models.CharField(null=True,blank=True,max_length=500)
    
    class Meta:
        verbose_name="Temporary Images"

    def __str__(self) -> str:
        return str(self.pk)
