from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from rest_framework import response
from django.http import JsonResponse
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Appointment, Dates_info
from .services import calculate_possible_date


# Create your views here.
def main(request):
    return render(request, 'main.html')




class CalculateDateAPIView(APIView):

    def post(self, request, *args, **kwargs):
        """
        사용자가 선택한 날짜를 서버에 저장하고 가능한 약속 날짜를 반환하는 API
        """
        try:
            data = request.data  # ✅ DRF에서는 request.data를 사용 (자동 JSON 변환)
            available_dates = data.get("available", {})
            unavailable_dates = data.get("unavailable", {})
            calendar_code = data.get("calendarCode", "")
            user = data.get("user", "")

            print(f"✅ 받은 데이터: {data}")
            print(f"📅 달력 코드: {calendar_code}")
            print(f"✅ 받은 날짜 데이터: {available_dates}, {unavailable_dates}")

            # 저장 로직
            if not Appointment.objects.filter(calendar_code=calendar_code).exists():
                Appointment.objects.create(calendar_code=calendar_code)

            dates_info, created = Dates_info.objects.get_or_create(
                user=user,
                calendar_code=Appointment.objects.get(calendar_code=calendar_code),
                defaults={
                    'available_dates': available_dates,
                    'unavailable_dates': unavailable_dates
                }
            )

            # 이미 존재하는 경우, 날짜 정보 업데이트
            if not created:
                dates_info.available_dates = available_dates
                dates_info.unavailable_dates = unavailable_dates
                dates_info.save()
            


            # 약속 가능한 날짜 반환
            selected_date = sorted(calculate_possible_date(calendar_code))
            print(f"✅ 선택된: {selected_date}")


            return Response({"message": "날짜 저장 완료!", "selected_dates": selected_date}, status=status.HTTP_200_OK)
        

        except Exception as e:
            return Response({"error": f"서버 오류: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

    
    def get(self, request):
        """
        선택한 약속의 가능,불가능한 날짜를 반환하는 API
        """
        print("✅ GET 요청")
        calendar_code = request.GET.get("calendarCode", "")

        selected_date = sorted(calculate_possible_date(calendar_code))
        

        return Response({"message": "날짜 저장 완료!", "selected_dates": selected_date}, status=status.HTTP_200_OK)


