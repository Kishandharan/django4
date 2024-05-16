from django.shortcuts import render
from app1.forms import inputform

customer_id = 4000
def home(request):
	global customer_id
	if request.method == "POST":
		form1 = inputform(request.POST)
		if form1.is_valid():
			data = form1.cleaned_data
			fname = data.get('input1')
			lname = data.get('input2')
			email = data.get('input3')
			mobile = data.get('input4')
			aadhaar = data.get('input5')
			pincode = data.get('input6')
			customer_id += 1
			greeting = f"""
			Dear {fname}, 
			Congrats on opening an account in ICICI bank.
			Your customer id is {customer_id}
			"""
			return render(request, 'app1/index.html', {'param1':greeting,'form':form1})
	else:
		form1 = inputform()
	return render(request, 'app1/index.html', {'form':form1})	

