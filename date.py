import datetime

def time_ge():

    # Get the current local time
    current_time = datetime.datetime.now()

    # Format the local time as a string
    formatted_time = current_time.strftime("%H:%M:%S")

    # Print the formatted local time
    print(formatted_time)
