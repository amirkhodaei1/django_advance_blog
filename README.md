Django Advance Blog

A Full-Stack Django Backend Engineering Playground

<p align="center">
  <strong>From Django fundamentals to APIs, authentication, caching, background jobs, testing, load testing, and containerized deployment.</strong>
</p><p align="center">
  <a href="https://github.com/amirkhodaei1/django_advance_blog">
    <img src="https://img.shields.io/badge/GitHub-Repository-181717?logo=github" alt="GitHub">
  </a>
  <img src="https://img.shields.io/badge/Django-6.0.7-092E20?logo=django&logoColor=white" alt="Django">
  <img src="https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/DRF-3.15.2-A30000" alt="Django REST Framework">
  <img src="https://img.shields.io/badge/Redis-Cache%20%2B%20Broker-DC382D?logo=redis&logoColor=white" alt="Redis">
  <img src="https://img.shields.io/badge/Celery-5.6.3-37814A?logo=celery&logoColor=white" alt="Celery">
  <img src="https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker&logoColor=white" alt="Docker">
  <img src="https://img.shields.io/badge/Gunicorn-Production-499848" alt="Gunicorn">
  <img src="https://img.shields.io/badge/Nginx-Reverse%20Proxy-009639?logo=nginx&logoColor=white" alt="Nginx">
</p>---

✦ About

Django Advance Blog is not just a blog application.

It is an evolving backend engineering project built to explore how a Django application grows from a conventional web application into a more complete, API-driven, asynchronous, tested, cached, containerized, and deployable system.

The repository brings together multiple layers of backend engineering:

Django
  ↓
Application Architecture
  ↓
REST APIs
  ↓
Authentication
  ↓
API Documentation
  ↓
Redis Caching
  ↓
Celery Background Processing
  ↓
Periodic Tasks
  ↓
Automated Testing
  ↓
Load Testing
  ↓
Docker
  ↓
Gunicorn + Nginx
  ↓
Continuous Integration

The current codebase contains dedicated "accounts", "blog", and "locust" components, a "core" Django project, versioned blog APIs, Swagger/Redoc documentation routes, Docker deployment files, and a GitHub Actions CI workflow.

---

✨ Highlights

<table>
<tr>
<td width="50%">🧱 Django Core

- Modular Django applications
- Custom user model
- Class-Based Views
- Templates
- Forms
- Admin
- URL namespacing

</td>
<td width="50%">🌐 API Platform

- Django REST Framework
- Versioned API structure
- JWT authentication
- Token authentication
- Session authentication
- Filtering
- Djoser

</td>
</tr><tr>
<td>⚡ Distributed Features

- Redis caching
- Celery
- Celery Beat
- Redis-backed task infrastructure

</td>
<td>🧪 Quality & Performance

- Pytest
- pytest-django
- Flake8
- Black
- Locust
- CI with GitHub Actions

</td>
</tr><tr>
<td>🐳 Deployment

- Docker
- Docker Compose
- Gunicorn
- Nginx
- Static volumes
- Media volumes

</td>
<td>📚 Developer Experience

- Swagger
- ReDoc
- DRF API docs
- Management commands
- Containerized development

</td>
</tr>
</table>The dependency manifest confirms the project integrates Django REST Framework, Simple JWT, Djoser, Django Filters, Redis, django-redis, Celery, Django Celery Beat, Pytest, Flake8, Black, Locust-related infrastructure, Gunicorn, and API documentation tooling.

---

🧭 Project Vision

The project is designed around a simple engineering idea:

«Build a Django application the way a real backend system grows in the real world.»

Instead of stopping at:

Model → View → Template

the project explores:

                       ┌────────────────────┐
                       │       Client       │
                       └─────────┬──────────┘
                                 │
                                 ▼
                       ┌────────────────────┐
                       │       Nginx        │
                       │ Reverse Proxy      │
                       └─────────┬──────────┘
                                 │
                                 ▼
                       ┌────────────────────┐
                       │     Gunicorn       │
                       │      WSGI          │
                       └─────────┬──────────┘
                                 │
                                 ▼
                       ┌────────────────────┐
                       │      Django        │
                       │ Web + REST APIs    │
                       └──────┬──────┬──────┘
                              │      │
                    ┌─────────┘      └─────────┐
                    ▼                          ▼
             ┌──────────────┐           ┌──────────────┐
             │    Redis     │           │   Database   │
             │ Cache/Broker │           │    SQLite    │
             └──────┬───────┘           └──────────────┘
                    │
               ┌────┴────┐
               ▼         ▼
          ┌─────────┐ ┌─────────────┐
          │ Celery  │ │ Celery Beat │
          │ Worker  │ │  Scheduler  │
          └─────────┘ └─────────────┘

