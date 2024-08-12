from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import datetime
from django.conf import settings
import os


def fetch_resources(uri, rel):
       path = os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ""))
       return path


def render_to_pdf(template_src, context_dict={}, pdf_name = {}):
   
    template = get_template(template_src)
    html = template.render(context_dict)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{pdf_name}"'
    pdf_status = pisa.CreatePDF(html.encode("ISO-8859-1"), dest=response,link_callback=fetch_resources )

    if pdf_status.err:
        return HttpResponse('Some errors were encountered <pre>' + html + '</pre>')

    return response

   


    