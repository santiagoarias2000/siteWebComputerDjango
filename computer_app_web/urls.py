from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from products.views import index_views, customer_views
from products.views import views_products
from products.views import views_laptop
from products.views import views_pc
from products.views import monitor_views
from products.views import views_peripheral
app_name = "cart"
from cart import views_car

urlpatterns = [
    path('admin/', admin.site.urls),
    path('New_computer/', index_views.views, name='index'),

    # views data in the app
    path('products/', views_products.database_views, name='view_products'),
    path('products/laptop/', views_laptop.database_laptop, name='view_laptops'),
    path('products/pc/', views_pc.database_pc, name='view_pc'),
    path('products/monitors/', monitor_views.database_monitor, name='view_monitors'),
    path('products/type-peripheral/', views_peripheral.database_type, name='view_type-peripheral'),
    path('products/type/<int:id>', views_peripheral.data_typeperipheral, name='type_peripheral'),

    # detail data in the products of the app
    path('products/detail/peripheral/<int:id>', views_peripheral.detail_peripheral, name='detail_peripheral'),
    path('products/detail/pc/<int:id>', views_pc.detail_pc, name='detail_pc'),
    path('products/detail/monitor/<int:id>', monitor_views.detail_monitor, name='detail_monitor'),
    path('products/detail/laptop/<int:id>', views_laptop.detail_laptop, name='detail_laptop'),

    # create data by website
    path('products/create/', views_products.create_data, name="product_create"),
    path('products/create/laptop/', views_laptop.create_laptop, name="laptop_create"),
    path('products/create/laptops/', views_laptop.create_laptops, name="laptops_create"),
    path('products/create/monitor/', monitor_views.create_monitor, name="monitor_create"),
    path('products/create/monitors/', monitor_views.create_monitors, name="monitors_create"),
    path('products/create/pc/', views_pc.create_pc, name="pc_create"),
    path('products/create/pcs/', views_pc.create_pcs, name="pcs_create"),
    path('products/create/peripheral/', views_peripheral.create_peripheral, name="peripheral_create"),

    # Update data in one element choose by id
    url(r'^products/update/laptop/(?P<id>\d+)/$', views_laptop.update_laptop, name='update_laptop'),
    url(r'^products/update/monitor/(?P<id>\d+)/$', monitor_views.update_monitor, name='update_monitor'),
    url(r'^products/update/pc/(?P<id>\d+)/$', views_pc.update_pc, name='update_pc'),
    url(r'^products/update/peripheral/(?P<id>\d+)/$', views_peripheral.update_peripheral, name='update_peripheral'),

    # delete data of the database
    url(r'^products/delete(?P<id>\d+)/$', views_products.delete_data, name='delete_products'),
    url(r'^products/delete/laptop/(?P<id>\d+)/$', views_laptop.delete_laptop, name='delete_laptop'),
    url(r'^products/delete/monitor/(?P<id>\d+)/$', monitor_views.delete_monitor, name='delete_monitor'),
    url(r'^products/delete/pc/(?P<id>\d+)/$', views_pc.delete_pc, name='delete_pc'),
    url(r'^products/delete/peripheral/(?P<id>\d+)/$', views_peripheral.delete_peripheral, name='delete_peripheral'),

    # filter
    path('product/filter/', views_products.filter_one_product, name='filter_product'),

    # customer and user
    path('customer/create/', customer_views.create_user, name='user_create'),
    path('customer/login/', customer_views.login_view, name='login'),
    path('customer/logout/', customer_views.logout_v, name='logout'),

    # Super user methods
    path('superuser/create/', customer_views.create_superuser, name='superuser_create'),
    path('superuser/views/', customer_views.views_user, name='views_user'),
    path('superuser/delete/<int:id>', customer_views.delete_user, name='delete_user'),

    # car
    path('car/add_product/<int:product_id>/', views_car.add_product, name='add_product'),
    path('car/delete_product/<int:product_id>/', views_car.delete_product, name='delete_product'),
    path('car/subtract_product/<int:product_id>/', views_car.subtract_product, name='subtract_product'),
    path('car/clean_product/', views_car.clean_car, name='clean_product'),
    path('car/', index_views.cart, name='view_car'),

    # Send mail
    path('sendmail/', views_car.email, name='send_mail')


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
