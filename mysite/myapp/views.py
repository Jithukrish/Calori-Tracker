from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Food, Consume
# Create your views here.


# def index(request):

#     if request.method == "POST":
#         food_consumed = request.POST.get('food_consumed')
#         consume = Food.objects.get(name=food_consumed)
#         user = request.user.id
#         consume = Consume(user=user, food_consumed=consume)
#         consume.save()
#         foods = Food.objects.all()

#     else:
#         foods = Food.objects.all()
#     consumed_food = Consume.objects.filter(user=request.user.id)

#     return render(request, 'myapp/index.html', {'foods': foods, 'consumed_food': consumed_food})
def index(request):
    if request.method == "POST":
        food_consumed_name = request.POST.get('food_consumed')
        
        try:
            consume_food = Food.objects.get(name=food_consumed_name)
            
            # Create a new Consume object
            consume = Consume(user=request.user, food_consumed=consume_food)
            consume.save()
            
        except Food.DoesNotExist:
            # Handle the case when the food item does not exist
            error_message = 'Food item does not exist.'
            return render(request, 'myapp/index.html', {'foods': Food.objects.all(), 'consumed_food': Consume.objects.filter(user=request.user.id), 'error_message': error_message})

        foods = Food.objects.all()
    else:
        foods = Food.objects.all()
        
    consumed_food = Consume.objects.filter(user=request.user)

    return render(request, 'myapp/index.html', {'foods': foods, 'consumed_food': consumed_food})



# ------------------------------------------------------
def addfood(request):
    if request.method == "POST":
        # Retrieve form data
        food_name = request.POST.get('food_name')
        carbs = request.POST.get('carbs')
        protein = request.POST.get('protein')
        fats = request.POST.get('fats')
        calories = request.POST.get('calories')
        
        # Create a new Food object
        new_food = Food(
            name=food_name,
            carbs=carbs,
            protein=protein,
            fats=fats,
            calories=calories
        )
        
        new_food.save()
        
        return redirect('index')  # Replace 'success' with the name of your success URL pattern
    
    else:
        return render(request, 'myapp/addfood.html')



# ------------------------------------------------------









def delete_consume(request, id):
    consumed_food = Consume.objects.get(id=id)
    if request.method == 'POST':
        consumed_food.delete()
        return redirect('/')
    return render(request, 'myapp/delete.html')
