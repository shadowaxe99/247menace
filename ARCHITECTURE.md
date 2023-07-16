# Loco Project Architecture

This document describes the architecture of the Loco project.

## Overview

The Loco project is an email-based assistant that can schedule calls. It uses the Google Calendar and Gmail APIs to interact with a user's calendar and email.

## Components

The project consists of several components:

- **Email Integration**: This component reads emails from a specified account, looking for emails that request a call.

- **Natural Language Processing**: This component processes the emails to extract the date and time of the call and the participants.

- **Calendar Integration**: This component interacts with Google Calendar to schedule the call.

- **Email Sending**: This component sends a confirmation email once the call has been scheduled.

## Data Flow

1. The Email Integration component reads an email that requests a call.

2. The Natural Language Processing component processes the email to extract the call details.

3. The Calendar Integration component schedules the call in Google Calendar.

4. The Email Sending component sends a confirmation email.

## Limitations and Future Work

This is a basic implementation and has many limitations. For example, it doesn't handle different time zones, check for conflicts with existing events, or handle errors and edge cases. Future work could involve expanding the project to handle these cases and adding more features, such as support for different types of scheduling requests and integration with other calendar and email services.