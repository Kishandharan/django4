from django import forms
class inputform(forms.Form):
	input1 = forms.CharField(max_length = 50)
	input2 = forms.CharField(max_length = 50)
	input3 = forms.CharField(max_length = 50)
	input4 = forms.IntegerField(min_value = 1111111111, max_value = 9999999999)
	input5 = forms.IntegerField(min_value = 111111111111, max_value = 999999999999)
	input6 = forms.IntegerField(min_value = 100000, max_value = 999999)




