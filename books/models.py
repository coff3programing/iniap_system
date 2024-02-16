from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=150, verbose_name="Title")
    image = models.ImageField(upload_to='img/', null=True, verbose_name="Image")
    description = models.TextField(null=True, verbose_name="Description")
    date_register = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'Books'
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        
    def __str__(self) -> str:
        return self.title

    # This function allows me to delete the images.
    def delete(self, using=None, keep_parents=False):
       self.image.storage.delete(self.image.name)
       super().delete()