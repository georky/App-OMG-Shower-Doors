from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView, PasswordResetConfirmView
from home.forms import RegistrationForm, LoginForm, UserPasswordResetForm, UserSetPasswordForm, UserPasswordChangeForm
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from wkhtmltopdf.views import PDFTemplateView
from django.templatetags.static import static
def index(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/default/')  # Redirige al dashboard tras iniciar sesión
            else:
                # Manejo de error si el usuario no es válido
                form.add_error(None, 'Credenciales inválidas')
    else:
        form = AuthenticationForm()

    context = {'form': form}
    return render(request, 'accounts/signin/illustration.html', context)  # Ajusta la ruta de la plantilla según sea necesario

# Dashboard
@login_required
def default(request):
  context = {
    'parent': 'dashboard',
    'segment': 'default'
  }
  return render(request, 'pages/dashboards/default.html', context)

def automotive(request):
  context = {
    'parent': 'dashboard',
    'segment': 'automotive'
  }
  return render(request, 'pages/dashboards/automotive.html', context)

def smart_home(request):
  context = {
    'parent': 'dashboard',
    'segment': 'smart_home'
  }
  return render(request, 'pages/dashboards/smart-home.html', context)

def crm(request):
  context = {
    'parent': 'dashboard',
    'segment': 'crm'
  }
  return render(request, 'pages/dashboards/crm.html', context)

# Dashboard -> VR
def vr_default(request):
  context = {
    'parent': 'dashboard',
    'sub_parent': 'vr',
    'segment': 'vr_default'
  }
  return render(request, 'pages/dashboards/vr/vr-default.html', context)

def vr_info(request):
  context = {
    'parent': 'dashboard',
    'sub_parent': 'vr',
    'segment': 'vr_info'
  }
  return render(request, 'pages/dashboards/vr/vr-info.html', context)

# Pages
def messages(request):
  context = {
    'parent': 'pages',
    'segment': 'messages'
  }
  return render(request, 'pages/messages.html', context)

def widgets(request):
  context = {
    'parent': 'pages',
    'segment': 'widgets'
  }
  return render(request, 'pages/widgets.html', context)

def charts(request):
  context = {
    'parent': 'pages',
    'segment': 'charts'
  }
  return render(request, 'pages/charts.html', context)

def sweet_alerts(request):
  context = {
    'parent': 'pages',
    'segment': 'sweet_alerts'
  }
  return render(request, 'pages/sweet-alerts.html', context)

def notifications(request):
  context = {
    'parent': 'pages',
    'segment': 'notifications'
  }
  return render(request, 'pages/notifications.html', context)

def pricing_page(request):
  return render(request, 'pages/pricing-page.html')

def rtl(request):
  return render(request, 'pages/rtl-page.html')

# Pages -> Profile
def profile_overview(request):
  context = {
    'parent': 'pages',
    'sub_parent': 'profile',
    'segment': 'profile_overview'
  }
  return render(request, 'pages/profile/overview.html', context)

def teams(request):
  context = {
    'parent': 'pages',
    'sub_parent': 'profile',
    'segment': 'teams'
  }
  return render(request, 'pages/profile/teams.html', context)

def projects(request):
  context = {
    'parent': 'pages',
    'sub_parent': 'profile',
    'segment': 'projects'
  }
  return render(request, 'pages/profile/projects.html', context)

# Pages -> Users
def reports(request):
  context = {
    'parent': 'pages',
    'sub_parent': 'users',
    'segment': 'reports'
  }
  return render(request, 'pages/users/reports.html', context)

def new_user(request):
  context = {
    'parent': 'pages',
    'sub_parent': 'users',
    'segment': 'new_user'
  }
  return render(request, 'pages/users/new-user.html', context)

# Pages -> Accounts
def settings_1(request):
  context = {
    'parent': 'pages',
    'sub_parent': 'accounts',
    'segment': 'settings'
  }
  return render(request, 'pages/account/settings.html', context)

def billing(request):
  context = {
    'parent': 'pages',
    'sub_parent': 'accounts',
    'segment': 'billing'
  }
  return render(request, 'pages/account/billing.html', context)

def invoice(request):
  context = {
    'parent': 'pages',
    'sub_parent': 'accounts',
    'segment': 'invoice'
  }
  return render(request, 'pages/account/invoice.html', context)

def security(request):
  context = {
    'parent': 'pages',
    'sub_parent': 'accounts',
    'segment': 'security'
  }
  return render(request, 'pages/account/security.html', context)

# Pages -> Projects
def general(request):
  context = {
    'parent': 'pages',
    'sub_parent': 'projects',
    'segment': 'general'
  }
  return render(request, 'pages/projects/general.html', context)

def timeline(request):
  context = {
    'parent': 'pages',
    'sub_parent': 'projects',
    'segment': 'timeline'
  }
  return render(request, 'pages/projects/timeline.html', context)

def new_project(request):
  context = {
    'parent': 'pages',
    'sub_parent': 'projects',
    'segment': 'new_project'
  }
  return render(request, 'pages/projects/new-project.html', context)

# Applications
def kanban(request):
  context = {
    'parent': 'applications',
    'segment': 'kanban'
  }
  return render(request, 'pages/applications/kanban.html', context)

def wizard(request):
  context = {
    'parent': 'applications',
    'segment': 'wizard'
  }
  return render(request, 'pages/applications/wizard.html', context)

def datatables(request):
  context = {
    'parent': 'applications',
    'segment': 'datatables'
  }
  return render(request, 'pages/applications/datatables.html', context)

def calendar(request):
  context = {
    'parent': 'applications',
    'segment': 'calendar'
  }
  return render(request, 'pages/applications/calendar.html', context)

def analytics(request):
  context = {
    'parent': 'applications',
    'segment': 'analytics'
  }
  return render(request, 'pages/applications/analytics.html', context)

# Ecommerce
def overview(request):
  context = {
    'parent': 'ecommerce',
    'segment': 'overview'
  }
  return render(request, 'pages/ecommerce/overview.html', context)

def referral(request):
  context = {
    'parent': 'ecommerce',
    'segment': 'referral'
  }
  return render(request, 'pages/ecommerce/referral.html', context)

# Ecommerce -> Products
def new_product(request):
  context = {
    'parent': 'ecommerce',
    'sub_parent': 'products',
    'segment': 'new_product'
  }
  return render(request, 'pages/ecommerce/products/new-product.html', context)

def edit_product(request):
  context = {
    'parent': 'ecommerce',
    'sub_parent': 'products',
    'segment': 'edit_product'
  }
  return render(request, 'pages/ecommerce/products/edit-product.html', context)

def product_page(request):
  context = {
    'parent': 'ecommerce',
    'sub_parent': 'products',
    'segment': 'product_page'
  }
  return render(request, 'pages/ecommerce/products/product-page.html', context)

def products_list(request):
  
  context = {
    'parent': 'ecommerce',
    'sub_parent': 'products',
    'segment': 'products_list'
  }
  return render(request, 'pages/ecommerce/products/products-list.html', context)

# Ecommerce -> Orders
def order_list(request):
  context = {
    'parent': 'ecommerce',
    'sub_parent': 'orders',
    'segment': 'order_list'
  }
  return render(request, 'pages/ecommerce/orders/list.html', context)

def order_details(request):
  context = {
    'parent': 'ecommerce',
    'sub_parent': 'orders',
    'segment': 'order_details'
  }
  return render(request, 'pages/ecommerce/orders/details.html', context)

# Authentication -> Register
def basic_register(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('/accounts/login/basic-login/')
  else:
    form = RegistrationForm()
  
  context = {'form': form}
  return render(request, 'accounts/signup/basic.html', context)

def cover_register(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('/accounts/login/cover-login/')
  else:
    form = RegistrationForm()

  context = {'form': form}
  return render(request, 'accounts/signup/cover.html', context)

def illustration_register(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('/accounts/login/illustration-login/')
  else:
    form = RegistrationForm()

  context = {'form': form}
  return render(request, 'accounts/signup/illustration.html', context)

# Authentication -> Login
class BasicLoginView(LoginView):
  template_name = 'accounts/signin/basic.html'
  form_class = LoginForm

class CoverLoginView(LoginView):
  template_name = 'accounts/signin/cover.html'
  form_class = LoginForm

class IllustrationLoginView(LoginView):
  template_name = 'accounts/signin/illustration.html'
  form_class = LoginForm

# Authentication -> Reset
class BasicResetView(PasswordResetView):
  template_name = 'accounts/reset/basic.html'
  form_class = UserPasswordResetForm

class CoverResetView(PasswordResetView):
  template_name = 'accounts/reset/cover.html'
  form_class = UserPasswordResetForm

class IllustrationResetView(PasswordResetView):
  template_name = 'accounts/reset/illustration.html'
  form_class = UserPasswordResetForm


class UserPasswordResetConfirmView(PasswordResetConfirmView):
  template_name = 'accounts/reset-confirm/basic.html'
  form_class = UserSetPasswordForm

class UserPasswordChangeView(PasswordChangeView):
  template_name = 'accounts/change/basic.html'
  form_class = UserPasswordChangeForm

# Authentication -> Lock
def basic_lock(request):
  return render(request, 'accounts/lock/basic.html')

def cover_lock(request):
  return render(request, 'accounts/lock/cover.html')

def illustration_lock(request):
  return render(request, 'accounts/lock/illustration.html')

# Authentication -> Verification
def basic_verification(request):
  return render(request, 'accounts/verification/basic.html')

def cover_verification(request):
  return render(request, 'accounts/verification/cover.html')

def illustration_verification(request):
  return render(request, 'accounts/verification/illustration.html')

# Error
def error_404(request,exception=None ):
  return render(request, 'accounts/error/404.html')

def error_500(request, exception=None):
  return render(request, 'accounts/error/500.html')

def logout_view(request):
  logout(request)
  return redirect('/accounts/login/illustration-login/')
  #return redirect('/accounts/login/basic-login/')



# i18n
def i18n_view(request):
  context = {
    'parent': 'apps',
    'segment': 'i18n'
  }
  return render(request, 'pages/apps/i18n.html', context)

# views.py


class MyPDFView(PDFTemplateView):
    template_name = 'pages/ecommerce/overview1.html'
    cmd_options = {
        'enable-local-file-access': True,
        'orientation': 'Portrait',
        'page-size': 'A4',
        'encoding': 'UTF-8',
        'quiet': False,  # Elimina el --quiet para ver más detalles del error
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['STATIC_URL'] = settings.STATIC_URL
        context['img1_url'] = static('assets/img/3.jpg')
        context['img2_url'] = static('assets/img/5.jpg')
        return context

