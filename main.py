import calendar_integration
import nlp_processing
import action_executor
import daily_inspiration
import utils
import sick_mode
import family_mode
import leave_message
import get_message
import schedule_reminder
import workout_reminder
import ai_agent


def main():
    # Authenticate with Google Calendar API and Twilio API
    calendar_integration.authenticate()
    ai_agent.sendEmail()
    
    # Fetch upcoming events
    events = calendar_integration.get_upcoming_events()
    
    # Process each event
    for event in events:
        # Extract the intent and the necessary data from the event
        intent, data = nlp_processing.process_event(event)
        
        # Execute the action based on the intent and the data
        action_executor.execute_action(intent, data)
    
    # Send daily inspiration
    daily_inspiration.send_daily_inspiration()
    
    # Start sick mode if necessary
    if utils.is_user_sick():
        sick_mode.start_sick_mode()

    # Provide an inspirational quote every day
    daily_inspiration.send_daily_inspiration()
    
    # Handle family messages
    family_mode.handle_family_message()

    # Leave a message
    leave_message.leave_message()

    # Get a message
    get_message.get_message()

    # Schedule a reminder
    schedule_reminder.schedule_reminder()

    # Start workout mode if necessary
    if utils.is_workout_time():
        workout_reminder.start_workout_mode()
    
    # Start the AI agent
    ai_agent.start_ai_agent()

    # Transcribe audio recordings into text
    whisper_asr.transcribe_audio()
    
    # Create Zoom meetings
    zoom_integration.create_zoom_meeting()
    
    # Cancel events and email contacts when you're sick
    sick_mode.start_sick_mode()


if __name__ == '__main__':
    main()
