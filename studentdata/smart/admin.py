from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city', 'date_of_birth', 'course', 'email', 'phone_number', 'department', 'year_of_study')
    search_fields = ('name', 'city', 'course', 'department')
    list_filter = ('city', 'department', 'year_of_study')
    actions = ['print_report', 'print_form']

    def print_report(self, request, queryset):
        # Implement the logic to print reports here
        pass

    def print_form(self, request, queryset):
        # Implement the logic to print forms here
        pass

    print_report.short_description = "Print Report"
    print_form.short_description = "Print Form"

admin.site.register(Student, StudentAdmin)
