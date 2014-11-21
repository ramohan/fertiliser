from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Fertilizers.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^login/', 'Products.views.login'),
    url(r'^sign_up/','Products.views.sign_up'),
    url(r'^sign_up_user/','Products.views.sign_up_user'),
    url(r'^test_login/','Products.views.test_login'),
    url(r'^total_dealers_details/','Products.views.total_dealers_details'),
    url(r'^check_dealers/','Products.views.check_dealers'),
    url(r'^new_user_details/','Products.views.new_user_details'),
    url(r'^add_dealers/','Products.views.add_dealers'),
    url(r'^add_dealers_details_to_db/','Products.views.add_dealers_details_to_db'),
    url(r'^check_dealer_wise/','Products.views.check_dealer_wise'),
    url(r'^show_dealer_wise_details/','Products.views.show_dealer_wise_details'),
    url(r'^show_company_wise/','Products.views.show_company_wise'),
    url(r'^show_company_wise_details/','Products.views.show_company_wise_details'),
    url(r'^check_billing/','Products.views.check_billing'),
    url(r'^enter_billing_items/','Products.views.enter_billing_items'),
    url(r'^check_stock/','Products.views.check_stock_details'),
    url(r'^add_stock/','Products.views.add_stock'),
    url(r'^add_stock_to_db/','Products.views.add_stock_to_db'),
    url(r'^home/','Products.views.home'),
    url(r'^check_product_wise/','Products.views.check_product_wise'),
    url(r'^show_product_wise_stock/','Products.views.show_product_wise_stock'),
    url(r'^check_company_wise/','Products.views.check_company_wise'),
    url(r'^show_company_wise_stock/','Products.views.show_company_wise_stock'),
    url(r'^check_batch_number_wise/','Products.views.check_batch_number_wise'),
    url(r'^show_batch_number_wise_stock/','Products.views.show_batch_number_wise_stock'),

    url(r'^admin/', include(admin.site.urls)),
)
