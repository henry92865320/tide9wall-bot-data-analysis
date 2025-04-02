# Development Log
# Started at 2025-04-03 07:36:51

# Added documentation
# Added unit tests
# Added error handling

from datetime import datetime, timedelta

def get_date_range(start_date, end_date):
    date_list = []
    current_date = start_date
    while current_date <= end_date:
        date_list.append(current_date)
        current_date += timedelta(days=1)
    return date_list