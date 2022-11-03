from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from .forms import ContactForm


class AboutView(TemplateView):
    template_name = "website/about.html"


class ContactView(FormView):
    """This class is for calling the contact form"""
    template_name = 'website/contact.html'
    form_class = ContactForm
    success_url = '/contact/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super().form_valid(form)


class IndexView(TemplateView):
    template_name = "website/index.html"


class ProjectView(TemplateView):
    template_name = "website/projects.html"


class SingleView(TemplateView):
    template_name = "website/single.html"


class ServiceView(TemplateView):
    template_name = "website/services.html"
