from django.shortcuts import render

# Create your views here.
def cal_view(request):
    result = None
    if request.method == "POST":
        num1 = float(request.POST.get("num1", 0))
        num2 = float(request.POST.get("num2", 0))
        
        operation = request.POST.get("operation", "")
        if operation == "add":
            result = num1 + num2
        elif operation == "substraction":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error division by zero")

    
    return render(request, "calc/index.html", {"result" : result})

