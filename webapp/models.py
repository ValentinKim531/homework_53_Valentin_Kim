from django.db import models

# Create your models here.

choices = [('new', 'Новая'), ('in_progress', 'В процессе'), ('finished', 'Сделано')]

class To_do(models.Model):
    title = models.CharField(max_length=100, null=True, blank=False, help_text = 'Заголовок задачи', verbose_name="Заголовок")
    description = models.CharField(max_length=200, null=False, blank=False, help_text = 'Кратко опишите задачу', verbose_name="Описание")
    status = models.CharField(max_length=20, choices=choices, default='new', help_text = 'Статус задачи', verbose_name="Статус")
    execution_date = models.CharField(max_length=10, null=True, blank=False, help_text = 'Введите в формате ГГГГ-ММ-ДД', verbose_name="Дата исполнения")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата и время обновления")

    def __str__(self):
        return f"{self.title} - {self.description} - {self.status} - {self.execution_date}"