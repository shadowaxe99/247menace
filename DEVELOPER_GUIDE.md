# Loco Project Developer Guide

This document provides additional information for developers working on the Loco project.

## Code Structure

The main script is `main.py`. This script reads emails, schedules calls, and sends confirmation emails.

The `calendar_integration.py` and `email_integration.py` modules handle interaction with the Google Calendar and Gmail APIs, respectively.

The `natural_language_processing.py` module processes the emails to extract the call details.

## Development Environment

You need Python 3.6 or later to run the scripts. You also need several Python libraries, which you can install with pip:

```
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

You also need to set up a Google Cloud project, enable the Gmail and Calendar APIs, and create credentials. Download the credentials file (a JSON file) from the Google Cloud Console and save it as `credentials.json` in the project directory.

## Testing

There are currently no automated tests for this project. To test the project, you can run the `main.py` script and check that it correctly schedules calls based on the emails in the specified email account.

## Contributing

If you want to contribute to this project, please create a fork of the repository, make your changes, and submit a pull request. Please ensure that your code follows the existing style and structure.

## Future Work

There are many ways this project could be improved. For example, it could be expanded to handle different time zones and check for conflicts with existing events. It could also be made more robust by adding error handling and dealing with edge cases. Additionally, it could be expanded to handle other types of scheduling requests, not just calls.