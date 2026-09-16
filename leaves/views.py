from django.shortcuts import render

# Create your views here.
def apply_leaves(request):
    return render(request, 'leaves/leaves_approval.html')
