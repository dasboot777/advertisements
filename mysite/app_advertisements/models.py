from django.db import models
from django.contrib import admin
from django.utils.html import format_html


# Create your models here.
class Advertisement(models.Model):
    id = models.CharField("id", max_length=64, primary_key=True)
    title = models.CharField("заголовок", max_length=64)
    description = models.TextField("описание")
    price = models.DecimalField("цена", max_digits=10, decimal_places=2)
    is_auction = models.BooleanField("уместен ли торг", help_text="отметьте, если торг по объявлению уместен")
    updated_at = models.DateField("дата обновления", auto_now=True)
    created_at = models.DateField("дата публикации", auto_now_add=True)

    @admin.display(description="дата публикации")
    def created_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():#проверяем, что дата создания объявления == сегодня
            created_time = self.created_at.time().strftime("%H:%M:%S")
            return format_html(
                "<span style='color: green; font-weight: bold'>Сегодня в {}</span>", created_time
            )
        return self.created_at.strftime("%d.%m.%Y - %H:%M")

    @admin.display(description="обновлено сегодня")
    def updated_date(self):
        from django.utils import timezone
        if self.updated_at.date() == timezone.now().date():  # проверяем, что дата создания объявления == сегодня
            updated_time = self.updated_at.time().strftime("%H:%M:%S")
            return format_html(
                "<span style='color: red; font-weight: bold'>Обновлено Сегодня в {}</span>", updated_time
            )
        return self.updated_at.strftime("%d.%m.%Y - %H:%M")

    class Meta:
        db_table = 'advertisements'

    def __str__(self):
        return f'<Advertisement: Advertisement(id={self.id}, title={self.title}, price={self.price})>'