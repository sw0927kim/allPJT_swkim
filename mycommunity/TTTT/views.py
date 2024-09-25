from django.shortcuts import render
from .tasks import run_background_tasks  # 백그라운드 작업을 불러오기
from django.db.models import Q
from .models import Employee  # Employee 모델을 import

def TTTT_home(request):
    # 백그라운드에서 데이터 업데이트 시작
    run_background_tasks()  # 여러 백그라운드 작업을 실행

    # 페이지 로드 시 기본적인 직원 정보 조회 및 렌더링
    employees = Employee.objects.all()
    return render(request, 'TTTT/TTTT_home.html', {'employees': employees})


def search_results(request):
    # 검색 조건 가져오기
    name = request.GET.get('name', '')
    age = request.GET.get('age', '')
    gender = request.GET.get('gender', '')
    position = request.GET.get('position', '')
    email = request.GET.get('email', '')

    # 필터링 조건 구성
    query = Q()  # 빈 쿼리 객체

    # 조건이 있을 경우 쿼리에 추가
    if name:
        query &= Q(name__icontains=name)
    if age and age.isdigit():
        query &= Q(age=int(age))
    if gender:
        query &= Q(gender=gender)
    if position:
        query &= Q(position__icontains=position)
    if email:
        query &= Q(email__icontains=email)

   # 검색 조건이 없으면 처음 10개 데이터를 가져옴
    if not any([name, age, gender, position, email]):
        employees = Employee.objects.all()[:10]  # 처음 10개의 데이터만 가져옴
    else:
        # 필터링된 데이터 가져오기
        employees = Employee.objects.filter(query)

    return render(request, 'TTTT/TTTT_home.html', {'data': employees})