from tokenize import group
from django.shortcuts import render, get_object_or_404
import serial
import json

from .models import Light, Group

def index(request):
    light_list = Light.objects.order_by('number')
    group_list = Group.objects.order_by('number')
    context = {
        'light_list': light_list,
        'group_list': group_list,
    }
    return render(request, 'lights/index.html', context)

def light_detail(request, id):
    light = get_object_or_404(Light, pk=id)
    return render(request, 'lights/light_detail.html', {'light': light})

def group_detail(request, id):
    group = get_object_or_404(Group, pk=id)
    return render(request, 'lights/group_detail.html', {'group': group})

def bmcomms(request):
    groupflag = False
    if request.POST['lightorgroup'] == "group":
        groupflag = True
    
    if groupflag:
        group = get_object_or_404(Group, pk=request.POST['group'])
        number = group.number
    else:
        light = get_object_or_404(Light, pk=request.POST['light'])
        number = light.number

    ser = serial.Serial(
    port='/dev/ttyS0',
    baudrate = 115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
    )

    reset = False
    if 'reset' in request.POST:
        reset = True

    duty = int(request.POST['duty'])
    duty = duty * 25
    if duty == 250:
        duty = 255

    data = {"Light control":{"id": number, "duty": duty, "reset": reset, "group": groupflag}}
    jsondata = json.dumps(data)

    ser.write(jsondata.encode('utf-8'))

    if groupflag:
        lightobject = group
    else:
        lightobject = light

    return render(request, 'lights/bmcomms.html', {'lightobject': lightobject, 'reset': reset, 'duty': request.POST['duty']})
