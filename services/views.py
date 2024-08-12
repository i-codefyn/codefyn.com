from django.views.generic import ListView, DetailView, TemplateView

from .models import Services
from sitesetting.models import Sites
from . import app_settings



class SeoView(TemplateView):
    template_name = "services/seo/seo." + app_settings.TEMPLATE_EXTENSION
    PAGE_TITLE = "SEO"
    extra_context = {
        "page_title": PAGE_TITLE,
    }



class DigitalMarketingView(TemplateView):
    template_name = "services/digital-marketing/digital-marketing." + app_settings.TEMPLATE_EXTENSION
    PAGE_TITLE = "Digital Marketing"
    extra_context = {
        "page_title": PAGE_TITLE,
    }



class DomainBookingView(TemplateView):
    template_name = "services/domain-booking/domain-booking." + app_settings.TEMPLATE_EXTENSION
    PAGE_TITLE = "Domian Booking"
    extra_context = {
        "page_title": PAGE_TITLE,
    }


class MarketingGraphicsView(TemplateView):
    template_name = "services/graphics/marketing." + app_settings.TEMPLATE_EXTENSION
    PAGE_TITLE = "Marketing Graphics Designing"
    extra_context = {
        "page_title": PAGE_TITLE,
    }

class GraphicsPackView(TemplateView):
    template_name = "services/graphics/graphics-pack." + app_settings.TEMPLATE_EXTENSION
    PAGE_TITLE = "Packing Graphics Designing"
    extra_context = {
        "page_title": PAGE_TITLE,
    }   
class GraphicsSmView(TemplateView):
    template_name = "services/graphics/graphics-sm." + app_settings.TEMPLATE_EXTENSION
    PAGE_TITLE = "Social Media Graphics Designing"
    extra_context = {
        "page_title": PAGE_TITLE,
    }   




class GraphicsView(TemplateView):
    template_name = "services/graphics/graphics." + app_settings.TEMPLATE_EXTENSION
    PAGE_TITLE = "Graphics Designing"
    extra_context = {
        "page_title": PAGE_TITLE,
    }   


class SoftDevView(TemplateView):
    template_name = "services/software-development/soft-dev." + app_settings.TEMPLATE_EXTENSION
    PAGE_TITLE = "Software Development"
    extra_context = {
        "page_title": PAGE_TITLE,
    }   



class PerformanceAnalysisView(TemplateView):
    template_name = "services/quick-commerce/quick-commerce-perfomance-analysis." + app_settings.TEMPLATE_EXTENSION
    PAGE_TITLE = "Quick Commerce Performance Analysis"
    extra_context = {
        "page_title": PAGE_TITLE,
    }   


class QuickCommerceView(TemplateView):
    template_name = "services/quick-commerce/quick-commerce." + app_settings.TEMPLATE_EXTENSION
    PAGE_TITLE = "Quick Commerce"
    extra_context = {
        "page_title": PAGE_TITLE,
    }   



class QuickCommercePayementView(TemplateView):
    template_name = "services/quick-commerce/quick-commerce-payment." + app_settings.TEMPLATE_EXTENSION
    PAGE_TITLE = " Quick Commerce Payment Getway Intregration"
    extra_context = {
        "page_title": PAGE_TITLE,
    }  



class CustomQuickCommerceView(TemplateView):
    template_name = "services/quick-commerce/custom-quick-commerce." + app_settings.TEMPLATE_EXTENSION
    PAGE_TITLE = "Custome Quick Commerce"
    extra_context = {
        "page_title": PAGE_TITLE,
    }   



class LogoReDesignView(TemplateView):
    template_name = "services/logodesign/logo-redesign." + app_settings.TEMPLATE_EXTENSION
    PAGE_TITLE = "Logo Redesign"
    extra_context = {
        "page_title": PAGE_TITLE,
    }   


class BrandLogoDesignView(TemplateView):
    template_name = "services/logodesign/brand-logo." + app_settings.TEMPLATE_EXTENSION
    PAGE_TITLE = "Brand Logo Design"
    extra_context = {
        "page_title": PAGE_TITLE,
    }


