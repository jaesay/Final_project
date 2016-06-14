from django.contrib import admin
from businesses.models import Business, Goal, Worker, Resource, Finance, Location, Material, Goal_score, Finance_score, Room

# Register your models here.
admin.site.register(Business)
admin.site.register(Goal)
admin.site.register(Worker)
admin.site.register(Resource)
admin.site.register(Finance)
admin.site.register(Location)
admin.site.register(Material)
admin.site.register(Goal_score)
admin.site.register(Finance_score)
admin.site.register(Room)