The current settings use SQLite for the database, Redis database "2" for Django caching, and Redis database "1" as the Celery broker.

---

🏗️ Architecture

Application Layer

core/
│
├── core/          → Django project configuration
│
├── accounts/      → User/account domain
│
├── blog/          → Blog domain
│
└── locust/        → Load-testing resources

The repository contains "core/manage.py", the inner "core" project package, "accounts", "blog", "locust", and a static directory.

---

📦 Repository Structure

django_advance_blog/
│
├── .github/
│   └── workflows/
│       └── docker-image.yml
│
├── core/
│   ├── accounts/
│   │   ├── ...
│   │   └── ...
│   │
│   ├── blog/
│   │   ├── api/
│   │   │   └── v1/
│   │   ├── ...
│   │   └── urls.py
│   │
│   ├── core/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── asgi.py
│   │
│   ├── locust/
│   ├── static/
│   ├── manage.py
│   ├── pytest.ini
│   └── .flake8
│
├── templates/
│
├── Dockerfile
├── docker-compose.yml
├── docker-compose-stage.yml
├── docker-compose-prod.yml
├── default.conf
├── requirements.txt
├── LICENSE
└── README.md

---

📝 Core Django Project

The inner "core" package contains the Django project's configuration.

The project configures:

ROOT_URLCONF = "core.urls"
WSGI_APPLICATION = "core.wsgi.application"

The production-oriented Compose configuration starts Gunicorn with:

gunicorn core.wsgi --bind 0.0.0.0:8000

---

👤 Accounts

The application defines a dedicated "accounts" application.

The project explicitly uses:

AUTH_USER_MODEL = "accounts.User"

This means user management is built around a custom user model.

---

📰 Blog

The "blog" application is the primary business domain.

It combines classic Django views with API-oriented functionality.

The current URL configuration includes routes for:

/blog/
/blog/post/
/blog/post/api
/blog/post/<id>/
/blog/post/create/
/blog/post/<id>/edit
/blog/post/<id>/delete
/blog/api/v1/
/blog/test_weather/

---

🌐 API Architecture

The blog API is explicitly versioned:

/blog/api/v1/

and is included from:

path(
    "api/v1/",
    include("blog.api.v1.urls", namespace="api-v1"),
)

This is an important architectural choice because API versioning provides a path for evolving endpoints without immediately breaking existing clients.

---

🔐 Authentication

The REST framework configuration currently supports:

BasicAuthentication
SessionAuthentication
TokenAuthentication
JWTAuthentication

This gives the API multiple authentication strategies for different client types.

Authentication ecosystem

                       Authentication
                              │
             ┌────────────────┼────────────────┐
             ▼                ▼                ▼
         Session            Token             JWT
             │                │                │
             └────────────────┼────────────────┘
                              ▼
                         REST API

The project also includes Djoser and Simple JWT in its dependency stack.

---

🔑 JWT

JWT support is provided through:

rest_framework_simplejwt

and registered in Django REST Framework's authentication classes.

This makes the project suitable for API consumers such as:

Web SPA
Mobile App
Desktop Client
External Service

---

🎛️ Filtering

The project includes:

django-filter

which provides infrastructure for building filterable REST endpoints.

---

📚 API Documentation

The project exposes multiple API documentation interfaces.

Current routes include:

/swagger/

/swagger/output.json

/redoc/

and DRF documentation:

/api-docs/

The Django URL configuration uses "drf_yasg" to build the Swagger schema and exposes both Swagger UI and ReDoc.

---

🗺️ API Documentation Flow

Django REST API
       │
       ▼
 OpenAPI Schema
       │
    ┌──┴───┐
    ▼      ▼
 Swagger  ReDoc

---

⚡ Redis

Redis plays a central role in the architecture.

It is used for:

Cache
 +
Celery Broker

The current Django settings configure:

Redis DB 2 → Django Cache
Redis DB 1 → Celery Broker

---

🧠 Caching

The project uses "django-redis":

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379/2",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        },
    }
}

This provides a foundation for reducing repeated database work and improving response performance.

---

🔄 Celery

Celery is integrated into the project for asynchronous processing.

Current broker:

redis://redis:6379/1

Architecture:

Django
  │
  │ enqueue task
  ▼
Redis
  │
  ▼
Celery Worker
  │
  ▼
Background Processing

Celery and "django-celery-beat" are included in the project's dependencies.

---

⏰ Celery Beat

Periodic tasks are supported through:

django-celery-beat

Conceptually:

Celery Beat
    │
    ▼
 Redis
    │
    ▼
