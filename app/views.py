from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from django.http import Http404
from app.models.client import Client
from app.models.cm_license import CmLicense
from app.forms import CmLicenseForm

def home(request):
    """
    Home page view that displays the main landing page.
    Authentication is not required to view this page.
    """
    return render(request, 'home.html')

@login_required
def dashboard(request):
    """
    Dashboard view that requires authentication.
    Redirects to login page if user is not authenticated.
    """
    return render(request, 'dashboard.html')

def access_denied(request):
    """
    403 error page view.
    Displayed when a user tries to access a restricted page.
    """
    return render(request, '403.html', status=403)

def logout_user(request):
    logout(request)
    return redirect(
        "home",
    )

@login_required
def clients(request):
    """
    View that displays all clients in the database.
    """
    clients_list = Client.objects.all().order_by('name')
    return render(request, 'clients.html', {'clients': clients_list})

@login_required
def client_detail(request, client_id):
    """
    View that displays details for a specific client and their licenses.
    """
    client = get_object_or_404(Client, id=client_id)
    licenses = CmLicense.objects.filter(client=client)
    
    return render(request, 'client_detail.html', {
        'client': client,
        'licenses': licenses
    })

@login_required
def add_license(request, client_id):
    """
    View that handles adding a new CM license for a client.
    """
    client = get_object_or_404(Client, id=client_id)
    
    if request.method == 'POST':
        form = CmLicenseForm(request.POST)
        if form.is_valid():
            license = form.save(commit=False)
            license.client = client
            license.save()
            
            messages.success(request, f"License added successfully for {client.name}")
            return redirect('client_detail', client_id=client.id)
        else:
            messages.error(request, "Error adding license. Please check the form.")
    
    # If not POST or form is invalid, redirect back to client detail page
    return redirect('client_detail', client_id=client.id)

@login_required
def edit_license(request, client_id, license_id):
    """
    View that handles editing an existing CM license.
    """
    client = get_object_or_404(Client, id=client_id)
    license = get_object_or_404(CmLicense, id=license_id, client=client)
    
    if request.method == 'POST':
        form = CmLicenseForm(request.POST, instance=license)
        if form.is_valid():
            form.save()
            messages.success(request, "License updated successfully")
        else:
            messages.error(request, "Error updating license. Please check the form.")
    
    return redirect('client_detail', client_id=client.id)

@login_required
def delete_license(request, client_id, license_id):
    """
    View that handles deleting a CM license.
    """
    client = get_object_or_404(Client, id=client_id)
    license = get_object_or_404(CmLicense, id=license_id, client=client)
    
    if request.method == 'POST':
        license.delete()
        messages.success(request, "License deleted successfully")
    
    return redirect('client_detail', client_id=client.id)
