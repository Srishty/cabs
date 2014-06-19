from django.conf.urls import patterns, url

from views import CabBookingView, BookedCabListView, DeleteBookedCab

urlpatterns = patterns("apps.employee",
    url(r'^cab-booking/$', CabBookingView.as_view(), name = 'cab-booking'),
    url(r'^booked-cab-list/$', BookedCabListView.as_view(), name = 'booked-cab-list'),
    url(r'^delete-booking-cab/$', DeleteBookedCab.as_view(), name = 'delete-booking-cab')
)