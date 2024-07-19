from django.db.models import Count
from django.shortcuts import render
from django.views.generic.base import TemplateView

from product_module.models import Product, ProductCategory
# class HomeView(View):
#
#     def get(self, request):
#         context = {
#             'data': 'this is data'
#         }
#         return render(request, 'home_module/index_page.html', context)
from sitemodule.models import SiteSetting, FooterLinkBox, Slider
from utils.convertor import group_list


# Create your views here.
# def index_page(request):
#     return render(request, 'home_module/index_page.html')


class HomeView(TemplateView):
    template_name = 'home_module/index_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sliders'] = Slider.objects.filter(is_active=True)
        # context['data'] = 'this is data in home page'
        # context['message'] = 'this is message in home page'

        latest_products = Product.objects.filter(is_active=True, is_delete=False).order_by('-id')[:12]
        most_visit_products = Product.objects.filter(is_active=True, is_delete=False).annotate(
            visit_count=Count('productvisit')).order_by('-visit_count')[:12]

        context['latest_products'] = group_list(latest_products)
        context['most_visit_products'] = group_list(most_visit_products)

        categories = list(ProductCategory.objects.annotate(products_count=Count('product_categories')).filter(is_delete=False, is_active=True, products_count__gt=0)[:6])
        categories_products = []
        for category in categories:
            item = {
                'id': category.id,
                'title': category.title,
                'products': list(category.product_categories.all()[:4])
            }
            categories_products.append(item)

            context['categories_products'] = categories_products

        return context


# def contact_page(request):
#     return render(request, 'home_module')


def site_header_component(request):
    setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()

    context = {
        # 'link': 'آموزش جنگو'
        'siteSetting': setting
    }
    return render(request, 'shared/site_header_partial.html', context)


def site_footer_component(request):
    setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
    footer_link_boxes = FooterLinkBox.objects.all()
    for item in footer_link_boxes:
        pass
        # item.fo
    context = {
        'siteSetting': setting,
        'footer_link_boxes': footer_link_boxes
    }
    return render(request, 'shared/site_footer_partial.html', context)


class AboutView(TemplateView):
    template_name = 'home_module/about_page.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        site_setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
        context['site_setting'] = site_setting
        return context
