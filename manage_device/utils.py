import datetime


def check_time(start_day):
    start_time = datetime.datetime.strptime(start_day, '%Y-%m-%d')

    current_time = datetime.datetime.now()

    return (current_time - start_time).days


def format_email_address_for_user(email_dict):
    for key, value in email_dict.items():
        email_dict[key] = value.replace(" ", ".") + "@ef.com"

    return email_dict
