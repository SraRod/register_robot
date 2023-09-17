import os
import pytz
import requests
import datetime
import subprocess

def sync_pc_time(ntp_server = 'time.apple.com'):
    if os.name == 'nt':
        try:
            subprocess.run(["w32tm", "/config", "/syncfromflags:manual", f"/manualpeerlist:{ntp_server}", "/update"])
            subprocess.run(["w32tm", "/resync", "/nowait"])
            print("System time synchronized successfully.")
        except Exception as e:
            print(f"Error synchronizing system time: {e}")

def get_server_time(url):
    try:
        response = requests.head(url, verify=False)
        server_time = response.headers['Date']
        datetime_object = datetime.datetime.strptime(server_time, '%a, %d %b %Y %H:%M:%S %Z')
        datetime_object = pytz.timezone('GMT').localize(datetime_object).astimezone(pytz.timezone('Asia/Taipei'))
        return datetime_object
    except Exception as e:
        print(f"Error retrieving server time: {e}")
        return None

def calculate_time_difference(server_time, target_time):
    target_time = datetime.datetime.strptime(target_time, '%H:%M:%S').time()
    target_time = datetime.datetime.combine(datetime.datetime.now().date(), target_time).astimezone(pytz.timezone('Asia/Taipei'))
    time_difference = target_time - server_time
    seconds_difference = time_difference.total_seconds()
    return seconds_difference