# 🎵 Kusa, Mi Reproductor de Música Web

Este es un reproductor de música web moderno y funcional, construido con Django para el backend y HTML/CSS/JavaScript para el frontend. Permite reproducir canciones, crear y gestionar playlists, y ofrece una interfaz visual intuitiva.

## 🚀 Funcionalidades

- Reproducción de canciones locales.
- Controles: play/pausa, anterior/siguiente, aleatorio, repetir.
- Visualización de portada, título y artista.
- Crear múltiples playlists con nombres personalizados.
- Añadir y quitar canciones de playlists.
- Añadir canciones al reproductor desde el sistema.
- Interfaz moderna con reproductor fijo en el footer.
- Almacenamiento de playlists en `localStorage`.

## 📷 Vista previa

![screenshot](https://imgur.com/E9KFTM5)

## 🛠️ Tecnologías usadas

- Python 3
- Django
- HTML5
- CSS3
- JavaScript

## ▶️ Cómo ejecutar el proyecto

1. Clona este repositorio:

```bash
git clone https://github.com/jzurit4/Kusa.git
cd Kusa
```

2. Instala las dependencias:

```bash
pip install -r requirements.txt
```

3. Ejecuta las migraciones y el servidor:

```bash
python manage.py migrate
python manage.py runserver
```

4. Abre en tu navegador:

```
http://localhost:8000
```

## 📁 Páginas del proyecto

- `/` — Reproductor principal y control de playlists.
- `/add` — Página para agregar canciones a la base de datos.
- `/addPlaylist` — Página para añadir canciones a una playlist.

## 🧠 Notas

- Las playlists y canciones añadidas se guardan en el navegador mediante `localStorage`, por lo que no se pierden al recargar.
- Las canciones deben subirse mediante el formulario en `/add`.

---

Desarrollado por [José Zurita](https://github.com/jzurit4/) ❤️
