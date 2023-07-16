# Loco Project

This project is an assistant that can schedule calls via email. It uses the Google Calendar and Gmail APIs to read emails, schedule calls in a calendar, and send confirmation emails.

## Setup

1. Install the required Python libraries: `pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib`

2. You need to set up a Google Cloud project, enable the Gmail and Calendar APIs, and create credentials. Download the credentials file (a JSON file) from the Google Cloud Console and save it as `credentials.json` in the project directory.

3. Run the main script: `python3 loco/main.py`

## How it works

The script reads emails from a specified email account, looking for emails that request a call. It uses natural language processing to extract the date and time of the call and the participants. It then schedules the call in Google Calendar and sends a confirmation email.

## Limitations

This is a basic implementation and has many limitations. For example, it doesn't handle different time zones, check for conflicts with existing events, or handle errors and edge cases. It's intended as a starting point and would need to be significantly expanded for a real-world application.# 247menace
# 247menace
