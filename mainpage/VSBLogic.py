import requests
import datetime
import math


def get_date():
    # annoying function that needs to be entered for the time to be validated. Hopefully this does not change,
    # if this app crashes due to requests look for nWindow() in the vsb source code and copy that exactly here.
    array = ["&t=", "&e="]
    time = int(datetime.datetime.utcnow().timestamp())
    updated_time = (math.floor(time / 60000)) % 1000
    updated_time = str(updated_time)
    e = (time % 3) + (time % 19) + (time % 42)
    e = str(e)
    return array[0] + updated_time + array[1] + e


def get_class_JSON(class_name,term):
    term = "202109"
    class_name = "COMP-250"
    url_base = "https://vsb.mcgill.ca/vsb/getclassdata.jsp"
    url_term = "?term=" + term
    url_course = "&course_1_0=" + class_name
    url_useless = "&rq_1_0=null&nouser=1"
    url_date = get_date()
    final_url = url_base + url_term + url_course + url_useless + url_date
    return requests.get(final_url).json()






