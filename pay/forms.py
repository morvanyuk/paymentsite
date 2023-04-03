from pay.models import Paidusers
from django.forms import ModelForm

class PaidingForm(ModelForm):
    class Meta:
        fields = ('user', 'total_sum')
        model = Paidusers