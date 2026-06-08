from django.contrib import admin
from .models import chaiVarity, chaiReview, store, chaiCerificate

# Register your models here.

class ChaiReviewInline(admin.TabularInline):
    model = chaiReview
    fk_name='chai'
    extra = 2

class ChaiVarietyAdmin(admin.ModelAdmin):
    list_display= ('name', 'type', 'date_added')
    inlines= [ChaiReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display=('name', 'location')
    filter_horizontal=('chai_varieties',)

class ChaiCertificateInline(admin.ModelAdmin):
    list_display=('chai','certificateNum')

admin.site.register(chaiVarity, ChaiVarietyAdmin)
admin.site.register(store, StoreAdmin)
admin.site.register(chaiCerificate, ChaiCertificateInline)