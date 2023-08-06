from django.db import models

# Create your models here.
class Advertisement(models.Model):
    id = models.CharField("id", max_length=64, primary_key=True)
    title = models.CharField("заголовок", max_length=64)
    description = models.TextField("описание")
    price = models.DecimalField("цена", max_digits=10, decimal_places=2)
    is_auction = models.BooleanField("уместен ли торг", help_text="отметьте, если торг по объявлению уместен")
    updated_at = models.DateField("дата обновления", auto_now=True)
    created_at = models.DateField("дата публикации", auto_now_add=True)

    class Meta:
        db_table = 'advertisements'

    def __str__(self):
        return f'<Advertisement: Advertisement(id={self.id}, title={self.title}, price={self.price})>'