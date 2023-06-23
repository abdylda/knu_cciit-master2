from django.contrib.auth.views import LogoutView
from django.urls import path, include
from django.contrib import admin
from main.views import index, cartridge, mainpage, nalichiTehniki, idview, list_reports, kabinet, category, \
    category_koruu, sostoyanieny_koruu, campus, Campus_koruu, documentation, application, tender, \
    kabinet_koruu, UserLoginView, custom_login
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    # path('login/', custom_login, name='login'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('cartridge/', cartridge, name='cartridge'),
    path('mainpage/', mainpage, name='mainpage'),
    path('nalichiTehniki/', nalichiTehniki, name='nalichiTehniki'),
    path('idview/<int:id>', idview, name='idview'),
    path('list_reports/', list_reports, name='idview'),
    path('kabinet/', kabinet, name='kabinet'),
    path('category/', category, name='category'),
    path('campus/', campus, name='campus'),
    path('documentation/', documentation, name='documentation'),
    path('application/', application, name='application'),
    path('tender/', tender, name='tender'),
    path('kabinetti/koruu/<int:id>', kabinet_koruu, name='kabinetti_koruu'),
    path("accounts/", include("django.contrib.auth.urls")),
    path('categoryny/koruu/<int:id>', category_koruu, name='category_koruu'),
    path('Campus/koruu/<int:id>', Campus_koruu, name='Campus_koruu'),
    path('sostoyanieny/koruu/<str:filter>', sostoyanieny_koruu, name='sostoyanieny_koruu'),
    path('chaining/', include('smart_selects.urls')),

]

# urlpatterns += i18n_patterns(
#     '',
#     url(r'^admin/', include(admin.site.urls)),
# )

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
