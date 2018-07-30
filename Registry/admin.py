from django.contrib import admin

# Register your models here.
from Registry.models import Project
from Registry.models import Domain
from Registry.models import StatusCode
from Registry.models import Node
from Registry.models import CDN

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    ordering = ('id',)

@admin.register(CDN)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id','cdn']
    list_display_links = ['cdn']
    ordering = ('id',)

@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display_links = ['domain']
    filter_horizontal = ['nodes',]

    list_display = ['id','domain','project','status','check','warning','cert_valid_date','cert_valid_days','cdn','detection_interval','trigger']

@admin.register(StatusCode)
class StatusCodeAdmin(admin.ModelAdmin):
    list_display = ['status_code','event_type']
    list_display_links = ['status_code','event_type']
    ordering = ('id',)


@admin.register(Node)
class NodeAdmin(admin.ModelAdmin):
    list_display = ['id','node','ip','description','online']
    list_display_links = ['node']
    ordering = ('id',)