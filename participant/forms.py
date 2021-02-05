from .models import Participant
from django import forms
import datetime


class ParticipantForm( forms.ModelForm ):
    ## set the label name of the date field.
    dob = forms.DateField(
        label='Date of birth',
        # Set the years range from 1985 to (current year - 15)
        widget=forms.SelectDateWidget( years=range( 1985, datetime.date.today().year - 15 ) )
    )

    class Meta:
        model = Participant
        fields = ("__all__")