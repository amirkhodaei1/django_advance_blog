# 🚀 Django Advance Blog

<p align="center">
  <strong>An Enterprise-Grade, Full-Stack Django Backend Architecture & Asynchronous System Playground</strong>
</p>

<p align="center">
  <a href="https://github.com/amirkhodaei1/django_advance_blog">
    <img src="https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github" alt="GitHub">
  </a>
  <img src="https://img.shields.io/badge/Django-6.0-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django">
  <img src="https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/DRF-3.15-A30000?style=for-the-badge&logo=django&logoColor=white" alt="DRF">
  <img src="https://img.shields.io/badge/Redis-Cache%20%26%20Broker-DC382D?style=for-the-badge&logo=redis&logoColor=white" alt="Redis">
  <img src="https://img.shields.io/badge/Celery-Async%20Tasks-37814A?style=for-the-badge&logo=celery&logoColor=white" alt="Celery">
  <img src="https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">
  <img src="https://img.shields.io/badge/Nginx-Reverse%20Proxy-009639?style=for-the-badge&logo=nginx&logoColor=white" alt="Nginx">
</p>

---

## 📌 Executive Summary

**Django Advance Blog** is a production-grade backend engineering reference architecture designed to demonstrate how a monolithic Django application seamlessly evolves into an asynchronous, cached, API-driven, and fully containerized distributed system.

Moving beyond basic CRUD mechanics, this project bridges core software development with enterprise systems engineering—integrating **JWT authentication**, **Redis distributed caching**, **Celery asynchronous task queues**, **Locust performance load testing**, **Docker container orchestration**, and **automated GitHub Actions CI/CD pipelines**.

---

## 🏛️ System Architecture

The infrastructure employs a decoupled, multi-layered design. Inbound traffic is handled by Nginx, routed through Gunicorn to the application layer, and backed by isolated in-memory stores and async worker queues.

```text
                                 ┌────────────────────────┐
                                 │     Client Request     │
                                 └───────────┬────────────┘
                                             │
                                             ▼
                                 ┌────────────────────────┐
                                 │      Nginx Proxy       │
                                 │  Static / Media / TLS  │
                                 └───────────┬────────────┘
                                             │
                                             ▼
                                 ┌────────────────────────┐
                                 │     Gunicorn WSGI      │
                                 │   App Server Cluster   │
                                 └───────────┬────────────┘
                                             │
                                             ▼
                                 ┌────────────────────────┐
                                 │      Django Core       │
                                 │   REST APIs / Models   │
                                 └─────┬────────────┬─────┘
                                       │            │
                     ┌─────────────────┘            └─────────────────┐
                     ▼                                                ▼
┌──────────────────────────────────────────┐        ┌───────────────────────────────────┐
│                 Redis                    │        │             Database              │
│   ├── DB 1: Celery Broker                │        │  SQLite (Dev) / PostgreSQL (Prod) │
│   └── DB 2: Django System Cache          │        └───────────────────────────────────┘
└────────────────────┬─────────────────────┘
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
┌──────────────────┐   ┌───────────────────┐
│  Celery Worker   │   │    Celery Beat    │
│ Async Processing │   │ Periodic Schedule │
└──────────────────┘   └───────────────────┘
```
✨ Feature Matrix
| Architectural Layer | Capabilities & Standards | Tech Stack |
|---|---|---|
| Core Framework | Custom User Model (accounts.User), Modular Apps, CBVs, Namespaced URLs | Django 6.x, Python 3.12 |
| API Platform | Versioned RESTful API Architecture (v1), Serializers, OpenAPI Spec | Django REST Framework 3.15 |
| Authentication | JWT (SimpleJWT), Token Auth, Session Auth, Basic Auth, Djoser integration | SimpleJWT, Djoser |
| Data Filtering | Advanced URL Filtering, Search Vectoring, Pagination Control | django-filter |
| Caching Layer | Low-latency in-memory query & response caching backed by Redis | django-redis, Redis |
| Async Processing | Distributed Background Queues, Scheduled & Periodic Workflows | Celery, Celery Beat |
| Quality & QA | Automated Unit/Integration Tests, PEP8 Linter, Auto-Formatter | Pytest, Flake8, Black |
| Load Testing | Distributed User Simulation, Latency Analysis, Bottleneck Detection | Locust |
| Containerization | Isolated Environments, Multi-stage Builds, Unified Compose Topology | Docker, Docker Compose |
| Web Gateway | WSGI Server Clustering, Static File Delivery, Reverse Proxying | Gunicorn, Nginx |
| Automation | Continuous Integration Pipeline with Automated Quality Gates | GitHub Actions |
📂 Repository Structure
django_advance_blog/
├── .github/
│   └── workflows/
│       └── docker-image.yml       # CI/CD Pipeline (Flake8 + Pytest execution)
├── core/                          # Main Application Workspace
│   ├── accounts/                  # Authentication & custom user domain
│   ├── blog/                      # Core business domain & API endpoints
│   │   └── api/
│   │       └── v1/                # Versioned serializers, views, and routes
│   ├── core/                      # Project configuration (settings, WSGI, ASGI)
│   ├── locust/                    # Load-testing scenarios & performance suites
│   ├── static/                    # Application static assets
│   ├── manage.py                  # Django CLI entrypoint
│   ├── pytest.ini                 # Pytest configuration file
│   └── .flake8                    # Code style & linting rules
├── templates/                     # Global HTML templates
├── Dockerfile                     # Multi-stage Python 3.12 build image
├── docker-compose.yml             # Local development compose file
├── docker-compose-stage.yml       # Staging & production topology
├── default.conf                   # Nginx reverse proxy server block
├── requirements.txt               # Locked project dependencies
└── README.md                      # Project documentation

