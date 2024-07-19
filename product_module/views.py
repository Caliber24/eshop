from django.db.models import Count
from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from sitemodule.models import SiteBanner
from utils.convertor import group_list
from utils.http_service import get_client_ip
from .models import Product, ProductCategory, ProductBrand, ProductVisit, ProductGallery


# Create your views here.


class ProductListView(ListView):
    template_name = ' product_module/product_list.html'
    model = Product
    context_object_name = 'products'
    ordering = ['-price', 'title']
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        # print('context')
        context = super(ProductListView, self).get_context_data()
        # query = self.get_queryset()
        query = Product.objects.all()
        product: Product = query.order_by('-price').first()
        db_max_price = product.price if product is not None else 1000000
        context['db_max_price'] = db_max_price
        context['start_price'] = self.request.GET.get('start_price') or 0
        context['end_price'] = self.request.GET.get('end_price') or db_max_price
        context['banners'] = SiteBanner.objects.filter(is_active=True,
                                                       position__iexact=SiteBanner.SiteBannerPositions.product_list)

        return context

    def get_queryset(self):
        # print('queryset')
        base_query = super(ProductListView, self).get_queryset()
        query = base_query.filter(is_active=True)
        category_name = self.kwargs.get('cat')
        brand_name = self.kwargs.get('brand')
        request: HttpRequest = self.request
        # print(request.GET)

        start_price = request.GET.get('start_price')
        end_price = request.GET.get('end_price')
        if start_price is not None:
            query = query.filter(price__gte=start_price)
        if end_price is not None:
            query = query.filter(price__lte=end_price)
        if brand_name is not None:
            query = query.filter(brand__url_title__iexact=brand_name)

        if category_name is not None:
            query = query.filter(category__url_title__iexact=category_name)
        return query


def product_list(request):
    # console = ProductCategory(title='پلی استیشن', url_title='playstation')
    # console.save()
    #
    # ps4 = Product(title='play station4', price=16000000, category=console,short_description='ps_4', rating=4)
    # ps4.save()
    products = Product.objects.all().order_by('price')[
               :5]  # hame etelaat ro load namikone -> dasturat ro be dasturat sql tabdil mihkone va hushmand kar mikone
    # products = Product.objects.all().order_by('price')
    # number_of_products = products.count()
    # avg_rating = products.aggregate(Avg('rating'), Min('price'))

    return render(request, ' product_module/product_list.html', {
        'products': products,
        # 'total_number_of_products': number_of_products,
        # 'average_ratings': avg_rating
    })


def product_detail(request, slug):
    # try:
    #     product = Product.objects.get(id=product_id)
    # except:
    #     raise Http404()
    product = get_object_or_404(Product, slug=slug)
    return render(request, ' product_module/product_detail.html', {
        'product': product
    })


class ProductDetailView(DetailView):
    template_name = ' product_module/product_detail.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_product = self.object
        request = self.request
        # favorite_product_id = request.session['product_favorite']
        favorite_product_id = request.session.get('product_favorites')
        context['is_favorite'] = favorite_product_id == str(loaded_product.id)
        context['banners'] = SiteBanner.objects.filter(is_active=True,
                                                       position__iexact=SiteBanner.SiteBannerPositions.product_detail)
        galleries = list(ProductGallery.objects.filter(product_id=loaded_product.id).all())
        galleries.insert(0, loaded_product)
        context['product_galleries_group'] = group_list(galleries, 3)
        context['related_products'] = group_list(
            list(Product.objects.filter(brand_id=loaded_product.brand_id).exclude(pk=loaded_product.id).all()[:12]), 3)
        user_ip = get_client_ip(self.request)
        user_id = None
        # print(user_ip)
        if self.request.user.is_authenticated:
            user_id = self.request.user.id

        has_been_visited = ProductVisit.objects.filter(ip__iexact=user_ip, product_id=loaded_product.id).exists()
        if not has_been_visited:
            new_visit = ProductVisit(ip=user_ip, user_id=user_id, product_id=loaded_product.id)
            new_visit.save()

        return context

    # def get_queryset(self):
    #     pass

    # def get_context_data(self, **kwargs):
    #     context = super(ProductDetailView, self).get_context_data()
    #     slug = self.kwargs['slug']
    #     product = get_object_or_404(Product, slug=slug)
    #     context['product'] = product
    #     return context


# class ProductDetailView(TemplateView):
#     template_name = ' product_module/product_detail.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(ProductDetailView, self).get_context_data()
#         slug = self.kwargs['slug']
#         product = get_object_or_404(Product, slug=slug)
#         context['product'] = product
#         return context


class AddProductFavorite(View):

    def post(self, request):
        product_id = request.POST['product_id']
        product = Product.objects.get(pk=product_id)
        request.session['product_favorites'] = product_id
        return redirect(product.get_absolute_url())


def product_categories_component(request: HttpRequest):
    product_categories = ProductCategory.objects.filter(is_active=True, is_delete=False)
    context = {
        'categories': product_categories
    }
    return render(request, 'components/product_categories_components.html', context)


def product_brands_component(request: HttpRequest):
    product_brands = ProductBrand.objects.annotate(product_count=Count('product')).filter(is_active=True)
    context = {
        'brands': product_brands
    }
    return render(request, ' product_module/components/product_brands_component.html', context)