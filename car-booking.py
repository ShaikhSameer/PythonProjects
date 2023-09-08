import pytz
from datetime import datetime

# Initialize the booking storage list
booking_storage = []

def add_tz(date_str, timezone):

    naive_datetime = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    tz = pytz.timezone(timezone)
    tz_aware_datetime = tz.localize(naive_datetime)
    return tz_aware_datetime

def convert_tz(datetime_obj, from_timezone, to_timezone):

    from_tz = pytz.timezone(from_timezone)
    to_tz = pytz.timezone(to_timezone)
    
    converted_datetime = datetime_obj.astimezone(to_tz)
    return converted_datetime

def is_slot_available(start_date, end_date):
    
    for booking in booking_storage:
        if start_date >= booking["start_date"] and start_date < booking["end_date"]:
            return False
        if end_date > booking["start_date"] and end_date <= booking["end_date"]:
            return False
    return True

def book_the_car(car_model, start_date, end_date):
    
    if is_slot_available(start_date, end_date):
        booking_storage.append({
            "car_model": car_model,
            "start_date": start_date,
            "end_date": end_date
        })
        return True
    else:
        return False

# Test the program with user inputs
for _ in range(5):
    car_model = input("Enter car model (e.g., Corolla, Civic): ")
    start_date_str = input("Enter start date (YYYY-MM-DD HH:MM:SS): ")
    end_date_str = input("Enter end date (YYYY-MM-DD HH:MM:SS): ")
    timezone = input("Enter timezone (e.g., Asia/Karachi): ")

    start_date = add_tz(start_date_str, timezone)
    end_date = add_tz(end_date_str, timezone)

    if book_the_car(car_model, start_date, end_date):
        print("Booking successful!")
    else:
        print("Booking failed. The slot is not available.")

# Print the booking storage
print("Booking Storage:")
for booking in booking_storage:
    print(booking)
