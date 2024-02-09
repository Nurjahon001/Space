from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(default='course_image/default_book_image.png', upload_to='books_image')
    price = models.DecimalField(max_digits=7, decimal_places=2)
    davomiyligi = models.CharField(max_length=50, blank=True, null=True)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'course_table'