from django.db import models

# Create your models here.
class Ration_DB(models.Model):
    Name=models.CharField(max_length=20)
    Email=models.CharField(max_length=50)
    District=models.CharField(max_length=20)
    Village=models.CharField(max_length=50)
    Ward=models.IntegerField()
    Contact=models.IntegerField()
    Aadhar=models.IntegerField()
    Location=models.CharField(max_length=20)
    Image=models.ImageField(upload_to='product_DB')
    shopImage=models.ImageField(upload_to='shop_img',default=True)
    Landmark=models.CharField(max_length=50)
    Working=models.CharField(max_length=15)
    coordinator=models.CharField(max_length=15)
    Password=models.CharField(max_length=15)

    def __str__(self):
        return self.Name
    
    
class Items_DB(models.Model):
    Items=models.CharField(max_length=20)
    Quantity=models.CharField(max_length=50)
    Price=models.CharField(max_length=20)
    Cardtype=models.CharField(max_length=50)
    Ration_id=models.ForeignKey(Ration_DB,on_delete=models.CASCADE)
    def __str__(self):
        return self.Items



