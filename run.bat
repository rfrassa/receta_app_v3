@echo off
echo -------------------------------------------------
echo          Iniciando RecetasApp...
echo -------------------------------------------------

REM Activar entorno virtual
call venv\Scripts\activate

REM Ejecutar el servidor de desarrollo
python manage.py runserver

pause
