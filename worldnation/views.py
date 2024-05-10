from django.shortcuts import render, redirect, get_object_or_404

from .models import Nations


# Create your views here.
def worldNations(request):
    if request.method == 'GET':
        nations = Nations.objects.all()
        return render(request, 'worldnations.html', {'nations': nations})


def worldnation_details(request, pk):
    nation = Nations.objects.get(id=pk)
    return render(request, 'nation.html', {'nation': nation})


def worldnation_create(request):
    try:
        if request.method == 'POST':
            nation = request.POST.get('nation')
            country = request.POST.get('country')
            numb = request.POST.get('numb')
            flag = request.FILES.get('flag')
            new_row = Nations(nation=nation, country=country, numb=numb, flag=flag)
            new_row.save()
            redirect('worldNation/')
        else:
            return render(request, 'worldnations.html')
    except Exception as e:
        print(e)


def worldnation_edit(request, pk):
    current_nation = get_object_or_404(Nations, id=pk)
    try:
        if request.method == 'POST':
            current_nation.nation = request.POST.get('nation')
            current_nation.country = request.POST.get('country')
            current_nation.numb = request.POST.get('numb')
            flag = request.FILES.get('flag')
            redirect('worldNation/')
            if flag:
                current_nation.flag = flag
            current_nation.save()
            return redirect('nation_info', pk=current_nation.pk)
        else:
            return render(request, 'edit_nation.html', {'nation_e': current_nation.pk})
    except Exception as e:
        print(e)


def del_nation_col(request, pk):
    del_nation = get_object_or_404(Nations, pk=pk)
    try:
        if request.method == 'POST':
            del_nation.delete()
            redirect('/worldNation')
    except Exception as e:
        print(e)
