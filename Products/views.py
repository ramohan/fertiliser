from django.shortcuts import render,HttpResponse,render_to_response
from Products.models import Login,Customer,Stock_details,Dealers_details
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
#from Products.forms import PostForm

def login(request):
	return render(request,'login.html')
def test_login(request):
	uname=request.GET['uname']
	pwd=request.GET['pwd']
	try:
		obj= Login.objects.get(username=uname)
	except:
		return HttpResponse("user not available")
	if obj:
		if obj.password==pwd:
			return render(request,'details.html')

			#return HttpResponse("Login successfull")
		else:
			return HttpResponse("incorrect password")
def home(request):
	return render(request,'details.html')

def sign_up(request):
	return render(request,'sign_up.html')
def sign_up_user(request):
	if request.method=="POST":
		Login_Name=request.POST['login']
		try:
			obj=customers.objects.get(Login_Name=login)
		except:
			obj=None
			if not obj:
				if request.POST['pwd1']==request.POST['pwd2']:
					obj=Customer(Login_Name=request.POST['login'],Full_Name=request.POST['full_name'],Password=request.POST['pwd1'],Phone_Number=request.POST['phone_number'] )
					obj.save()
					obj=Login(username=request.POST['login'],password=request.POST['pwd1'])
					obj.save()
					return render(request,'login.html')
				else:
					return HttpResponse("Password doesn't match")
			else:
				return HttpResponse("user already exist")

def check_dealers(request):
	return render(request,'check_dealers.html')

def total_dealers_details(request):
	obj = Dealers_details.objects.all()
	return render_to_response('show_dealers_details.html', {'data': obj})

def new_user_details(request):
	return render(request,'new_user_details.html')

def add_dealers(request):
	return render_to_response(
        'add_dealers.html',
        {'no_of_dealers': range(int(request.GET['dealer']))},
        context_instance=RequestContext(request))

@csrf_protect
def add_dealers_details_to_db(request):
	#import pdb
	#pdb.set_trace()
	dictionary= dict(request.POST.viewitems())
	for i in range(len(dictionary.values()[0])):
		try:
			data= Dealers_details.objects.get(Company_name=dictionary.values[3][i])
		except:
			data= None
		if not data:
			obj = Dealers_details(
				Dealer_name=dictionary.values()[0][i],
				Company_name=dictionary.values()[3][i],
				Phone_name=dictionary.values()[1][i])
			obj.save()
		else:
			return ('all ready exist')
	return render(request,'success.html')

def check_dealer_wise(request):
	return render(request,'check_dealer_wise.html')

def show_dealer_wise_details(request):
	obj=  Dealers_details.objects.get(Dealer_name=request.GET.get('check_dealer_name'))
	return render_to_response('conditioned_dealers.html',{'data': [obj],'search': 'Dealer Name'})

def show_company_wise(request):
	return render(request,'show_company_wise.html')

def show_company_wise_details(request):
	obj= Dealers_details.objects.filter(Company_name=request.GET.get('check_company1_name'))
	return render_to_response('conditioned_dealers.html',{'data': obj,'search': 'Company Name'})

def check_billing(request):
	return render(request,'check_billing.html')

def enter_billing_items(request):
	return render_to_response('enter_billing_items.html',{'no_of_products': range(int(request.GET['billing']))},
		context_instance=RequestContext(request))


def check_stock_details(request):
	obj = Stock_details.objects.all()
	return render_to_response('show_stock.html', {'data': obj})


def add_stock(request):
    return render_to_response(
        'add_stock.html',
        {'no_of_items': range(int(request.GET['item']))},
        context_instance=RequestContext(request))

@csrf_protect
def add_stock_to_db(request):
	#import pdb
	#pdb.set_trace()
	dictionary = dict(request.POST.viewitems())
	for i in range(len(dictionary.values()[0])):
		try:
			data = Stock_details.objects.get(Batch_number = dictionary.values()[3][i])
		except:
			data = None
		if not data:
			obj = Stock_details(
				Batch_number=dictionary.values()[3][i],
				Product_name=dictionary.values()[8][i],
				Company_name=dictionary.values()[4][i],
				Manfacturing_date=dictionary.values()[1][i],
				Expire_date=dictionary.values()[5][i],
				Net_weigth=dictionary.values()[0][i],
				Price=dictionary.values()[2][i],
				Quantity=dictionary.values()[9][i],
				Remarks=dictionary.values()[6][i])
			obj.save()
		else:
			if data.Product_name == dictionary.values()[8][i]:
				data.Quantity = data.Quantity + dictionary.values()[9][i]
				data.save()
			else:
				return HttpResponse("Item Name is not matched")
	return render(request,'success.html')

def check_product_wise(request):
	return render(request,'check_stock_product_wise.html')

def show_product_wise_stock(request):
	obj= Stock_details.objects.get(Product_name=request.GET.get('check_product_name'))
	return render_to_response('conditioned_stock.html',{'data': [obj],'search': 'Product Name'})

def check_company_wise(request):
	return render(request,'check_stock_company_wise.html')

def show_company_wise_stock(request):
	obj= Stock_details.objects.filter(Company_name=request.GET.get('check_company_name'))
	return render_to_response('conditioned_stock.html',{'data': obj,'search': 'Company Name'})

def check_batch_number_wise(request):
	return render(request,'check_stock_batch_number_wise.html')

def show_batch_number_wise_stock(request):
	obj= Stock_details.objects.get(Batch_number=request.GET.get('check_batch_number'))
	return render_to_response('conditioned_stock.html',{'data': [obj],'search': 'Batch Number'})








# Create your views here.
