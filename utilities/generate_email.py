from datetime import datetime


def get_new_email():
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    random_email_id = "sainadhreddy_" + time_stamp + "@gmail.com"
    return random_email_id
