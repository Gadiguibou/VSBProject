import requests
import datetime
import math
import xmltodict
import json

def get_date():
    # annoying function that needs to be entered for the time to be validated. Hopefully this does not change,
    # if this app crashes due to requests look for nWindow() in the vsb source code and copy that exactly here.
    array = ["&t=", "&e="]
    time = int(datetime.datetime.utcnow().timestamp()) * 1000
    # x 1000 to convert from Python to Javascript datetime object
    updated_time = (math.floor(time / 60000)) % 1000

    e = (updated_time % 3) + (updated_time % 19) + (updated_time % 42)
    e = str(e)
    updated_time = str(updated_time)
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
    print(final_url)
    r = requests.get(final_url)
    if r.status_code == 200:
        d = xmltodict.parse(r.text)
        json_object = json.dumps(d, indent = 4)
        return json_object
    else:
        return "fail"


def formated (class_name,term ):
    JSON = json.loads(get_class_JSON(class_name,term))
    r_string = " Class formate \n\n Name:" + "\n" + str(JSON["addcourse"]["classdata"]["course"]["@key"]) + "\n" + "des:" + str(JSON["addcourse"]["classdata"]["course"]["@desc"])
    return r_string

