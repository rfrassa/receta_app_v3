@echo off
echo Iniciando el proyecto Django...
cd /d D:\Programacion\Python\Django\djangoproject\recetas_app_v3
call D:\Programacion\Python\Django\djangoproject\recetas_app_v3\venv\Scripts\activate
python manage.py runserver 0.0.0.0:8000
pause