from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import  CreateView,TemplateView,ListView
from users.models import CustomUser
from services.models import Services


        
class StaffViewServices(LoginRequiredMixin,TemplateView):
      template_name = 'staff/dashboard/services/services-tab.html'
      login_url = 'account_login' # new

      def get_context_data(self, **kwargs):
          
          context = super().get_context_data(**kwargs)
          context = {
            'services':Services.objects.all(),
            'site_name':'Codefyn',
            'page_title':'Staff Dashboard',
            'pagename':'Service List',
            
        }
          return context

   
        
        




