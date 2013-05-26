from django.views.generic.base import TemplateView

from .models import Patent, License


class Index(TemplateView):
    template_name = "licenses_patents.html"
    
    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context["patents"] = Patent.objects.all()
        context["licenses"] = License.objects.all()
        return context