Celery Worker
    │
    ▼
Periodic Task

This architecture allows the application to move beyond request/response processing into scheduled background workflows.

---

📧 Email Infrastructure

The current settings configure SMTP through a service named:

smtp4dev

using:

smtp4dev:25

This is useful for local/staging email development without relying on a real mail provider.

---

🌐 CORS

The project currently enables:

CORS_ALLOW_ALL_ORIGINS = True

This is convenient during development and testing, but production deployments should normally restrict allowed origins.

---

🎨 Static Files

The current Django configuration uses:

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "static"
STATICFILES_DIRS = [
    BASE_DIR / "staticfiles"
]

The project also defines media handling through:

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

---

📦 Static File Architecture

                   Django
                      │
                      │ collectstatic
                      ▼
              /app/core/static
                      │
                      ▼
               static_volume
                      │
                      ▼
                    Nginx
                      │
                      ▼
                  /static/*

The staging Compose configuration shares "static_volume" and "media_volume" between the backend and Nginx containers.

---

🌍 Nginx

Nginx sits in front of Django and forwards application requests to:

backend:8000

while also serving static and media assets.

                         Nginx
                           │
             ┌─────────────┼─────────────┐
             ▼             ▼             ▼
          /static/       /media/          /
             │             │              │
             ▼             ▼              ▼
          Static          Media         Django
                                        :8000

The repository's current Nginx configuration uses an upstream named "django" pointing at "backend:8000".

---

🦄 Gunicorn

Gunicorn is used as the WSGI application server.

Current staging command:

gunicorn core.wsgi --bind 0.0.0.0:8000

This establishes the standard deployment chain:

Client
  ↓
Nginx
  ↓
Gunicorn
  ↓
Django

---

🐳 Docker

The project includes a Dockerfile based on:

FROM python:3.12-slim

The image installs the project's Python dependencies and switches the working directory to the "core" directory where "manage.py" resides.

---

🧩 Docker Compose

The repository includes separate Compose definitions:

docker-compose.yml
docker-compose-stage.yml
docker-compose-prod.yml

The current staging configuration defines:

redis
backend
nginx

with named volumes:

static_volume
media_volume

---

🚀 Staging Deployment

Start the staging environment:

docker compose -f docker-compose-stage.yml up -d --build

Check status:

docker compose -f docker-compose-stage.yml ps

Follow logs:

docker compose -f docker-compose-stage.yml logs -f

Backend only:

docker compose -f docker-compose-stage.yml logs -f backend

Nginx only:

docker compose -f docker-compose-stage.yml logs -f nginx

---

🛠️ Django Operations

System Check

docker compose exec backend python manage.py check

Migrations

docker compose exec backend python manage.py makemigrations

docker compose exec backend python manage.py migrate

Superuser

docker compose exec backend python manage.py createsuperuser

Static Collection

docker compose exec backend python manage.py collectstatic --noinput

Django Shell

docker compose exec backend python manage.py shell

---

🧪 Testing

Testing is part of the repository's development workflow.

The project includes:

pytest
pytest-django

Run:

pytest .

or:

docker compose exec backend pytest .

---

🧹 Code Quality

The project includes:

Flake8
Black

Run Flake8:

flake8 .

Run Black:

black .

Inside Docker:

docker compose exec backend flake8 .

docker compose exec backend black .

---

📈 Load Testing

A dedicated "locust" directory exists in the project for load-testing resources.

This allows the application to be evaluated under simulated concurrent traffic.

Load testing can reveal:

Latency
Throughput
Error Rate
Concurrency Limits
Database Bottlenecks
Cache Effectiveness
Resource Pressure

Conceptually:

Locust
   │
   ├──── Request
   ├──── Request
   ├──── Request
   ├──── Request
   ▼
Django API

---

🤖 Continuous Integration

The repository includes:

.github/workflows/docker-image.yml

The current workflow runs for pushes and pull requests against "main".

Its pipeline executes:

Checkout
   ↓
Start Docker Compose
   ↓
Run Flake8
   ↓
Run Pytest

The current workflow specifically runs both linting and tests inside the Docker backend container.

---

🔁 CI Pipeline

                    GitHub
                       │
                       ▼
                  Git Push / PR
                       │
                       ▼
               GitHub Actions
                       │
              ┌────────┴────────┐
              ▼                 ▼
           Flake8             Pytest
              │                 │
              └────────┬────────┘
                       ▼
                    Result

---

🔐 Configuration

The project uses "python-decouple".

The current settings define configuration through environment-aware values such as:

SECRET_KEY = config("SECRET_KEY", default="test")

DEBUG = config("DEBUG", cast=bool, default=True)

ALLOWED_HOSTS = config(
    "ALLOWED_HOSTS",
    cast=lambda v: [s.strip() for s in v.split(",")],
    default="*",
)

For production:

SECRET_KEY=<strong-secret>
DEBUG=False
ALLOWED_HOSTS=example.com,www.example.com

---

🛡️ Production Security Notes

Before exposing the application publicly, review:

DEBUG
SECRET_KEY
ALLOWED_HOSTS
CORS
CSRF
HTTPS
Cookies
Redis exposure
Database exposure
File permissions
Secrets

The current development-oriented configuration includes permissive defaults such as "ALLOWED_HOSTS="*"" and "CORS_ALLOW_ALL_ORIGINS=True"; these should be tightened for a real production deployment.

---

🧭 API Map

The current top-level URL architecture includes:

Route| Purpose
"/admin/"| Django Admin
"/accounts/"| Account-related routes
"/blog/"| Blog application
"/api-auth/"| DRF authentication
"/api-docs/"| DRF API documentation
"/swagger/"| Swagger UI
"/swagger/output.json"| OpenAPI schema
"/redoc/"| ReDoc
"/blog/api/v1/"| Versioned Blog API

---

🔬 Engineering Concepts Demonstrated

This repository is especially valuable as a practical study project because it touches several independent backend concepts.

                    Backend Engineering
                            │
       ┌────────────────────┼────────────────────┐
       ▼                    ▼                    ▼
   Application            API Layer          Infrastructure
       │                    │                    │
   Django Apps          DRF / JWT          Docker / Nginx
       │                    │                    │
       ▼                    ▼                    ▼
   Domain Logic        Authentication       Gunicorn
                            │                    │
                            ▼                    ▼
                        API Docs              Redis
                                                 │
                                                 ▼
                                               Celery

---

🧪 Quality Engineering

The project treats quality as a separate engineering concern.

                    Code
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
      Flake8       Black        Pytest
        │            │            │
        └────────────┼────────────┘
                     ▼
                   CI

The current GitHub Actions workflow executes Flake8 and Pytest through Docker Compose.

---

⚡ Performance Engineering

Performance is addressed through two complementary mechanisms:

Redis

Reduce expensive repeated work:

Request
   │
   ▼
Cache?
 ┌─┴─┐
Yes  No
 │    │
 ▼    ▼
Data Database

Locust

Measure application behavior under load:

Users
  │
  ▼
Locust
  │
  ▼
Django
  │
  ├── Redis
  └── Database

---

🔄 Asynchronous Architecture

Celery introduces a second processing path alongside regular HTTP requests.

Synchronous

Client
  ↓
Nginx
  ↓
Django
  ↓
Response

Asynchronous

Client
  ↓
Django
  ↓
Redis
  ↓
Celery Worker
  ↓
Background Task

This separation allows expensive or delayed workloads to move outside the HTTP request lifecycle.

---

🧱 Development Philosophy

The project is intentionally incremental.

Every new technology solves a different engineering problem:

Problem| Solution
Web framework| Django
API development| DRF
Authentication| Session / Token / JWT
User APIs| Djoser
Filtering| django-filter
API documentation| Swagger / ReDoc
Caching| Redis
Background jobs| Celery
Scheduled jobs| Celery Beat
Testing| Pytest
Code quality| Flake8 / Black
Performance testing| Locust
Runtime isolation| Docker
HTTP gateway| Nginx
Application server| Gunicorn
Automation| GitHub Actions

---

🚀 Quick Start

Clone

git clone https://github.com/amirkhodaei1/django_advance_blog.git
cd django_advance_blog

Start with Docker

docker compose up -d --build

Check containers

docker compose ps

Run migrations

docker compose exec backend python manage.py migrate

Collect static files

docker compose exec backend python manage.py collectstatic --noinput

Run tests

docker compose exec backend pytest .

Run linting

docker compose exec backend flake8 .

---

🔍 Useful Debugging Commands

Inspect Django paths

docker compose exec backend \
python manage.py shell -c \
"from django.conf import settings; \
print('BASE_DIR =', settings.BASE_DIR); \
print('STATIC_ROOT =', settings.STATIC_ROOT); \
print('STATIC_URL =', settings.STATIC_URL)"

Verify WSGI

docker compose exec backend \
python -c "import core.wsgi; print('WSGI OK')"

Inspect static files

docker compose exec backend \
find /app/core/static -type f | head -20

Inspect Nginx static files

docker compose exec nginx \
find /home/app/static -type f | head -20

Validate Nginx

docker compose exec nginx nginx -t

---

🐞 Troubleshooting Philosophy

When something fails, follow the request through the architecture.

Browser
  ↓
Nginx
  ↓
Gunicorn
  ↓
Django
  ↓
Redis / Database

For static files:

Django collectstatic
        ↓
   static_volume
        ↓
      Nginx
        ↓
    /static/*

For Celery:

Django
   ↓
Redis
   ↓
Celery Worker

This approach makes debugging systematic instead of trial-and-error.

---

📈 Roadmap

The existing repository already contains a strong set of backend engineering components.

Natural next stages include:

Production Hardening

- [ ] HTTPS
- [ ] Secure production headers
- [ ] Restrictive CORS
- [ ] Strict "ALLOWED_HOSTS"
- [ ] Secret management
- [ ] Health checks

Data Layer

- [ ] PostgreSQL production configuration
- [ ] Automated database backups
- [ ] Backup restoration testing

Async Platform

- [ ] Dedicated Celery Worker service
- [ ] Dedicated Celery Beat service
- [ ] Flower monitoring

Observability

- [ ] Sentry
- [ ] Prometheus
- [ ] Grafana
- [ ] Centralized logging

Delivery

- [ ] Docker image registry
- [ ] Automated staging deployment
- [ ] Production deployment
- [ ] Rollback strategy

Scaling

- [ ] Multiple backend replicas
- [ ] Load balancing
- [ ] Object storage
- [ ] Managed Redis
- [ ] Managed PostgreSQL

---

🧠 The Learning Journey

The project can be read as a progression:

                   DJANGO
                     │
                     ▼
               Web Application
                     │
                     ▼
                   REST
                     │
                     ▼
              Authentication
                     │
                     ▼
               API Design
                     │
                     ▼
                  Redis
                     │
                     ▼
                 Celery
                     │
                     ▼
             Scheduled Tasks
                     │
                     ▼
                  Testing
                     │
                     ▼
              Load Testing
                     │
                     ▼
                  Docker
                     │
                     ▼
             Gunicorn + Nginx
                     │
                     ▼
                    CI
                     │
                     ▼
             Production Mindset

---

🌟 Why This Project Matters

A blog is only the visible surface.

The real value of this repository is the engineering journey underneath it.

It demonstrates how a simple Django application can evolve into a system with:

                    ┌─────────────────┐
                    │   Web Layer     │
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │    API Layer    │
                    └────────┬────────┘
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
        Authentication     Cache       Background Jobs
              │              │              │
              ▼              ▼              ▼
             JWT           Redis          Celery
              │                             │
              └─────────────┬───────────────┘
                            ▼
                       Django Core
                            │
              ┌─────────────┼─────────────┐
              ▼             ▼             ▼
           Testing       Load Test     Deployment
              │             │             │
           Pytest         Locust      Docker/Nginx
              │                             │
              └─────────────┬───────────────┘
                            ▼
                           CI

That is what makes "django_advance_blog" more than a CRUD tutorial.

It is a practical environment for learning how backend systems are actually assembled.

---

🤝 Contributing

Contributions, bug fixes, test improvements, documentation updates, refactoring, and infrastructure improvements are welcome.

Before submitting a change:

pytest .

flake8 .

black .

and verify that the Docker environment starts successfully.

---

📜 License

See the repository's ""LICENSE"" (LICENSE) file for the project's licensing terms.

---

👨‍💻 Author

Amir Khodaei

GitHub:

https://github.com/amirkhodaei1

Repository:

https://github.com/amirkhodaei1/django_advance_blog

---

⭐ Final Snapshot

                    DJANGO ADVANCE BLOG
                           │
         ┌─────────────────┼─────────────────┐
         │                 │                 │
         ▼                 ▼                 ▼
     APPLICATION          API             INFRASTRUCTURE
         │                 │                 │
      Django              DRF             Docker
      Blog              JWT / Token       Nginx
      Accounts          Djoser            Gunicorn
         │            Swagger/Redoc       Redis
         │                 │                 │
         └─────────────────┼─────────────────┘
                           │
                ┌──────────┴──────────┐
                ▼                     ▼
             QUALITY              ASYNC
                │                     │
             Pytest               Celery
             Flake8             Celery Beat
             Black                  Redis
             Locust
                │                     │
                └──────────┬──────────┘
                           ▼
                     GitHub Actions
                           │
                           ▼
                Continuous Improvement

<p align="center">
  <strong>Built to learn Django.</strong><br>
  <strong>Structured to understand backend engineering.</strong><br>
  <strong>Designed to evolve toward production.</strong>
</p><p align="center">
  ⭐ <strong>django_advance_blog</strong> ⭐
</p>