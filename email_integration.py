import datetime
import google.auth
from googleapiclient.discovery import build

# Load credentials and create a service
credentials, project = google.auth.default()
service = build('calendar', 'v3', credentials=credentials)

# Define the event
event = {
  'summary': 'Call with John',
  'start': {
    'dateTime': '2022-01-01T09:00:00-07:00',
    'timeZone': 'America/Los_Angeles',
  },
  'end': {
    'dateTime': '2022-01-01T10:00:00-07:00',
    'timeZone': 'America/Los_Angeles',
  },
}

# Add the event to the calendar
calendar_id = 'primary'
event = service.events().insert(calendarId=calendar_id, body=event).execute()

print(f'Event created: {event["htmlLink"]}')