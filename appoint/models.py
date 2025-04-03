from django.db import models

# Create your models here.


class Appointment(models.Model):
    """
    생성된 달력의 코드를 저장하는 모델
    """
    calendar_code = models.CharField(max_length=50, verbose_name="달력 코드")
   


class Dates_info(models.Model):
    """
    사용자가 선택한 날짜를 저장하는 모델
    """
    user = models.CharField(max_length=50, verbose_name="사용자")
    calendar_code = models.ForeignKey(Appointment, on_delete=models.CASCADE, verbose_name="달력 코드")
    available_dates = models.JSONField(default=list)  # ✅ 리스트 저장 가능
    unavailable_dates = models.JSONField(default=list)  # ✅ 리스트 저장 가능
    


class Selected_date(models.Model):
    """
    사용자가 선택한 날짜를 저장하는 모델
    """
    calendar_code = models.ForeignKey(Appointment, on_delete=models.CASCADE, verbose_name="달력 코드")
    selected_dates = models.CharField(max_length=50, verbose_name="선택한 날짜")



class Feedback(models.Model):
    
    message = models.TextField(verbose_name="피드백 내용")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.message}"