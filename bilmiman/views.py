from django.views.generic import TemplateView

from .models import Work, About, Contact


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['works'] = Work.objects.all()
        context['abouts'] = About.objects.all()[:1]
        context['contacts'] = Contact.objects.all()[:1]
        return context
