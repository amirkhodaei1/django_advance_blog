django_advance_blog

Advanced Django Blog Platform with REST APIs, Authentication, Background Tasks, Caching, Testing, Load Testing, Docker, and CI

""Python" (https://img.shields.io/badge/Python-3.12+-3776AB?logo=python&logoColor=white)" (https://www.python.org/)
""Django" (https://img.shields.io/badge/Django-6.0.7-092E20?logo=django&logoColor=white)" (https://www.djangoproject.com/)
""Django REST Framework" (https://img.shields.io/badge/DRF-3.15.2-A30000?logo=django&logoColor=white)" (https://www.django-rest-framework.org/)
""Redis" (https://img.shields.io/badge/Redis-8.x-DC382D?logo=redis&logoColor=white)" (https://redis.io/)
""Celery" (https://img.shields.io/badge/Celery-5.6.3-37814A?logo=celery&logoColor=white)" (https://docs.celeryq.dev/)
""Docker" (https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker&logoColor=white)" (https://www.docker.com/)
""Pytest" (https://img.shields.io/badge/Pytest-9.x-0A9EDC?logo=pytest&logoColor=white)" (https://pytest.org/)
""License" (https://img.shields.io/badge/License-MIT-blue.svg)" (LICENSE)

«A serious Django learning and engineering project that combines a traditional blog application with REST APIs, multiple authentication mechanisms, asynchronous processing, caching, automated testing, load testing, containerization, and CI.»

---

📌 Project Overview

"django_advance_blog" is an advanced Django project built around a blog application and designed to explore the transition from a conventional Django website into a more complete backend platform.

The repository brings together multiple areas of modern Django development:

- Django application development
- Blog/domain modeling
- Custom user management
- Class-Based Views
- Django REST Framework
- API authentication
- JWT authentication
- API documentation
- Redis caching
- Celery background processing
- Celery Beat scheduling
- Automated testing
- Pytest
- Flake8
- Load testing with Locust
- Docker and Docker Compose
- Gunicorn
- Nginx
- GitHub Actions

The current repository contains dedicated "accounts", "blog", "locust", and "core" components, together with Docker, deployment, and CI configuration.

---

🎯 What This Project Demonstrates

This project is intentionally broader than a simple CRUD blog.

It demonstrates how different backend concerns can coexist in one Django system:

                         ┌──────────────────────┐
                         │      Web Client      │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │        Nginx         │
                         │ Reverse Proxy / HTTP │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │      Gunicorn        │
                         │    WSGI Server       │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │       Django         │
                         │  Web + REST APIs     │
                         └───────┬───────┬──────┘
                                 │       │
                    ┌────────────┘       └────────────┐
                    ▼                                 ▼
             ┌─────────────┐                    ┌─────────────┐
             │    Redis    │                    │  Database   │
             │ Cache/Queue │                    │   SQLite*   │
             └──────┬──────┘                    └─────────────┘
                    │
              ┌─────┴──────┐
              ▼            ▼
        ┌──────────┐  ┌──────────────┐
        │  Celery  │  │ Celery Beat  │
        │  Worker  │  │  Scheduler   │
        └──────────┘  └──────────────┘

* The current settings use SQLite as the default database.

The repository's current settings configure SQLite, Redis caching, Redis as the Celery broker, and Django apps including "blog", "accounts", DRF, Djoser, JWT support, CORS headers, and "django-celery-beat".

---

🧰 Technology Stack

Technology| Purpose
Python 3.12+| Backend language/runtime
Django 6.0.7| Web framework
Django REST Framework| REST API development
Djoser| Authentication endpoints
Simple JWT| JWT authentication
Token Authentication| API token authentication
Django Filters| API filtering
DRF YASG| Swagger/OpenAPI documentation
Redis| Cache + Celery broker
django-redis| Django Redis cache backend
Celery| Background task processing
django-celery-beat| Periodic task scheduling
Pytest| Testing
pytest-django| Django test integration
Flake8| Static analysis
Black| Code formatting
Locust| Load testing
Gunicorn| WSGI application server
Nginx| Reverse proxy + static/media serving
Docker| Containerization
Docker Compose| Local/staging orchestration
GitHub Actions| CI

These dependencies are pinned in "requirements.txt".

---

📂 Repository Structure

The repository currently follows this general structure:

django_advance_blog/
│
├── .devcontainer/
│
├── .github/
│   └── workflows/
│       └── docker-image.yml
│
├── .vscode/
│
├── core/
│   ├── accounts/
│   ├── blog/
│   ├── core/
│   ├── locust/
│   ├── static/
│   ├── manage.py
│   ├── pytest.ini
│   └── .flake8
│
├── templates/
│
├── Dockerfile
├── default.conf
├── docker-compose.yml
├── docker-compose-stage.yml
├── docker-compose-prod.yml
├── requirements.txt
├── LICENSE
└── README.md

The repository currently contains separate "accounts", "blog", "core", "locust", and static components, as well as development, staging, and production Compose files.

---

🧠 Application Architecture

"accounts"

The project contains a dedicated "accounts" application for user-related functionality.

The Django settings also configure:

AUTH_USER_MODEL = "accounts.User"

which means the project uses a custom user model rather than relying solely on Django's default user model.

---

"blog"

The "blog" application contains the blog domain and its associated application logic.

It serves as the primary business domain through which the project demonstrates:

- Django models
- forms
- views
- class-based views
- REST APIs
- serializers
- authentication-aware endpoints
- testing

---

"core"

The inner "core" package contains the Django project configuration:

core/
├── settings.py
├── urls.py
├── wsgi.py
└── asgi.py

The current WSGI application is configured as:

WSGI_APPLICATION = "core.wsgi.application"

and Gunicorn is configured to run:

gunicorn core.wsgi --bind 0.0.0.0:8000

---

🔐 Authentication

The project integrates several Django REST authentication mechanisms.

Current REST framework configuration includes:

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
}

This gives the project a useful foundation for experimenting with:

- Session authentication
- Basic authentication
- DRF token authentication
- JWT authentication

---

🔑 JWT Authentication

JWT support is provided through:

djangorestframework_simplejwt

and is included in the project's REST authentication classes.

This allows API clients to use stateless token-based authentication suitable for:

- mobile applications
- SPA frontends
- external API consumers
- service integrations

---

👤 Djoser

The project also includes:

djoser

as a dependency and Django application.

Djoser provides infrastructure for authentication-related API endpoints and can reduce the amount of repetitive authentication boilerplate required in an API project.

---

📡 REST API

The project uses:

Django REST Framework

together with:

django-filter

for API development and filtering capabilities.

The dependency stack also contains both:

drf-yasg
drf-spectacular

providing OpenAPI/Swagger-related tooling in the project environment.

---

📚 API Documentation

API documentation is part of the project's architecture.

The repository includes Swagger/OpenAPI-related dependencies such as:

drf-yasg
drf-spectacular

This makes it possible to expose machine-readable and interactive API documentation for the REST layer.

---

⚡ Redis

Redis is integrated into the project for more than one purpose.

Cache

The current Django configuration uses:

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379/2",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        },
    }
}

Celery Broker

Celery is configured to use Redis as its broker:

CELERY_BROKER_URL = "redis://redis:6379/1"

This separates cache traffic and Celery broker traffic into different Redis databases.

---

🔄 Celery

The project includes:

celery
django-celery-beat
redis

providing the foundation for asynchronous background processing.

Conceptually:

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
Background Task

This architecture is suitable for operations that do not need to block an HTTP request.

Examples include:

- email delivery
- notifications
- long-running processing
- scheduled work
- background data processing

The repository explicitly includes Celery, Redis, and Django Celery Beat dependencies.

---

⏰ Celery Beat

"django-celery-beat" is included for periodic task scheduling.

The conceptual flow is:

Celery Beat
     │
     ▼
   Redis
     │
     ▼
Celery Worker
     │
     ▼
   Task

This allows the application to evolve from request/response processing toward scheduled background workflows.

---

🗃️ Database

The current project settings use SQLite:

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

This is convenient for development and educational use.

For larger production deployments, the database layer can later be moved to a dedicated relational database such as PostgreSQL.

---

🎨 Static & Media Files

Django currently defines:

STATIC_URL = "static/"
MEDIA_URL = "media/"

STATIC_ROOT = BASE_DIR / "static"
MEDIA_ROOT = BASE_DIR / "media"

STATICFILES_DIRS = [
    BASE_DIR / "staticfiles"
]

The staging Compose configuration shares static and media content between the Django backend and Nginx using Docker named volumes:

volumes:
  static_volume:
  media_volume:

The backend mounts:

- static_volume:/app/core/static
- media_volume:/app/core/media

while Nginx mounts those same named volumes for serving the files.

---

🌐 Nginx

Nginx acts as the HTTP entry point in the containerized deployment.

The current configuration forwards application traffic to:

backend:8000

and serves static and media files directly.

Architecture:

Client
  │
  ▼
Nginx :80
  │
  ├── /static/ → static files
  │
  ├── /media/  → media files
  │
  └── /        → backend:8000

---

🚀 Gunicorn

The staging deployment uses Gunicorn as the production WSGI server:

gunicorn core.wsgi --bind 0.0.0.0:8000

This replaces Django's development server with a dedicated WSGI application server for deployment scenarios.

---

🐳 Docker

The repository includes a Dockerfile based on:

FROM python:3.12-slim

The image:

1. creates "/app" as the initial working directory,
2. upgrades pip,
3. installs "requirements.txt",
4. copies the project,
5. switches to "/app/core",
6. exposes port "8000".

---

🧩 Docker Compose

The repository contains multiple Compose configurations:

docker-compose.yml
docker-compose-stage.yml
docker-compose-prod.yml

This gives the project a clear path toward separating development, staging, and production concerns.

---

🧪 Testing

The repository contains:

pytest
pytest-django

and a "pytest.ini" configuration file inside the Django project.

Run tests with:

pytest .

Inside Docker:

docker compose exec backend pytest .

---

🧹 Code Quality

The project includes both:

flake8
black

for code-quality and formatting workflows.

Run Flake8:

flake8 .

Inside Docker:

docker compose exec backend flake8 .

Format with Black:

black .

---

📈 Load Testing

The repository includes a dedicated:

core/locust/

component for load testing.

Locust is useful for evaluating application behavior under concurrent traffic and identifying:

- slow endpoints
- throughput limitations
- unexpected error rates
- bottlenecks
- resource pressure

Run Locust according to the load-testing configuration contained in the "core/locust" directory.

---

🤖 Continuous Integration

The repository contains a GitHub Actions workflow:

.github/workflows/docker-image.yml

The current workflow runs on pushes and pull requests targeting "main".

Its pipeline:

GitHub
   │
   ▼
Checkout
   │
   ▼
Start Docker Compose
   │
   ├── Flake8
   │
   └── Pytest

The current workflow explicitly starts Docker Compose and executes both Flake8 and Pytest inside the backend container.

---

🚀 Getting Started

1. Clone the repository

git clone https://github.com/amirkhodaei1/django_advance_blog.git

cd django_advance_blog

---

🐳 Run with Docker

Start the default Compose environment:

docker compose up -d --build

Check services:

docker compose ps

View logs:

docker compose logs -f

---

🧰 Development Commands

Run Django checks:

docker compose exec backend python manage.py check

Create migrations:

docker compose exec backend python manage.py makemigrations

Apply migrations:

docker compose exec backend python manage.py migrate

Open Django shell:

docker compose exec backend python manage.py shell

Create a superuser:

docker compose exec backend python manage.py createsuperuser

Collect static files:

docker compose exec backend python manage.py collectstatic --noinput

---

🧪 Run Tests

docker compose exec backend pytest .

Or locally:

pytest .

---

🧹 Run Flake8

docker compose exec backend flake8 .

---

🎨 Run Black

docker compose exec backend black .

---

🔴 Redis CLI

Open the Redis shell:

docker compose exec redis redis-cli

Test connectivity:

PING

Expected:

PONG

---

🏗️ Staging

The repository provides a dedicated staging configuration:

docker compose -f docker-compose-stage.yml up -d --build

Inspect:

docker compose -f docker-compose-stage.yml ps

Follow backend logs:

docker compose -f docker-compose-stage.yml logs -f backend

Follow Nginx logs:

docker compose -f docker-compose-stage.yml logs -f nginx

The current staging definition starts Redis, Django/Gunicorn, and Nginx and uses named volumes for static/media assets.

---

🔄 Staging Deployment Flow

Recommended operational sequence:

Pull Code
   │
   ▼
Build Images
   │
   ▼
Start Services
   │
   ▼
Django Check
   │
   ▼
Migrations
   │
   ▼
Collect Static
   │
   ▼
Nginx Validation
   │
   ▼
Application Smoke Test

Commands:

git pull

docker compose -f docker-compose-stage.yml up -d --build

docker compose -f docker-compose-stage.yml exec backend \
python manage.py check

docker compose -f docker-compose-stage.yml exec backend \
python manage.py migrate

docker compose -f docker-compose-stage.yml exec backend \
python manage.py collectstatic --noinput

docker compose -f docker-compose-stage.yml exec nginx nginx -t

---

🔍 Troubleshooting

Backend does not start

Inspect logs:

docker compose logs backend

Or:

docker compose -f docker-compose-stage.yml logs backend

Verify the Django project:

docker compose exec backend python -c \
"import core; print(core.__file__)"

Verify WSGI:

docker compose exec backend python -c \
"import core.wsgi; print('WSGI OK')"

---

❌ "ModuleNotFoundError: No module named 'core'"

Check the project structure:

docker compose exec backend find /app -maxdepth 3 -name wsgi.py

Check the working directory:

docker compose exec backend pwd

Check "/app":

docker compose exec backend ls -la /app

The container's working directory, volume mounts, and Gunicorn module path must match the actual repository structure.

---

❌ Static Files Are Not Loading

First verify Django's settings:

docker compose exec backend python manage.py shell -c \
"from django.conf import settings; print(settings.BASE_DIR); print(settings.STATIC_ROOT); print(settings.STATIC_URL)"

Collect:

docker compose exec backend python manage.py collectstatic --noinput

Check backend:

docker compose exec backend \
find /app/core/static -type f | head -20

Check Nginx:

docker compose exec nginx \
find /home/app/static -type f | head -20

Then validate:

docker compose exec nginx nginx -t

---

❌ "static_volume" Is Undefined

Make sure the Compose file declares:

volumes:
  static_volume:
  media_volume:

The current staging configuration includes both named volumes.

---

🧠 Redis Connectivity Problems

Inside Docker, use the Compose service name:

redis:6379

not:

localhost:6379

The project's Celery broker currently uses:

redis://redis:6379/1

and Django's cache uses:

redis://redis:6379/2

---

🔐 Configuration & Environment Variables

The project uses "python-decouple" for configuration.

For example:

SECRET_KEY = config("SECRET_KEY", default="test")
DEBUG = config("DEBUG", cast=bool, default=True)
ALLOWED_HOSTS = config(
    "ALLOWED_HOSTS",
    cast=lambda v: [s.strip() for s in v.split(",")],
    default="*",
)

For real deployments, secrets should be stored outside source control.

Recommended values include:

SECRET_KEY=<strong-secret>
DEBUG=False
ALLOWED_HOSTS=example.com,www.example.com

---

⚠️ Production Considerations

The repository already contains deployment-oriented components such as Gunicorn, Nginx, Docker Compose, Redis, Celery, static/media volumes, and environment-based configuration.

However, a production deployment should still be hardened before public exposure.

Important areas include:

Security
├── DEBUG=False
├── strong SECRET_KEY
├── restricted ALLOWED_HOSTS
├── HTTPS
├── secure cookies
└── CSRF configuration

Infrastructure
├── database backups
├── media backups
├── log management
├── monitoring
└── health checks

Networking
├── avoid public Redis exposure
├── restrict database access
└── firewall unnecessary ports

---

📊 Operational Commands

Show containers:

docker ps

Show all containers:

docker ps -a

Show images:

docker images

Show volumes:

docker volume ls

Show networks:

docker network ls

Show resource usage:

docker stats

---

🧹 Stop the Environment

docker compose down

For staging:

docker compose -f docker-compose-stage.yml down

To remove volumes:

docker compose -f docker-compose-stage.yml down -v

«⚠️ Removing volumes can permanently remove stored data. Use "-v" only when you understand exactly what is stored inside those volumes.»

---

🗺️ Development Roadmap

The project already provides a strong advanced-Django foundation.

Natural next steps include:

Infrastructure

- [ ] Production-grade PostgreSQL configuration
- [ ] HTTPS automation
- [ ] Health checks
- [ ] Reverse-proxy hardening
- [ ] Structured logging

Async Processing

- [ ] Dedicated Celery worker service
- [ ] Dedicated Celery Beat service
- [ ] Flower monitoring

Quality

- [ ] Expanded API test coverage
- [ ] Integration tests
- [ ] Coverage reporting
- [ ] Security scanning

CI/CD

- [ ] Docker image publishing
- [ ] Staging deployment automation
- [ ] Production deployment pipeline
- [ ] Automated rollback

Observability

- [ ] Sentry
- [ ] Prometheus
- [ ] Grafana
- [ ] Centralized logs

Scaling

- [ ] Multiple Gunicorn replicas
- [ ] External/object storage for media
- [ ] Managed Redis
- [ ] Managed PostgreSQL
- [ ] Load balancing

---

🧭 Engineering Philosophy

The architecture can be understood as a gradual evolution:

Django Website
      │
      ▼
Django + REST API
      │
      ▼
Authentication
      │
      ▼
Redis Caching
      │
      ▼
Celery Background Tasks
      │
      ▼
Testing + Linting
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
Production Platform

The value of the project is not any single technology.

It is the combination of these technologies into one coherent backend engineering workflow.

---

📚 Learning Map

This repository can be used as a practical study path:

01. Django Fundamentals
        ↓
02. Models and Applications
        ↓
03. Class-Based Views
        ↓
04. Authentication
        ↓
05. Django REST Framework
        ↓
06. JWT / Token APIs
        ↓
07. API Documentation
        ↓
08. Redis Caching
        ↓
09. Celery
        ↓
10. Periodic Tasks
        ↓
11. Testing
        ↓
12. Code Quality
        ↓
13. Load Testing
        ↓
14. Docker
        ↓
15. Gunicorn + Nginx
        ↓
16. CI
        ↓
17. Production Engineering

---

🤝 Contributing

Contributions, improvements, bug fixes, documentation updates, and test improvements are welcome.

Before opening a pull request:

pytest .

flake8 .

black .

and verify that the Docker environment can start successfully.

---

📜 License

This project is released under the MIT License.

See:

LICENSE

for the complete license text.

---

👨‍💻 Author

Amir Khodaei

GitHub:

https://github.com/amirkhodaei1

Repository:

https://github.com/amirkhodaei1/django_advance_blog

---

⭐ Project Status

This repository is an evolving advanced Django project.

It currently combines:

Django
├── Blog
├── Custom User Model
├── REST API
├── Authentication
├── JWT
├── API Documentation
├── Redis Cache
├── Celery
├── Celery Beat
├── Pytest
├── Flake8
├── Black
├── Locust
├── Docker
├── Gunicorn
├── Nginx
└── GitHub Actions

The project is structured as a practical backend engineering environment rather than a minimal demo application.

---

🚀 Why This Repository?

A typical Django tutorial may stop at:

Model → View → Template

This project goes further:

                         ┌──────────────┐
                         │    Django    │
                         └──────┬───────┘
                                │
              ┌─────────────────┼─────────────────┐
              │                 │                 │
              ▼                 ▼                 ▼
          REST API         Authentication       Templates
              │                 │
              ▼                 ▼
             JWT              Djoser
              │
              └────────────┬────────────┘
                           ▼
                         Redis
                      ┌────┴────┐
                      ▼         ▼
                   Cache      Celery
                                │
                                ▼
                           Celery Beat

Docker
  │
  ├── Backend
  ├── Redis
  └── Nginx

Quality
  ├── Pytest
  ├── Flake8
  └── Black

Performance
  └── Locust

Automation
  └── GitHub Actions

The result is a project that demonstrates not only how to write a Django application, but also how the application fits into a broader backend engineering and deployment ecosystem.

---

Built with Django. Tested with Pytest. Accelerated by Redis. Powered by Celery. Containerized with Docker. Served by Gunicorn and Nginx. Automated with GitHub Actions.