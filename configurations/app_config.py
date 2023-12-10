from datetime import datetime
import random


class AppConfig:
    first_name = "Sainadh"
    last_name = "Reddy"
    email_id = "sainadhreddy@gmail.com"
    password = "123456"
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    random_email_id = "sainadhreddy_" + time_stamp + "@gmail.com"
    random_telephone_number = '9' + ''.join(str(random.randint(0, 9)) for _ in range(9))