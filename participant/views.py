from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from .forms import ParticipantForm
from .models import Participant

def displayData(request):
    form = ParticipantForm()
    participants = Participant.objects.filter(id=3)
    return render(request, "index.html", {"form": form, "participants": participants})

def postParticipant(request):
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        # get the form data
        form = ParticipantForm(request.POST)
        # save the data and after fetch the object in instance
        if form.is_valid():
            instance = form.save()
            # serialize in new participant object in json
            ser_instance = serializers.serialize('json', [ instance, ])
            # send to client side.
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)

    # some error occured
    return JsonResponse({"error": ""}, status=400)


