from django import forms

from index.models import testdb

class LoginForm(forms.Form):
	name = forms.CharField(max_length = 50)        # same vars as the name of <input>
	city = forms.CharField(max_length = 50)
	roll = forms.CharField(max_length = 8)


class SaveForm(forms.ModelForm):

	class Meta:
		model = testdb                         # class Meta, where we tell Django which model should be used to create this form
		fields = ["name", "city", "roll"]      # which field(s) should end up in our form.