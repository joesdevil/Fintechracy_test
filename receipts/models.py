from django.db import models
from django.contrib.auth.models import User


#receipt model
class Receipt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=255)
    date_of_purchase = models.DateField()
    item_list = models.TextField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self):
        return f"{self.store_name} - {self.date_of_purchase}"
