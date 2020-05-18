from django.contrib import admin
from .models import Extraction, DataExtraction
import csv


def read_data_csv(path):
    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = []
        for row in reader:
            data.append(dict(row))
        return data


# action que converte para JSON. Qual a melhor maneira de salvar no campo JSONField de DataExtraction?
def spider(modeladmin, request, queryset):
    for extraction in queryset:
        csv_file_path = extraction.lawsuits.path
        dataset = read_data_csv(csv_file_path)
    print(dataset)


spider.short_description = "Apply Spider"


class ExtractionAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_date', 'total_lawsuits', 'found']
    actions = [spider]


admin.site.register(Extraction, ExtractionAdmin)
admin.site.register(DataExtraction)
