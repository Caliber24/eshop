from django.shortcuts import render, redirect
from django.views.generic import ListView

from sitemodule.models import SiteSetting
from .forms import ContactUsForm, ContactUsModelForm, ProfileForm
from .models import Contact, UserProfile
from django.views.generic.edit import FormView, CreateView

from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
# from django.views.generic import

from django.views import View


# class ContactUsView(FormView):
#
#     template_name = 'contact_module/contact_us_page.html'
#     form_class = ContactUsModelForm
#     success_url = '/products/'
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)


    # def post(self, request):
    #     contact_form = ContactUsModelForm(request.POST)
    #     if contact_form.is_valid():
    #         contact_form.save()
    #         return redirect('home_page')
    #
    #     return render(request, 'contact_module/contact_us_page.html', {
    #         'contact_form': contact_form
    #     })


    #     class ContactUsView(View):
    #
    # def get(self, request):
    #     contact_form = ContactUsModelForm()
    #
    #     return render(request, 'contact_module/contact_us_page.html', {
    #         'contact_form': contact_form
    #     })
    #
    #
    # def post(self, request):
    #     contact_form = ContactUsModelForm(request.POST)
    #     if contact_form.is_valid():
    #         contact_form.save()
    #         return redirect('home_page')
    #
    #     return render(request, 'contact_module/contact_us_page.html', {
    #         'contact_form': contact_form
    #     })



def contact_us_page(request):
    # contact_form = ContactUsForm(request.POST or None)
    if request.method == 'POST':
        # contact_form = ContactUsForm(request.POST)
        current_contact = Contact.objects.get(pk=1)
        contact_form = ContactUsModelForm(request.POST,instance=current_contact)
        if contact_form.is_valid():
            # print(contact_form.cleaned_data)
            # contact = Contact(
            #     title=contact_form.cleaned_data.get('title'),
            #     full_name=contact_form.cleaned_data.get('full_name'),
            #     email=contact_form.cleaned_data.get('email'),
            #     message=contact_form.cleaned_data.get('message')
            # )
            #
            # contact.save()
            contact_form.save()

            return redirect('home_page')

    else:
        # contact_form = ContactUsForm()
        contact_form = ContactUsModelForm()

    return render(request, 'contact_module/contact_us_page.html', {
        'contact_form': contact_form
    })


class ContactUsView(CreateView):
    # model = Contact
    # fields = ['name', 'email', '']
    form_class = ContactUsModelForm
    template_name = 'contact_module/contact_us_page.html'
    success_url = '/products/'

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
        context['sitesetting'] = setting
        return context


def store_file(file):
    with open('temp/image.jpg', 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)


class CreateProfileView(CreateView):
    template_name = 'contact_module/create_profile_page.html'
    model = UserProfile
    fields = '__all__'
    success_url = '/contact/create-profile'



    # def get(self, request, *args, **kwargs):
    #     form = ProfileForm()
    #     return render(request,'contact_module/create_profile_page.html',{
    #         'form': form
    #     })
    #
    # def post(self, request, *args, **kwargs):
    #     # print(request.FILES)
    #     submitted_form = ProfileForm(request.POST, request.FILES)
    #
    #     if submitted_form.is_valid():
    #         # store_file(request.FILES['profile'])
    #         profile = UserProfile(image=request.FILES['user_image'])
    #         profile.save()
    #         return redirect('create_profile_page')
    #
    #     return render(request, 'contact_module/create_profile_page.html',{
    #         'form': submitted_form
    #     })


class ProfilesView(ListView):
    model = UserProfile
    template_name = 'contact_module/profiles_list_page.html'
    context_object_name = 'profiles'