🌐 API Ecosystem & Routing
The system automatically parses route metadata into interactive OpenAPI specs accessible through multiple UI engines.
                    ┌────────────────────────┐
                    │    Django REST API     │
                    └───────────┬────────────┘
                                │
                                ▼
                    ┌────────────────────────┐
                    │ OpenAPI Schema Engine  │
                    └─────┬────────────┬─────┘
                          │            │
                          ▼            ▼
                    ┌──────────┐  ┌──────────┐
                    │ Swagger  │  │  ReDoc   │
                    └──────────┘  └──────────┘

Primary System Endpoints
| Route | Interface / Format | Purpose | Access Control |
|---|---|---|---|
| /admin/ | Django Admin UI | Administrative Panel | Staff / Superuser |
| /blog/api/v1/ | JSON / REST API | Versioned Blog API Endpoints | Public / Authenticated |
| /swagger/ | Interactive Swagger UI | OpenAPI Interactive API Documentation | Public |
| /redoc/ | ReDoc UI | Structured API Schema Visualization | Public |
| /swagger/output.json | JSON Schema | Raw OpenAPI 2.0/3.0 Specification | System / Public |
| /api-docs/ | DRF Native UI | Browsable API Explorer | Developer |
⚡ Redis & Asynchronous Infrastructure
Distributed Database Allocation
 * Redis DB 1: Designated as the Celery Task Broker (redis://redis:6379/1).
 * Redis DB 2: Dedicated as the Low-Latency System Cache (redis://redis:6379/2).
Asynchronous Workflow Execution
Client Request  ──►  Django API View  ──►  Push Job to Redis Broker (DB 1)
                                                       │
                                                       ▼
Client Receives HTTP 202 Accepted  ◄──  Celery Worker Picks Up & Executes Job

🚀 Quick Start Guide
Prerequisites
 * Docker (v24.0+)
 * Docker Compose (v2.20+)
 * Git
1. Clone the Repository
git clone [https://github.com/amirkhodaei1/django_advance_blog.git](https://github.com/amirkhodaei1/django_advance_blog.git)
cd django_advance_blog

2. Launch Containerized Stack
Spin up the full infrastructure (Nginx, Gunicorn, Django, Redis, Celery) in detached mode:
docker compose -f docker-compose-stage.yml up -d --build

3. Initialize Database & Static Assets
Execute migrations, collect static files, and set up an administrator:
# Run database migrations
docker compose exec backend python manage.py migrate

# Collect static assets for Nginx
docker compose exec backend python manage.py collectstatic --noinput

# Create superuser account
docker compose exec backend python manage.py createsuperuser

Access the application at http://localhost.
🛠️ CLI Operations & Debugging Matrix
Quality Assurance & Testing
# Run test suite inside Docker
docker compose exec backend pytest .

# Run Flake8 linter
docker compose exec backend flake8 .

# Check code formatting compliance
docker compose exec backend black --check .

System Inspection & Shells
# Open interactive Django Shell
docker compose exec backend python manage.py shell

# Stream live container logs
docker compose -f docker-compose-stage.yml logs -f backend

# Validate Nginx configuration
docker compose exec nginx nginx -t

Performance & Load Testing
Simulate high-concurrency traffic using Locust:
docker compose exec backend locust -f locust/locustfile.py --host=http://localhost:8000

🛡️ Production Security Hardening Checklist
 * [ ] Environment Configuration: Replace python-decouple default values with encrypted production secrets.
 * [ ] SSL/TLS Termination: Configure HTTPS certificates via Let's Encrypt / Certbot inside Nginx.
 * [ ] Restrict CORS & Hosts: Set strict domain bounds in ALLOWED_HOSTS and CORS_ALLOWED_ORIGINS.
 * [ ] Persistent Database: Swap local SQLite for a managed PostgreSQL instance with connection pooling.
 * [ ] Observability: Integrate Sentry for error tracking and Flower for real-time Celery monitoring.
👨‍💻 Author & Community
Amir Khodaei
 * GitHub: @amirkhodaei1
 * Repository: django_advance_blog
📜 License
Distributed under the MIT License. See LICENSE for full details.
<p align="center">
⭐ <strong>If you find this repository helpful, please consider giving it a star!</strong> ⭐
</p>
