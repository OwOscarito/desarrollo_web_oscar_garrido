# desarrollo_web_oscar_garrido
[http](https://github.com/OwOscarito/desarrollo_web_oscar_garrido/tree/Tarea_2o)

## Base de datos
Para correr el servidor web se necesita una base de datos mysql corriendo de forma local con:
- Nombre = ```tarea2```
- Usuario = ```cc5002```
- Contraseña = ```programacionweb```
- Puerto: = ```3306```

Se puede ejecutar en un contenedor con el archivo ```compose.yaml```:
```sh
docker compose up -d
```

Luego para inicializar las tablas de la base de datos y los datos de region-comuna:
```sh
python app/database/manage.py init
```

Ademas de pueden eliminar todas la base de datos:
```sh
python app/database/manage.py drop
```

## Correr Servidor web 
Crear venv:
```sh
python -m venv .venv
```

Cargar venv:
```sh
source .venv/Scripts/activate #Linux/MacOS
```
```ps1
./.venv/Scripts/activate #Windows
```

Instalar dependencias:
```sh
pip install -r requirements.txt
```

Correr la aplicacion con:
```sh
flask run
```