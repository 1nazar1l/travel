from django.shortcuts import render
from django.http import HttpResponse
from .models import Person, Category, Country, Another
  
def index(request):
    category = Another.objects.all()
    countries = Country.objects.all()
    return render(request, 'index.html', {'category': category, 'countries': countries})
 
def tours(request, name=None):
    def get_country_by_name(name):
        country = Country.objects.get(name=name)
        return country
    
    # if request.method == 'GET':
    #     # Получение name из GET-параметра
    #     name = request.GET.get('name')


    # country = get_country_by_name(name)

    # context = {
    #     'country': country
    # }
    category = Another.objects.all()
    return render(request, 'tours.html', {'category': category})
    # return render(request, 'tours.html', context)
 


def tour(request):
    return render(request, 'tour.html')

# country = Country.objects.get(id=1)
# popular = Category.objects.get(id=1)
# food = Category.objects.get(id=2)
# place = Category.objects.get(id=3)
# sea = Category.objects.get(id=4)
# mountain = Category.objects.get(id=5)

# country.category.remove()
# country.save()
# if country.category.exists():
#     print(list(country.category.all()))
# else:
#     print("Нет связанных категорий")

