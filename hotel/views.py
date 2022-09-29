from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import ListView, FormView, View, DeleteView
from .models import Room, Booking
from .forms import AvailabilityForm
from hotel.booking_functions.availability import check_availability
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import AnonymousUser

# Create your views here.

def home(request):
    return render(request, 'hotel/index.html', {})

def about(request):
    return render(request, 'hotel/about.html', {})

def services(request):
    return render(request, 'hotel/services.html', {})

def blog(request):
    return render(request, 'hotel/blog.html', {})

def payment(request):
    return render(request, 'hotel/makepayment.html', {})





def RoomListView(request):
    room = Room.objects.all()[0]
    room_categories = dict(room.ROOM_CATEGORIES)
 

    room_values = room_categories.values()
   
    room_list = []

    for room_category in room_categories:
        room = room_categories.get(room_category)
        room_url = reverse('hotel:RoomDetailView', kwargs={'category': room_category})


        room_list.append((room, room_url))
    context={
        "room_list":room_list,
    }
    return render(request, 'hotel/room_list_view.html', context)


class BookingListView(ListView):
    model=Booking
    template_name="hotel/booking_list.html"

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_staff:
            booking_list = Booking.objects.all()
            return booking_list
        else:
            booking_list = Booking.objects.filter(user=self.request.user)
            return booking_list


class RoomDetailView(View):
    def get(self, request, *args, **kwargs):
        category = self.kwargs.get('category', None)
        form = AvailabilityForm()
        room_list = Room.objects.filter(category=category)
        
        if len(room_list) > 0:
            room = room_list[0]
            room_category = dict(room.ROOM_CATEGORIES).get(room.category, None)

            context={
                'room_category': room_category,
                'form': form,
            }        
        
            return render(request, 'hotel/room_detail_view.html', context)
        else:
            return HttpResponse('Category doesnt exist')
        


    def post(self, request, *args, **kwargs):
        category = self.kwargs.get('category', None)
        room_list =Room.objects.filter(category=category)
        form = AvailabilityForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

        available_rooms=[]
        for room in room_list:
            if check_availability(room, data['check_in'], data['check_out']):
                available_rooms.append(room)

        if len(available_rooms) > 0:
            room = available_rooms[0]
            booking = Booking.objects.create(
                user = self.request.user,
                room = room,
                check_in=data['check_in'],
                check_out=data['check_out']
            )
            booking.save()
            # olu -improvised
            booking = booking
            context={        
            'booking': booking,
            }        
        
            return render(request, 'hotel/olubook.html', context)
           # return HttpResponse (booking)
        elif request.user.is_anonymous:
            # user = AnonymousUser
           
                     
            return HttpResponse('You must be logged in first. LOGIN HERE....')     
            # return render(request, 'hotel/anonymous_booking.html')
        else:
            return HttpResponse('All the rooms in this category are already booked')




# REDUDANT CODE USED INITIALLY, WE DONT NEED IT AGAIN

# class BookingView(FormView):
#     form_class = AvailabilityForm
#     template_name = 'hotel/availability_form.html'

#     def form_valid(self, form):
#         data = form.cleaned_data
#         room_list = Room.objects.filter(category=data['room_category'])
#         available_rooms=[]
#         for room in room_list:
#             if check_availability(room, data['check_in'], data['check_out']):
#                 available_rooms.append(room)

#         if len(available_rooms) > 0:
#             room = available_rooms[0]
#             booking = Booking.objects.create(
#                 user = self.request.user,
#                 room = room,
#                 check_in=data['check_in'],
#                 check_out=data['check_out']
#             )
#             booking.save()
#             return HttpResponse(booking)
#         else:
#             return HttpResponse('This category is booked')



class CancelBookingView(DeleteView):
    model = Booking
    template_name = 'hotel/booking_cancel_view.html'
    success_url = reverse_lazy('hotel:BookingListView')




def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']

        message = request.POST['message']

        # send an email
        send_mail(
            message_name, # name
            message,
            message_email, # email
            ['contact@fizcos.com'], # to email
            )
        
        return render(request, 'hotel/contact.html', {'message_name': message_name})
    else:
        return render(request, 'hotel/contact.html', {})


def book_by_mail(request):
    if request.method == "POST":
        check_in = request.POST['check-in']
        check_out = request.POST['check-out']
        guest_phone = request.POST['phone']
        guest_email = request.POST['email']
        room_select = request.POST['room-select']


        booking_detail = "Phone :" + guest_phone +  "Check In Date: " + check_in + "Check Out Date: "  + check_out  + "Room Selected: " +  room_select
        # send an email
        send_mail(
            'Booking', # subject
            booking_detail,    # message
            guest_email, # from email
            ['contact@fizcos.com'], # to email
            )
        
        return render(request, 'hotel/index.html', {})
    else:
        return render(request, 'hotel/index.html', {})
