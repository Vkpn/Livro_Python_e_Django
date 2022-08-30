from django.views.generic.edit import FormView
from main import forms


# Create your views here.
class ViewFaleConosco(FormView):
    template_name = "fale_conosco.html"
    form_class = forms.FormFaleConosco
    success_url = "/"


def form_valid(self, form):
    form.enviar_mensagem_por_email()
    return super().form_valid(form)
