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
    light = get_object_or_404(Light, pk=request.POST['light'])

    ser = serial.Serial(
    port='/dev/ttyS0',
    baudrate = 115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
    )

    reset = False
    if request.POST['reset']:
        reset = True

    duty = request.POST['duty']
    duty = duty * 25

    light_id = light.number
    data = {"Light control":{"id": light_id, "duty": duty, "reset": reset, "group": False}}
    jsondata = json.dumps(data)

    ser.write(jsondata.encode('utf-8'))

    return render(request, 'lights/bmcomms.html', {'light': light})