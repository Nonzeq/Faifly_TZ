
from wagtail.contrib.modeladmin.options import modeladmin_register,ModelAdmin

from .models.appointment import Appointment
from .models.location import Location
from .models.schedule import Schedule
from .models.worker import Worker





class LocationAdmin(ModelAdmin):
    model = Location
    list_display = ['id', 'nameLocation']
    list_display_links = ('id', 'nameLocation')
    search_fields = ('nameLocation',)


class WorkerAdmin(ModelAdmin):
    model = Worker
    list_display = ['id', 'full_name',]
    list_display_links = ('id', 'full_name',)
    search_fields = ('full_name',)



class ScheduleAdmin(ModelAdmin):
    model = Schedule
    list_display = ['id','worker','work_location','work_day','time_start', 'time_end' ]
    list_display_links = ('id', 'work_day',)
    search_fields = ('work_day','worker__full_name', 'work_location__nameLocation')



class ApointmentAdmin(ModelAdmin):
    model = Appointment
    list_display = ['id','apointment_worker','user', 'date','apointment_start','apointment_end',]
    list_display_links = ('id', 'apointment_start','apointment_worker')
    search_fields = ('apointment_start','apointment_end','date','apointment_worker__full_name',)




modeladmin_register(WorkerAdmin)
modeladmin_register(LocationAdmin)
modeladmin_register(ScheduleAdmin)
modeladmin_register(ApointmentAdmin)





# admin.site.register(location.Location, LocationAdmin)
# #admin.site.register(worker.Worker, WorkerAdmin)
# admin.site.register(schedule.Schedule, ScheduleAdmin)
# admin.site.register(appointment.Appointment, ApointmentAdmin)
