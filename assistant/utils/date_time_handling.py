import datetime

def get_current_date_time():
    current_date_time = datetime.datetime.now()
    formatted_date_time = current_date_time.strftime("%Y-%m-%d%H:%M:%S.%f")[:-3]
    return formatted_date_time