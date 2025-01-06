from django.shortcuts import render
from django.http import HttpResponse


def display(request):
    return HttpResponse("HELLO DJANGO CODE!!!")


def functions(request):
    a = 5
    b = 10
    result = a + b
    return HttpResponse(f"the sum {a} and {b} is {result} ") 


def reverse_string(request):
    text = request.GET.get("text", )
    reversed_text = text[::-1]
    return HttpResponse (f"The orginal string {text} and the revesed_string {reversed_text}")
# output :  http://127.0.0.1:8000/reverse/?text=sum


def name(request):
    name_text = request.GET.get("name_text", "")
    if name_text == "Anusha":
        return HttpResponse ("True")
    else:
        return HttpResponse ("False")
    
def add_number(request):
    if request.method == "POST":
        a = int(request.POST.get("a", 0))
        b = int(request.POST.get("b", 0))
        # return HttpResponse (f"the sum of {a} and {b} and {a + b}")
        return HttpResponse(f"The sum of {a} and {b} is {a + b}")

    
    elif request.method == "GET":
        a = int(request.GET.get("a", 0))
        b = int(request.GET.get("b", 0))
        return HttpResponse (f"{a}, {b} sum is {a + b}")
    
    return HttpResponse(f"send get and post request paramaters of a and b")


def numbers(request):
    if request.method == "GET":
        number = int(request.GET.get("number", 0))
    result = ""
    for i in range(number):
        if i % 2 == 0:
            result += (f"its even number {i}<br>")
        else:
            result += (f"its odd number {i}<br>")
        
    return HttpResponse (f"the result : {result}")


