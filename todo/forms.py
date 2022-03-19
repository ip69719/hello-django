from django import forms # import forms which will allow us to leverage some of the built-in Django form functionality.
from .models import Item # And secondly, we need our item model.


class ItemForm(forms.ModelForm):#To set it up we need to create a new class. I'll call mine ItemForm and it's going to inherit all the functionality of forms.ModelForm To tell the form which model it's going to be associated with.
    class Meta: #meta inner class just gives our form some information about itself.Like which fields it should render how it should display error messages and so on.
        model = Item
        fields = ['name', 'done']
