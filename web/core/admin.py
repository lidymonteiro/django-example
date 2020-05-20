import csv
from django.contrib import admin
from .models import Extraction, DataExtraction


def read_data_csv(path):
    with open(path) as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        csv_data = [line for line in reader]
    return csv_data


def spider(modeladmin, request, queryset):
    for extraction in queryset:
        csv_file_path = extraction.lawsuits.path
        dataset = read_data_csv(csv_file_path)
        for data in dataset:
            DataExtraction.objects.create(dataset=data)


spider.short_description = "Apply Spider"


class ExtractionAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_date', 'total_lawsuits', 'found']
    actions = [spider]


admin.site.register(Extraction, ExtractionAdmin)
admin.site.register(DataExtraction)
