from django.urls import path
from .views import RoomListView, BookingListView, RoomDetailView, CancelBookingView
from . import views

app_name='hotel'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact-us'),
    path('services/', views.services, name='services'),
    path('blog/', views.blog, name='blog'),
    path('payment/', views.payment, name='payment'),

    path('room_list/', RoomListView, name='RoomListView'),
    path('booking_list/', BookingListView.as_view(), name='BookingListView'),
    # path('book/', BookingView.as_view(), name='BookingView'),
    path('room/<category>', RoomDetailView.as_view(), name='RoomDetailView'),
    path('booking/cancel/<pk>', CancelBookingView.as_view(), name='CancelBookingView'),
]