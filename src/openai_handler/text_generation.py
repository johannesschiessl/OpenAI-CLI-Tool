from openai import OpenAI
import datetime

def get_current_date():
    return datetime.datetime.now().strftime("%Y-%m-%d")
