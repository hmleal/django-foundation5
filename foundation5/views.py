from django.views import generic
from forms import BaseForm


class FormView(generic.FormView):
    template_name = 'foundation/forms.html'
    form_class = BaseForm
