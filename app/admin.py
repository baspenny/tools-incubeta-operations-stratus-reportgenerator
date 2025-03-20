from django.contrib import admin
from app.models import Profile, Country, Client, CmLicense

# Register models
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'gender', 'github_username')
    search_fields = ('user__username', 'user__email', 'github_username')

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'iso_code')
    search_fields = ('name', 'iso_code')

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'acumatica_code', 'country')
    search_fields = ('name', 'acumatica_code')
    list_filter = ('country',)

@admin.register(CmLicense)
class CmLicenseAdmin(admin.ModelAdmin):
    list_display = ('client', 'account_id', 'profile_id', 'report_id')
    search_fields = ('client__name', 'account_id', 'profile_id', 'report_id')
    list_filter = ('client',)
