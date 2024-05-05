from __future__ import unicode_literals
from django.shortcuts import render
from payment.models import payment_status as paystat
import requests
import json

def shipment_details_update(uname):
    ship_dict = {}
    user = paystat.objects.filter(username = uname)
    for data in user.values():
        print(data)
        data
    ship_dict['Product Type'] = data['product_type']
    ship_dict['Product Id'] = data['product_id']
    ship_dict['Quantity'] = data['quantity']
    ship_dict['Payment Status'] = data['status']
    ship_dict['Transaction Id'] = data['id']
    ship_dict['Mobile Number'] = data['mobile']
    
    url = 'http://127.0.0.1:8001/api/v1/user/info/'
    d1 = {}
    d1["User Name"] = data['username']
    data = json.dumps(d1)
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=data, headers=headers)
    val1 = json.loads(response.content.decode('utf-8'))
    ship_dict['First Name'] = val1['data']['First Name']
    ship_dict['Last Name'] = val1['data']['Last Name']
    ship_dict['Address'] = val1['data']['Address']
    ship_dict['Email Id'] = val1['data']['Email Id']
    url = 'http://127.0.0.1:8006/api/v1/shipment/update/'
    
    data = json.dumps(ship_dict)
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=data, headers=headers)
    api_resp = json.loads(response.content.decode('utf-8'))
    return api_resp
