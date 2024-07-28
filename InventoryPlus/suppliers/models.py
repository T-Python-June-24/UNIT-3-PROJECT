from django.db import models

# def calculate_final_price(quantity, unit_price, discount_percentage):
#     # حساب السعر الإجمالي بدون الخصم
#     total_price = quantity * unit_price
    
#     # حساب قيمة الخصم
#     discount_amount = total_price * (discount_percentage / 100)
    
#     # حساب السعر النهائي بعد الخصم
#     final_price = total_price - discount_amount
    
#     return final_price, discount_amount
#------------------------------------------- later 

class Supplier(models.Model):
    supplierName = models.CharField(max_length=100)
    supplierAddress = models.TextField()
    supplierPhoneNumber = models.CharField(max_length=15)
    supplierEmail = models.EmailField()
    createdAt = models.DateTimeField(auto_now_add=True)
    productQuantity = models.IntegerField()
    unitPrice = models.FloatField()
    totalPrice = models.FloatField()
    supplierDiscount = models.SmallIntegerField()
    supplierImage = models.ImageField(upload_to='images/',default="default.png")


    def __str__(self):
        return self.supplierName