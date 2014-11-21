from django import forms
 
class PostForm(forms.Form):
	Product_name=forms.CharField(max_length=20)
	Manfacturing_date=forms.DateTimeField()
	Expire_date=forms.DateTimeField()
	Net_weigth=models.CharField(max_length=20)
	Price=models.IntegerField()
	Quantity=models.IntegerField()
	Remarks=models.CharField(max_length=50)