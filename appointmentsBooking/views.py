from django.shortcuts import render
from .models import Clients
from .models import Appointmentsdetail
from .models import Calenderslots
from .models import Recommendation
from .models import Practioner
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'home.html',{})

def client(request):
    return render(request,'client.html')

def practitioner(request):
    return render(request,'practitioner.html',{})

def makeAppointment(request):
    if request.method=='POST':
        slotcheck=Calenderslots.objects.filter(date=request.POST.get('date')).filter(timeslot=request.POST.get('time'))
        if slotcheck.exists():
            messages.info(request,'Selected slot is already booked!! Please try another slot')
            return render(request,'client.html',{})
        else:
            print("avaliable")
            new_slot=Calenderslots()
            new_slot.date=request.POST.get('date')
            new_slot.timeslot=request.POST.get('time')
            new_slot.status="Booked"
            new_slot.save()
            client_inst=Clients()
            client_inst.idclients=request.POST.get('idclient')
            newrecord=Appointmentsdetail()
            newrecord.idclients= client_inst
            newrecord.date= request.POST.get('date')
            newrecord.time=request.POST.get('time')
            newrecord.appointmentstatus= "Confirmed"
            newrecord.save()
            messages.success(request,'Appointment is Confirmed')
            return render(request,'client.html',{})
    else:
        return render(request,'client.html',{})


def makeRegistration(request):
    if request.method=='POST':
        emailcheck=Clients.objects.filter(email_id=request.POST.get('email'))
        if emailcheck.exists():
            messages.info(request,'Email Id is already Registered')
            return render(request,'home.html',{})
        else:
            new_client=Clients()
            new_client.name=request.POST.get('name')
            new_client.age=request.POST.get('age')
            new_client.contact_number=request.POST.get('contact')
            new_client.city=request.POST.get('city')
            new_client.email_id=request.POST.get('email')
            new_client.height=request.POST.get('height')
            new_client.weight=request.POST.get('weight')
            new_client.save()
            obj=Clients.objects.get(email_id=request.POST.get('email'))
            messages.success(request,'Your Client Id is %s. Keep it safe!!' %obj.idclients)
            return render(request,'home.html',{})
    else:
        return render(request,'home.html',{})

def makeRecommendation(request):
    if request.method=='POST':
        appointmentcheck=Recommendation.objects.filter(idappointmentdetails=request.POST.get('AppointmentId'))
        if appointmentcheck.exists():
            messages.info(request,'Appointment has already occured')
            return render(request,'practitioner.html',{})
        else:
            client_inst=Clients()
            client_inst.idclients=request.POST.get('clientId')
            practitioner_inst=Practioner()
            practitioner_inst.idpractioner=request.POST.get('PractitionerId')
            appointment_inst=Appointmentsdetail()
            appointment_inst.idappointmentsdetail=request.POST.get('AppointmentId')
            appointment_inst.appointmentstatus="Occured"
            appointment_inst.save(update_fields=['appointmentstatus'])
            new_recommendation=Recommendation()
            new_recommendation.idclients=client_inst
            new_recommendation.idpractioner=practitioner_inst
            new_recommendation.idappointmentdetails=appointment_inst
            new_recommendation.stresslevel=request.POST.get('StressLevel')
            new_recommendation.cholestrol=request.POST.get('cholestrol')
            new_recommendation.bloodpressure=request.POST.get('bloodPressure')
            new_recommendation.dietplan=request.POST.get('dietPlan')
            new_recommendation.save()
            messages.success(request,'Recommendation Submitted Successfully')
            return render(request,'practitioner.html',{})
    else:
        return render(request,'practitioner.html',{})


def viewClientAppointment(request):
    query1= Clients.objects.filter(idclients=request.POST.get('idclient'))
    if query1.exists():
        query= Appointmentsdetail.objects.filter(idclients=request.POST.get('idclient'))
        if query.exists():
            context={'query':query}
            return render(request,'client.html',context)
        else:
            messages.info(request,'No Appointments made by client')
            return render(request,'client.html')
    else:
        messages.info(request,'Client not registered')
        return render(request,'client.html',{})


def viewPractionerAppointment(request):
        query= Appointmentsdetail.objects.filter(appointmentstatus="Confirmed")
        if query.exists():
            context={'query':query}
            return render(request,'practitioner.html',context)
        else:
            messages.info(request,'No upcoming Appointments')
            return render(request,'practitioner.html')


def viewRecommendation(request):
    query1= Clients.objects.filter(idclients=request.POST.get('idclient'))
    if query1.exists():
        queryrecommendation= Recommendation.objects.filter(idclients=request.POST.get('idclient'))
        if queryrecommendation.exists():
            context={'queryrecommendation':queryrecommendation}
            return render(request,'client.html',context)
        else:
            messages.info(request,'No Recommendations for client')
            return render(request,'client.html')
    else:
        messages.info(request,'Client not registered')
        return render(request,'client.html',{})