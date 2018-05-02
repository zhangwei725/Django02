from django.shortcuts import render

from form01.froms import TestForm


def test(request):
    if request.method == 'POST':
        test_from = TestForm(request.POST)
        if test_from.is_valid():
            pass
            # test_from.cleaned_data['username'] # {username:value}

    else:
        test_from = TestForm()

    return render(request, 'form01.html', {'form': test_from})
