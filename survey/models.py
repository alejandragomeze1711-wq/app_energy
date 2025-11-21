from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SurveyResponse(models.Model):
    questions = models.JSONField()
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    fecha_realizacion = models.DateTimeField(auto_now_add=True)
    

class MonthlyBill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    year = models.IntegerField()            # Ej. 2025
    month = models.IntegerField()           # 1 a 12
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # valor en COP
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'year', 'month')  # evita duplicados
        ordering = ['-year', '-month']

    def __str__(self):
        return f"{self.user.username} - {self.year}/{self.month}: ${self.amount}"