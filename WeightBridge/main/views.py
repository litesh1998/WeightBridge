from django.http.response import HttpResponseForbidden, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import VehicleType, Reading
from .forms import FirstReadingForm, SecondReading
from django.template.loader import render_to_string
import weasyprint
# Create your views here.

def Home(request):
    return render(request, 'main/reading/home.html')

def firstReading(request):
    if request.method=='POST':
        form=FirstReadingForm(request.POST)
        form.save(commit=False)
        if form.is_valid():
            reading=form.save()
            
            return redirect('main:printInvoice', pk=reading.id)
            
    else:
        form=FirstReadingForm()

    return render(request, 'main/reading/firstReading.html', context={
        'form': form
        })

def secondReading(request):
    pk=int(request.GET.get('pk'))
    reading= get_object_or_404(Reading, pk=pk)
    if reading.weight2:
        return HttpResponseForbidden("Second Weight Already Excists")
    form=SecondReading(instance=reading)
    
    if request.method=='POST':
        form=SecondReading(request.POST, instance=reading)
        form.save(commit=False)
        if form.is_valid():
            form.save()
            return redirect('main:printInvoice', pk=pk)

    return render(request, 'main/reading/secondReadin.html', {'form':form, 'reading': reading})

def printInvoice(request, pk):
    reading = get_object_or_404(Reading, id=pk)
    html = render_to_string('main/invoice/invoice.html',
    {'reading': reading})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename=order_{reading.id}.pdf'
    weasyprint.HTML(string=html).write_pdf(response
    )
    return response
        


