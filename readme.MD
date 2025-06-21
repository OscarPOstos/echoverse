# 🌌 EchoVerse API

EchoVerse es una API construida con Django REST Framework que permite a los usuarios compartir pensamientos breves, responder a otros usuarios, reaccionar con emojis y ver estadísticas de participación.

---

## 🔐 Autenticación

La API usa autenticación por token. Para obtener un token:

- **Registro:** `POST /api/auth/register/`
- **Login:** `POST /api/auth/login/`

Incluye el token en el encabezado:
```
Authorization: Token tu_token_aqui
```

---

## 📌 Pensamientos (Posts)
- `GET /api/posts/` — Lista todos los pensamientos.
- `POST /api/posts/` — Publica un nuevo pensamiento.
- `GET /api/posts/{id}/` — Ver detalles de un pensamiento.
- `DELETE /api/posts/{id}/` — Elimina un pensamiento (solo autor o moderador).

---

## 💬 Ramificaciones (Responses)
- `GET /api/posts/{post_id}/replies/` — Ver respuestas al pensamiento.
- `POST /api/posts/{post_id}/replies/` — Responder con otro pensamiento.

---

## ❤️ Reacciones
- `POST /api/posts/{post_id}/react/` — Reaccionar a un pensamiento con un emoji.
- `GET /api/posts/{post_id}/reactions/` — Ver resumen de reacciones.

---

## 📊 Estadísticas
- `GET /api/stats/active/` — Pensamientos publicados hoy.
- `GET /api/stats/top/` — Pensamientos más populares.

---

## 🧪 Test rápido con HTTP client (VSCode)
Puedes usar los archivos `.http` incluidos para probar la API directamente desde Visual Studio Code.

---

## 🚀 Instalación rápida
```bash
git clone <repo>
cd echoverse
python -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

## 🛠 Requisitos
- Python 3.8+
- Django 4+
- Django REST Framework

---

## 📄 Licencia
MIT © 2025 EchoVerse API