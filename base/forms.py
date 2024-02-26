from django.forms import ModelForm
from base.models import TODO
class TODOForm(ModelForm):
    
    class Meta:
        model = TODO
        fields = ['title', 'status', 'priority', 'description', 'image']