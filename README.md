🚀 Django Advance Blog
<p align="center">
<strong>An Enterprise-Grade, Full-Stack Django Backend Architecture & Asynchronous System</strong>
</p>
<p align="center">
<a href="[https://github.com/amirkhodaei1/django_advance_blog](https://github.com/amirkhodaei1/django_advance_blog)">
<img src="[https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github)" alt="GitHub">
</a>
<img src="[https://img.shields.io/badge/Django-6.0-092E20?style=for-the-badge&logo=django&logoColor=white](https://img.shields.io/badge/Django-6.0-092E20?style=for-the-badge&logo=django&logoColor=white)" alt="Django">
<img src="[https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)" alt="Python">
<img src="[https://img.shields.io/badge/DRF-3.15-A30000?style=for-the-badge&logo=django](https://img.shields.io/badge/DRF-3.15-A30000?style=for-the-badge&logo=django)" alt="DRF">
<img src="[https://img.shields.io/badge/Redis-Cache%20%2B%20Broker-DC382D?style=for-the-badge&logo=redis&logoColor=white](https://img.shields.io/badge/Redis-Cache%20%2B%20Broker-DC382D?style=for-the-badge&logo=redis&logoColor=white)" alt="Redis">
<img src="[https://img.shields.io/badge/Celery-5.6-37814A?style=for-the-badge&logo=celery&logoColor=white](https://img.shields.io/badge/Celery-5.6-37814A?style=for-the-badge&logo=celery&logoColor=white)" alt="Celery">
<img src="[https://img.shields.io/badge/Docker-Compose-2496ED?style=for-the-badge&logo=docker&logoColor=white](https://img.shields.io/badge/Docker-Compose-2496ED?style=for-the-badge&logo=docker&logoColor=white)" alt="Docker">
<img src="[https://img.shields.io/badge/Nginx-Reverse%20Proxy-009639?style=for-the-badge&logo=nginx&logoColor=white](https://img.shields.io/badge/Nginx-Reverse%20Proxy-009639?style=for-the-badge&logo=nginx&logoColor=white)" alt="Nginx">
<img src="[https://img.shields.io/badge/Gunicorn-WSGI-499848?style=for-the-badge&logo=gunicorn&logoColor=white](https://img.shields.io/badge/Gunicorn-WSGI-499848?style=for-the-badge&logo=gunicorn&logoColor=white)" alt="Gunicorn">
</p>
📌 Executive Summary
Django Advance Blog is a production-oriented reference architecture designed to demonstrate how a monolithic Django application scales into an asynchronous, cached, API-first microservices-ready backend system.
Rather than focusing merely on simple CRUD operations, this playground bridges fundamental software development with production backend engineering—incorporating JWT authentication, Redis distributed caching, Celery task queues, Locust performance load testing, Docker orchestration, and automated CI/CD pipelines.
🏛️ System Architecture
The project implements a layered backend infrastructure. Incoming traffic flows through a hardened reverse proxy down to asynchronous worker nodes and persistent data stores.
                         ┌─────────────────────────────────┐
                         │         Client Request          │
                         └────────────────┬────────────────┘
                                          │
                                          ▼
                         ┌─────────────────────────────────┐
                         │          Nginx Proxy            │
                         │   Static / Media / Rate Limit   │
                         └────────────────┬────────────────┘
                                          │
                                          ▼
                         ┌─────────────────────────────────┐
                         │         Gunicorn WSGI           │
                         │    Application Server Cluster   │
                         └────────────────┬────────────────┘
                                          │
                                          ▼
                         ┌─────────────────────────────────┐
                         │          Django Core            │
                         │    REST API / ORM / Business    │
                         └────────┬──────────────┬─────────┘
                                  │              │
                   ┌──────────────┘              └──────────────┐
                   ▼                                            ▼
┌────────────────────────────────────┐        ┌──────────────────────────────────┐
│             Redis                  │        │             Database             │
│  ├── DB 1: Celery Broker           │        │    SQLite (Dev) / PostgreSQL     │
│  └── DB 2: Django Cache            │        └──────────────────────────────────┘
└──────────────────┬─────────────────┘
                   │
         ┌─────────┴─────────┐
         ▼                   ▼
┌─────────────────┐ ┌──────────────────┐
│  Celery Worker  │ │   Celery Beat    │
│ Async Task Exec │ │ Scheduler Daemon │
└─────────────────┘ └──────────────────┘

