from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q
import datetime
from django.views import View
from ntc_templates.parse import parse_output
from .parse_test import output
import netmiko
from netmiko import ConnectHandler
from .credentials import password1, username1
from .parse_test import output

# using module from django:
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
    )
# Create your views here.

def controller_choose(request):
    return render(request, 'Migration_Website/controller_choose.html')

def ap_list(request):
    # Connect to correct controller:
    # ip_address = "{}.{}.{}.{}".format(a, b, c, d)
    # cisco1 = {
    #     "ip": ip_address
    #     "username": username1,
    #     "password": password1,
    #     "device_type": "cisco_wlc_ssh",
    #     'global_delay_factor': 4,
    #     'banner_timeout': 7
    # }
    # net_connect = ConnectHandler(**cisco1)
    # Send command and get output from controller:
    # command = "show ap summary"
    # output = net_connect.send_command(command)
    # parse output using ntc_templates:
    new_output = parse_output(platform="cisco_wlc_ssh", command="show ap summary", data=output)
    # render output as {'context': new_output} becouse django dont accept contect as list of dist:
    return render(request, 'Migration_Website/ap_list.html', {'context': new_output})