import os.path

from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.views.generic import View

from .utils import render_to_pdf

logo_site = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/image/logo.jpg')

def relatorio_view(request):
    template_name='relatorios.html'
    return render(request, template_name)



class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('template.html')
        context = {
            "invoice_id": 123,
            "customer_name": "John Cooper",
            "amount": 1399.99,
            "today": "Today",
        }
        html = template.render(context)
        pdf = render_to_pdf('template.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" % ("12341231")
            content = "inline; filename='%s'" % (filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" % (filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")




def relatorio_de_testes(request):
    pass


def relatorio_viagem_interno():
    pass
