import PySimpleGUI as sg
from geopy.geocoders import Nominatim
import webbrowser
from twilio.rest import Client

# Twilio credentials
TWILIO_ACCOUNT_SID = 'AC051c94b636e2e33a3d4604211cfbdaca'
TWILIO_AUTH_TOKEN = '567ffed0a4ae67ca2e9aa7e812a4139f'
TWILIO_PHONE_NUMBER = '+1 650 263 8687'
FRIEND_PHONE_NUMBER = '+919359215647'

def get_current_location():
    geolocator = Nominatim(user_agent="ambulance_app")
    location = geolocator.geocode("current")
    if location:
        return location.latitude, location.longitude
    else:
        return None, None

def send_location_sms(lat, lon):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message_body = f"Emergency: Please send an ambulance to location - Latitude: {lat}, Longitude: {lon}"
    message = client.messages.create(
        body=message_body,
        from_=TWILIO_PHONE_NUMBER,
        to=FRIEND_PHONE_NUMBER
    )
    print(f"Location SMS sent to {FRIEND_PHONE_NUMBER}. Message SID: {message.sid}")

# Define the layout for the GUI
layout = [
    [sg.Button("Call Ambulance", key='-AMBULANCE-')],
    [sg.Output(size=(60, 10))]
]

# Create the GUI window
window = sg.Window('Ambulance Call Button').Layout(layout)

# Event loop to process events and interact with the GUI
while True:
    event, _ = window.Read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == '-AMBULANCE-':
        lat, lon = get_current_location()
        if lat is not None and lon is not None:
            send_location_sms(lat, lon)
            print("Ambulance called. Location sent to your friend's number.")
        else:
            print("Error: Unable to retrieve current location.")

# Close the GUI window
window.close()
