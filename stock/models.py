from django.db import models
# Create your models here.
# from phonenumber_field.modelfields import PhoneNumberField
class Stock(models.Model):
    Chassis_No = models.CharField(max_length=150,primary_key=True)
    Engine_No = models.CharField(max_length=150)
    Description = models.CharField(max_length=50)
    Dlr_Invoice_No = models.CharField(max_length=50, blank="True")
    GST_Invoice = models.CharField(max_length=50)
    Manufacturing_Date = models.CharField(max_length=100)
    TM_Invoice_Date = models.CharField(max_length=100)
    Commercial_Invoice = models.CharField(max_length=150)
    Selling_Dealer = models.CharField(max_length=150)
    Product = models.CharField(max_length=150)
    Dealer_Purchase_Order_Price = models.CharField(max_length=150)
    Product_Line = models.CharField(max_length=150)
    LOB = models.CharField(max_length=150)
    Parent_Product_Line = models.CharField(max_length=150)

    def __str__(self):
        return self.Chassis_No

    

        

       