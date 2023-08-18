from django.shortcuts import render, get_object_or_404
from .models import Calculator
from communities.models import Community

# https://hintabout.com/finance/2022-%ED%95%9C%EA%B5%AD%EC%9E%A5%ED%95%99%EC%9E%AC%EB%8B%A8-%EC%86%8C%EB%93%9D%EB%B6%84%EC%9C%84-%EA%B5%AD%EA%B0%80%EC%9E%A5%ED%95%99%EA%B8%88-%EC%86%8C%EB%93%9D%EC%9D%B8%EC%A0%95%EC%95%A1/
# Create your views here.
def calc_view(request):
    
    return render(request, 'calc/calc-page.html')

def result_view(request):
    if request.method == 'POST':
        income_myself = int(request.POST.get('income_myself' )) * 10000
        income_fam = int(request.POST.get('income_fam' )) * 10000
        house = int(request.POST.get('house' )) * 10000
        land = int(request.POST.get('land' )) * 10000
        rental_deposit = int(request.POST.get('rental_deposit' )) * 10000
        property = int(request.POST.get('property' )) * 10000
        car = int(request.POST.get('car' )) * 10000
        finance = int(request.POST.get('finance' )) * 10000
        debt = int(request.POST.get('debt' )) * 10000


        general = ((house + land + rental_deposit + property) - 69000000 - debt) * 4.14 / 300
        finance = finance * 6.23 / 300
        car = car * 4.17 / 300

        
        result = general + finance + car + income_myself + income_fam
        result = round(result)

        if result <= 1620289:
            section = 1
        elif result > 1620289 and result <= 2700482:
            section = 2
        elif result > 2700482 and result <= 3780675:
            section = 3
        elif result > 3780675 and result <= 4860868:
            section = 4
        elif result > 4860868 and result <= 5400964:
            section = 5
        elif result > 5400964 and result <= 7021253:
            section = 6
        elif result > 7021253 and result <= 8101446:
            section = 7
        elif result > 8101446 and result <= 10801928:
            section = 8
        elif result > 10801928 and result <= 16202892:
            section = 9
        elif result > 16202892:
            section = 10
        
        if request.user.is_authenticated:
            if Calculator.objects.filter(user=request.user).exists():
                calc_res = get_object_or_404(Calculator, user=request.user)
                calc_res.delete()
                calc_res.income = result
                calc_res.section = section
                calc_res.save()
            else:
                calc = Calculator(income=result, section=section, user=request.user).save()



    post_list = Community.objects.all().filter(section=section)
    context = {
        'result' : result,
        'section' : section,
        'post_list' : post_list,
    }
    return render(request, 'calc/calc-res-page.html', context)