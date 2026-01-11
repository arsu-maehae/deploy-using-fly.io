from django.shortcuts import render
from lists.models import Item
from django.shortcuts import render, redirect  # <--- เพิ่ม redirect

def home_page(request):
    if request.method == "POST":
        Item.objects.create(text=request.POST["item_text"])
        # return redirect("/")
        return redirect("/lists/the-only-list-in-the-world/")
        

    # ดึงข้อมูลทั้งหมดออกมา
    # items = Item.objects.all()
    # ส่งไปที่ template ในชื่อ 'items'
    # return render(request, "home.html", {"items": items})
    return render(request, "home.html")

def about_page(request):
    return render(request, 'about.html')

def view_list(request):
    items = Item.objects.all()
    return render(request, "list.html", {"items": items})