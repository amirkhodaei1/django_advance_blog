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
