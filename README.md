python manage.py add_data - Наполнить БД.

Эндпоинты :

1. http://127.0.0.1:8000/api/client/workerList/ - Список рабочих.
2. http://127.0.0.1:8000/api/client/workerList/?location={location.id} - Выбор рабочего по локации.
3. http://127.0.0.1:8000/api/client/locationsList/ - список локаций.
4. http://127.0.0.1:8000/api/worker/AppointmentList/ - список заказов.
5. http://127.0.0.1:8000/api/worker/AppointmentList/?worker={worker.id}&date={year-month-day} - список заказов по рабочему и по дате.
6. http://127.0.0.1:8000/api/client/SchelduleList/?work_day={day}&worker={worker.id} - расписание для контретного рабочего по дню недели

http://127.0.0.1:8000/cms/ - wagtail admin panel
