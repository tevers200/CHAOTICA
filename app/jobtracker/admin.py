from django.contrib import admin
from .models import *
from django.apps import apps
from import_export import resources
from import_export.admin import ImportExportModelAdmin

###########################
## This part makes sure we have the default groups configured...

class PhasesInline(admin.StackedInline):
    model = Phase
    extra = 1
    min_num = 0

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    inlines = [PhasesInline]


class OrganisationalUnitMemberInline(admin.TabularInline):
    model = OrganisationalUnitMember
    extra = 1

@admin.register(OrganisationalUnit)
class OrganisationalUnitAdmin(admin.ModelAdmin):
    inlines = [OrganisationalUnitMemberInline]


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1

@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    inlines = [SkillInline]

admin.site.register(Service)
admin.site.register(TimeSlot)
admin.site.register(WorkflowTasks)
admin.site.register(BillingCode)
admin.site.register(Feedback)
admin.site.register(Certification)
admin.site.register(UserCertification)

#### Skill
class SkillResource(resources.ModelResource):
    class Meta:
        model = Skill
        
class SkillAdmin(ImportExportModelAdmin):
    resource_classes = [SkillResource]

admin.site.register(Skill, SkillAdmin)


#### Client
class ClientResource(resources.ModelResource):
    class Meta:
        model = Client
        
class ClientAdmin(ImportExportModelAdmin):
    resource_classes = [ClientResource]

admin.site.register(Client, ClientAdmin)



@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "company"]



@admin.register(UserSkill)
class UserSkillAdmin(admin.ModelAdmin):
    list_display = ["skill", "user", "rating", "last_updated_on"]
