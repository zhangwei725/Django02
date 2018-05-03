from django.shortcuts import render


def test(request):
    print('views----->>>>执行了')
    return render(request, 'index.html')