✨ Core Feature Matrix
| Domain | Engineering Capability | Key Technologies & Implementations |
|---|---|---|
| Architecture | Scalable Modular Design | Custom User Model (accounts.User), Namespaced Routing, CBVs |
| API Engine | Versioned RESTful Web Services | DRF v1 API, Filtering (django-filter), Djoser Management |
| Security & Auth | Multi-Strategy Authentication | JWT (SimpleJWT), Session, Token, Basic Auth, CORS control |
| Caching | In-Memory Data Optimization | django-redis backend configured on dedicated Redis instance |
| Async & Tasks | Background & Scheduled Processing | Celery Workers, Celery Beat Scheduler, Redis Broker |
| Quality & QA | Testing & Code Formatting | pytest-django, Flake8 linting, Black auto-formatting |
| Performance | Distributed Load Testing | Locust load testing scenarios for latency & throughput audits |
| Deployment | Production Container Orchestration | Docker, Docker Compose, Gunicorn WSGI, Nginx Reverse Proxy |
📂 Repository Structure
django_advance_blog/
├── .github/
│   └── workflows/
│       └── docker-image.yml     # Automated CI pipeline (Flake8 + Pytest)
├── core/                        # Main Application Root
│   ├── accounts/                # User management & custom auth domain
│   ├── blog/                    # Main business domain & API resources
│   │   └── api/
│   │       └── v1/              # Versioned API routes & serializers
│   ├── core/                    # System settings, WSGI/ASGI configurations
│   ├── locust/                  # Load testing suites & user scenarios
│   ├── static/                  # Collected static assets
│   ├── manage.py                # Django CLI entrypoint
│   ├── pytest.ini               # Pytest test-runner config
│   └── .flake8                  # Linting style guide rules
├── templates/                   # Global HTML templates
├── Dockerfile                   # Multi-stage Python 3.12 build image
├── docker-compose-stage.yml     # Staging/Production service topology
├── default.conf                 # Nginx server block & proxy settings
├── requirements.txt             # Locked Python dependencies
└── README.md                    # Project documentation

🌐 API Documentation & Endpoint Map
The project dynamically generates OpenAPI 2.0/3.0 schema specs and exposes multiple UI interfaces for API discovery and testing.
       ┌────────────────────────┐
       │     Django REST API    │
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

Key API & System Routes
| Endpoint | Access / Interface | Description |
|---|---|---|
| /admin/ | Staff Only | Django Administrative Panel |
| /blog/api/v1/ | Public / Token / JWT | Versioned RESTful API for blog resources |
| /swagger/ | Interactive UI | Swagger UI for API testing and inspection |
| /redoc/ | Readable Schema | ReDoc formatted API documentation |
| /swagger/output.json | JSON File | Raw OpenAPI JSON Specification |
| /api-docs/ | DRF Native UI | Django REST Framework native API viewer |
⚡ Asynchronous Engine & Caching
Redis Memory Allocation Architecture
 * Redis Database 1: Celery Task Broker (redis://redis:6379/1)
 * Redis Database 2: Django System Cache (redis://redis:6379/2)
Background Task Execution Flow
Client HTTP Request  ──►  Django View  ──►  Enqueue Task to Redis (DB 1)
                                                     │
                                                     ▼
Client Receives 202 Accepted ◄── Celery Worker Executes Task Asynchronously

🚀 Quick Start & Container Setup
1. Prerequisites
 * Docker (v24.0+)
 * Docker Compose (v2.20+)
 * Git
2. Clone & Environment Setup
git clone https://github.com/amirkhodaei1/django_advance_blog.git
cd django_advance_blog

3. Spin Up Staging Infrastructure
Start the entire stack (Nginx, Gunicorn, Django, Redis, Celery) in detached mode:
docker compose -f docker-compose-stage.yml up -d --build

4. Database Setup & Static Collection
Execute migrations and collect static files within the running container:
# Run database migrations
docker compose exec backend python manage.py migrate

# Collect static assets for Nginx
docker compose exec backend python manage.py collectstatic --noinput

# Create an administrative superuser
docker compose exec backend python manage.py createsuperuser

🧪 Testing, Code Quality & Load Audits
Run Automated Unit & Integration Tests
docker compose exec backend pytest .

Code Formatting & Style Checks
# Run Flake8 linter
docker compose exec backend flake8 .

# Check Black formatting compliance
docker compose exec backend black --check .

Performance & Load Testing with Locust
Run Locust to simulate concurrent user traffic and measure latency bounds:
docker compose exec backend locust -f locust/locustfile.py --host=http://localhost:8000

🛡️ Production Hardening Checklist
 * [ ] Secrets Security: Replace python-decouple fallback values with production environment variables.
 * [ ] HTTPS Enforcement: Terminate SSL/TLS at Nginx or cloud load balancer level.
 * [ ] Strict CORS/CSRF: Restrict CORS_ALLOW_ALL_ORIGINS to trusted frontend domains.
 * [ ] Persistent Database: Migrate from SQLite to a managed PostgreSQL service.
 * [ ] Monitoring & Alerts: Integrate Flower for Celery monitoring and Sentry for error tracking.
👨‍💻 Author & Contribution
Amir Khodaei
 * GitHub: @amirkhodaei1
 * Repository: django_advance_blog
Contributions, bug reports, and optimizations are always welcome! Feel free to open an Issue or pull request.
