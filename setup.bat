@echo off
echo -------------------------------------------------
echo          Bienvenido al instalador de RecetasApp
echo -------------------------------------------------

REM Crear el entorno virtual
echo Creando entorno virtual...
python -m venv venv

REM Activar el entorno virtual
echo Activando entorno virtual...
call venv\Scripts\activate

REM Actualizar pip
echo Actualizando pip...
python -m pip install --upgrade pip

REM Instalar dependencias
echo Instalando dependencias...
pip install -r requirements.txt

echo -------------------------------------------------
echo Instalación completada.
echo Ahora podes correr: 
echo    venv\Scripts\activate
echo    python manage.py runserver
echo -------------------------------------------------
pause