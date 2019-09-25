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
import ast

# using module from django:
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
    )
# Create your views here.

ap_to_migration = list()

def controller_choose(request):
    return render(request, 'Migration_Website/controller_choose.html')


def ap_list(request):
    if request.method == "GET":
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
    if request.method == "POST":
        ip_list = request.POST.getlist("ip")
        for ap in ip_list:
            ap_to_migration.append(ap)
        return redirect('ap_migration')


def ap_migration(request):
    wlc_name = "EMEA-WLC"
    wlc_ip = "10.1.1.1"
    config = open('config_for_wlc.txt', 'w+')
    print(ap_to_migration)
    for ap in ap_to_migration:
        config.write("config ap primary-base {} {} {} \n ".format(wlc_name, ap, wlc_ip))
    config.close()
    ap_to_migration.clear()
    return HttpResponse("Udało się ?")