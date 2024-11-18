from django.http import HttpResponse
from django.shortcuts import render
def count_characters(request):
    if request.method == "POST":
        name =request.POST.get('name','')
        char_count=name+"은 바보입니다"
        return render(request,'counter/result.html',{'name':name,'char_count':char_count})

    return render(request,'counter/form.html')
