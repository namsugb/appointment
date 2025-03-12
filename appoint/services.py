
import os
import django


from .models import Appointment, Dates_info



        
def calculate_possible_date(calendar_code):
    """
    입력받은 달력 코드에 대한 가능한 날짜를 계산하는 함수
    """
    appointment_instance = Appointment.objects.get(calendar_code=calendar_code)
    calendar_code = appointment_instance.id
    dates_infos = Dates_info.objects.filter(calendar_code=calendar_code)

    possible_date = []
    impossible_date = []

    for dates_info in dates_infos:
        possible_date.append(dates_info.available_dates)
        impossible_date.append(dates_info.unavailable_dates)

    print(f"✅ 가능한 날짜: {possible_date}")
    print(f"❌ 불가능한 날짜: {impossible_date}")

    # 리스트 평탄화(flatten)
    flattened_possible_date = []
    flattend_impossible_date = []

    for date in possible_date:
        flattened_possible_date.extend(date)
        
    for date in impossible_date:
        flattend_impossible_date.extend(date)

    print(f"✅ 가능한 날짜: {possible_date}")
    print(f"❌ 불가능한 날짜: {impossible_date}")

    selected_date = list(set(flattened_possible_date) - set(flattend_impossible_date))

    print(f"✅ 선택된: {selected_date}")

    
    return selected_date
