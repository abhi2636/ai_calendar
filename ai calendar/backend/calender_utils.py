from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime, timedelta

SCOPES = ['https://www.googleapis.com/auth/calendar']
SERVICE_ACCOUNT_FILE = 'backend/credentials.json'  # adjust as needed
CALENDAR_ID = 'your-calendar-id@group.calendar.google.com'  # or 'primary' if it's the main calendar

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)
service = build('calendar', 'v3', credentials=credentials)

def check_availability():
    now = datetime.utcnow().isoformat() + 'Z'
    events_result = service.events().list(
        calendarId=CALENDAR_ID, timeMin=now, maxResults=10, singleEvents=True,
        orderBy='startTime').execute()
    events = events_result.get('items', [])
    return str([e['start'] for e in events]) or "No upcoming events."

def book_appointment():
    event = {
        'summary': 'Test Appointment',
        'start': {
            'dateTime': (datetime.utcnow() + timedelta(hours=1)).isoformat() + 'Z',
            'timeZone': 'UTC',
        },
        'end': {
            'dateTime': (datetime.utcnow() + timedelta(hours=2)).isoformat() + 'Z',
            'timeZone': 'UTC',
        }
    }
    event_result = service.events().insert(calendarId=CALENDAR_ID, body=event).execute()
    return f"Appointment booked: {event_result.get('htmlLink')}"
