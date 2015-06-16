from django import forms
from django.utils.translation import ugettext_lazy as _


SELECT_INPUT_CHOICES = [('item-{0}'.format(i), 'Option item {0}'.format(i)) for i in range(1, 6)]
RADIO_INPUT_CHOICES = [('item-{0}'.format(i), 'Radio item {0}'.format(i)) for i in range(1, 4)]


class BaseForm(forms.Form):
    """
    Base form with inputs
    """
    full_name = forms.CharField(label=_('Full name'))
    email = forms.EmailField(label=_('Email'), required=True, help_text=_('A valid email address, please.'))

    column_input_1 = forms.CharField(label=_('Column input 2'), required=True)
    column_input_2 = forms.CharField(label=_('Column input 2'), required=True)
    column_input_3 = forms.CharField(label=_('Column input 3'), required=False)

    textarea_input = forms.CharField(label=_('Textarea'))

    select_input = forms.ChoiceField(label=_('Select input'), choices=SELECT_INPUT_CHOICES, required=True)
    radio_input = forms.ChoiceField(label=_('Radio inputs'), choices=RADIO_INPUT_CHOICES, widget=forms.RadioSelect, required=False)

    checkbox_input = forms.BooleanField(label=_('Checkbox input'), required=False)
    checkbox_switch_input_1 = forms.BooleanField(label=_('Checkbox switch'), required=False)
    checkbox_switch_input_2 = forms.BooleanField(label=_('Checkbox inline switch'), required=False)
