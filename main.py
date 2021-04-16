# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright (c) 2020 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at
               https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""

__author__ = "Eda Akturk <eakturk@cisco.com>"
__copyright__ = "Copyright (c) 2020 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"

import requests


API_KEY = ' '

org_id = ''

on = 'true'
off = 'false'

# create a list for camera serial ids
serial_id_list = []


def mv_audio(serial_id, audio_setting):
    """
    This function will change the audio recording settings to {audio_setting} in the meraki dashboard for the mv camera
    with the {serial_id}
    :param: serial_id: the serial id for the meraki mv camera
    :param: audio_setting: 'true' to turn on audio recording, 'false' to turn off audio recording
    :return: api response status code
    """
    url = f"https://api.meraki.com/api/v1/devices/{serial_id}/camera/qualityAndRetention"

    payload = f'''{{
        "audioRecordingEnabled": {audio_setting}
    }}'''

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": API_KEY
    }

    response = requests.request('PUT', url, headers=headers, data=payload)

    if response.status_code == 403:
        print(f'Camera-serial id:{serial_id} audio recording have been changed to: {audio_setting}')

    return response.status_code

def get_camera_ids(org_id):
    """
    This function will add all the camera serial id's to a list belonging to the organization with the {org_id}
    :param: org_id: the organization id
    :return: list of camera serial id's
    """
    camera_list = []

    url = f"https://api.meraki.com/api/v1/organizations/{org_id}/devices"
    payload = None
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": API_KEY
    }
    response = requests.request('GET', url, headers=headers, data=payload)
    for device in response.json():
        if 'MV' in device['model']:
            camera_list.append(device['serial'])

    return camera_list


if __name__ == '__main__':

    # for all the serial ids in the list turns the audio settings to off
    for serial_id in serial_id_list:
        mv_audio(serial_id, off)
