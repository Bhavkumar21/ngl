from django import forms

class UserForm(forms.Form):
  username = forms.CharField(label="Make their profile", widget=forms.TextInput(attrs={'placeholder': 'create username. you have naming rights XD'}), max_length=100)
  fullname = forms.CharField(label="Full Name", max_length=200, widget=forms.TextInput(attrs={'placeholder': 'real names only pretty please. so no duplication'}))
  age = forms.IntegerField(label="Age", widget=forms.TextInput(attrs={'placeholder': 'age is just a number'}))
  identifier = forms.CharField(label="Identifier", max_length=200, widget=forms.TextInput(attrs={'placeholder': '\'is very verry fluffy\''}))

class PostForm(forms.Form):
  content = forms.CharField(
        label="",
        widget=forms.Textarea(attrs={'placeholder': 'Whatever you say is going to stay on the internet forever. haha (evil-villan-laughter)', 'rows': '4'}),
        max_length=500
    )