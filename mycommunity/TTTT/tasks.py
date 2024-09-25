import threading
import pandas as pd
from .models import Employee  # 모델 불러오기

# 각 데이터프레임 예시
employee_data = {
    "Name": ["John Doe", "Jane Smith", "Michael Johnson", "Alice Brown","김성원"],
    "Age": [28, 32, 35, 30,34],
    "Email": ["john.doe@example.com", "jane.smith@example.com", "michael.j@example.com", "alice.b@example.com","alice.b@example.com"],
    "Gender": ["Male", "Female", "Male", "Female","Male"],
    "Position": ["Developer", "Designer", "Manager", "HR","HR"]
}
df_employee = pd.DataFrame(employee_data)

# 백그라운드에서 실행할 함수 정의 (예: 직원 데이터 업데이트)
def update_employee_database():
    # 기존 데이터 삭제
    Employee.objects.all().delete()

    # Django ORM 객체 리스트 생성
    employee_list = [
        Employee(
            name=row['Name'],
            age=row['Age'],
            email=row['Email'],
            gender=row['Gender'],
            position=row['Position']
        )
        for _, row in df_employee.iterrows()
    ]

    # bulk_create로 한 번에 삽입
    Employee.objects.bulk_create(employee_list)

# 다른 데이터프레임 업데이트 함수도 이곳에 추가 가능
# 예시로 추가할 다른 데이터프레임 및 관련 업데이트 함수들

def update_another_database():
    # 여기에 다른 데이터프레임 업데이트 작업
    pass

# 백그라운드 작업 실행 함수
def run_background_tasks():
    # 백그라운드 스레드 시작
    threading.Thread(target=update_employee_database).start()
    threading.Thread(target=update_another_database).start()  # 다른 업데이트 작업