class LogoDesignView(TemplateView):
    template_name = "services/logodesign/logo-design." + app_settings.TEMPLATE_EXTENSION
    PAGE_TITLE = "Logo Design"
    extra_context = {
        "page_title": PAGE_TITLE,
    }


class CustomLogoDesignView(TemplateView):
    template_name = "services/logodesign/custom-logo-design." + app_settings.TEMPLATE_EXTENSION
    PAGE_TITLE = "Custom Logo Design"
    extra_context = {
        "page_title": PAGE_TITLE,
    }



class EcommercePackPriceDetail(TemplateView):
    """views"""

    template_name = (
        "services/e-commerce_pack_price_detail." + app_settings.TEMPLATE_EXTENSION
    )
    extra_context = {
        "page_title": "E-Commerce Pack Detail",
    }


class CorporatePackPriceDetail(TemplateView):
    """views"""

    template_name = (
        "services/corporate_pack_price_detail." + app_settings.TEMPLATE_EXTENSION
    )
    extra_context = {
        "page_title": "Corporate Pack Detail",
    }


class DynamicPackPriceDetail(TemplateView):
    """views"""

    template_name = (
        "services/dynamic_pack_price_detail." + app_settings.TEMPLATE_EXTENSION
    )
    extra_context = {
        "page_title": "Dynamic Pack Detail",
    }


class StaticPackPriceDetail(TemplateView):
    """views"""

    template_name = "services/static_price_detail." + app_settings.TEMPLATE_EXTENSION
    extra_context = {
        "page_title": "Static Pack Detail",
    }


class StaticPackPrice(TemplateView):
    """views"""

    template_name = "services/static_pack_price." + app_settings.TEMPLATE_EXTENSION
    extra_context = {
        "page_title": "Static Pack Price",
    }


class BasicPack(TemplateView):
    """views"""

    template_name = "services/basic_pack." + app_settings.TEMPLATE_EXTENSION
    extra_context = {
        "page_title": "Basic Pack",
    }


class WebDev(TemplateView):
    """views"""

    template_name = "services/webdev." + app_settings.TEMPLATE_EXTENSION
    extra_context = {
        "page_title": "Web Development Services",
    }


class DynamicWeb(TemplateView):
    """views"""

    template_name = "services/dynamic_web." + app_settings.TEMPLATE_EXTENSION
    extra_context = {
        "page_title": "Dynamic Websites",
    }


class Hrm(TemplateView):
    """views"""

    template_name = "services/HRM." + app_settings.TEMPLATE_EXTENSION
    extra_context = {
        "page_title": "HRM",
    }


class StaticSites(TemplateView):
    """views"""

    template_name = "services/static_sites." + app_settings.TEMPLATE_EXTENSION
    extra_context = {
        "page_title": "Static Sites",
    }


class Portfollio(TemplateView):
    """views"""

    template_name = "services/portfollio." + app_settings.TEMPLATE_EXTENSION
    extra_context = {
        "page_title": "Portfollio",
    }


class Blogs(TemplateView):
    """views"""

    template_name = "services/blogs." + app_settings.TEMPLATE_EXTENSION
    extra_context = {
        "page_title": "Blogs",
    }


class PersonalSites(TemplateView):
    """views"""

    template_name = "services/personal_site." + app_settings.TEMPLATE_EXTENSION
    extra_context = {
        "page_title": "Personal Sites",
    }


class Ecommerce(TemplateView):

    """View"""

    template_name = "services/ecommerce." + app_settings.TEMPLATE_EXTENSION
    extra_context = {
        "page_title": "E-commerce",
    }


class Corporate(TemplateView):

    """View"""

    template_name = "services/corporate." + app_settings.TEMPLATE_EXTENSION
    extra_context = {
        "page_title": "Mobile Web App",
    }


class Cms(TemplateView):

    """View"""

    template_name = "services/CMS." + app_settings.TEMPLATE_EXTENSION
    extra_context = {
        "page_title": "CMS",
    }


class ServicesListViews(ListView):
    model = Services
    context_object_name = "service_list"
    template_name = "services/service_list." + app_settings.TEMPLATE_EXTENSION


class ServicesDetailViews(DetailView):
    model = Services
    context_object_name = "service"  # new
    template_name = "services/service_details." + app_settings.TEMPLATE_EXTENSION
