import datetime

def get_current_date_time():
    """
    Returns the current date and time as a formatted string.
    """
    current_date_time: str = datetime.datetime.now()
    formatted_date_time: str = current_date_time.strftime("%Y-%m-%d%H:%M:%S.%f")[:-3]
    return formatted_date_time