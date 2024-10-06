# Instalación

- Clonar el repo
```sh
git clone https://github.com/gabrieldeluca88/ProyectoFinal.git
```
- Crear el entorno virtual 
```sh 
py -m venv myvenv
```
- Iniciar el entorno virtual 
```sh
.\myvenv/Scripts/activate
```
- Actualizar pip
```sh
python -m pip install --upgrade pip
```
- Descargar dependencias
```sh
pip install -r requirements.txt
```
- Crear la base de datos 
```sh
py manage.py migrate
```
- Crear un super usuario 
```sh
py manage.py createsuperuser
```
- Levantar el server 
```sh
py manage.py runserver
```

- Listo!

usuario: admin
pass: admin123456
