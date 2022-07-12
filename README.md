Docker: 
1. mkdir PROJECT && cd PROJECT
2. git init
3. git clone https://github.com/Nonzeq/REACT_DJANGO.git
4. cd REACT_DJANGO
5. docker-compose build
6. docker-compose up -d
7. http://localhost:3000/

docker stop $(docker ps -a -q) : for stop all containers

docker rm $(docker ps -a -f status=exited -q) : for delete all containers with status exist

docker system prune -a : for delete all images

Эндпоинты :

1. http://127.0.0.1:8000/api/client/workerList/ - список рабочих.
2. http://127.0.0.1:8000/api/client/AddAppointment/ - добавление записи
3. http://127.0.0.1:8000/api/client/locationsList/ - список локаций.
4. http://127.0.0.1:8000/api/worker/AppointmentList/ - список заказов.
5. http://127.0.0.1:8000/api/worker/AppointmentList/?worker={worker.id}&date={year-month-day} - список заказов по рабочему и по дате.
6. http://127.0.0.1:8000/api/client/SchelduleList/?work_day={day}&worker={worker.id} - расписание для контретного рабочего по дню недели

http://127.0.0.1:8000/cms/ - wagtail admin panel
