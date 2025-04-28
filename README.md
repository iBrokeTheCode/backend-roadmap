# Python Backend Developer Roadmap

> [!TIP]
> Review a related [roadmap](./notes/roadmap/README.md)

## Roadmap

1. **Foundations** (10 h)

   1.1. **Internet Fundamentals** (4 h)  
   &nbsp;&nbsp;- Domain names & DNS resolution  
   &nbsp;&nbsp;- HTTP/HTTPS protocols & status codes  
   &nbsp;&nbsp;- Hosting basics (shared, VPS, containers)  
   &nbsp;&nbsp;- SSL/TLS & CDN overview

   1.2. **Dev Environment & Tooling** (6 h)  
   &nbsp;&nbsp;- Python versions & virtual environments (`venv`, `pyenv`)  
   &nbsp;&nbsp;- IDEs/editors (VS Code, PyCharm)  
   &nbsp;&nbsp;- Linters & formatters (`flake8`, `black`)  
   &nbsp;&nbsp;- [Dependency management with Poetry](https://github.com/iBrokeTheCode/python-roadmap/blob/main/Tools/poetry.md)

2. **Python Core** (40 h)

   2.1. **Syntax, Data Types & Control Flow** (8 h)  
   &nbsp;&nbsp;- [Variables, numbers, strings, booleans](https://github.com/iBrokeTheCode/python-roadmap/blob/main/Fundamentals/Variables_Types_Operators.md)  
   &nbsp;&nbsp;- [Lists](https://github.com/iBrokeTheCode/python-roadmap/blob/main/Fundamentals/Lists/Lists.md), [tuples](https://github.com/iBrokeTheCode/python-roadmap/blob/main/Fundamentals/Tuples/Tuples.md), [sets](https://github.com/iBrokeTheCode/python-roadmap/blob/main/Fundamentals/Sets/Sets.md), [dicts](https://github.com/iBrokeTheCode/python-roadmap/blob/main/Fundamentals/Dicts/Dicts.md)  
   &nbsp;&nbsp;- [`if`/`elif`/`else`, loops (`for`/`while`)](https://github.com/iBrokeTheCode/python-roadmap/blob/main/Fundamentals/Control_Flow.md)

   2.2. **Functions, Modules & Packages** (8 h)  
   &nbsp;&nbsp;- [Defining functions, args/kwargs](https://github.com/iBrokeTheCode/python-roadmap/blob/main/Fundamentals/Functions/Advanced_Functions.md)  
   &nbsp;&nbsp;- [`import` system, creating packages](https://github.com/iBrokeTheCode/python-roadmap/blob/main/Standard_Library_Modules/Modules_Packages/Modules_Packages.md)

   2.3. **OOP in Python** (8 h)  
   &nbsp;&nbsp;- [Classes, instances, methods](https://github.com/iBrokeTheCode/python-roadmap/blob/main/OOP/OOP_Pillars.md#1-classes--objects)  
   &nbsp;&nbsp;- [Inheritance, polymorphism, encapsulation](https://github.com/iBrokeTheCode/python-roadmap/blob/main/OOP/OOP_Pillars.md#3-encapsulation-inheritance-polymorphism-abstraction)

   2.4. **Working with Files & Data** (8 h)  
   &nbsp;&nbsp;- `pathlib` & [file I/O](https://github.com/iBrokeTheCode/python-roadmap/blob/main/Standard_Library_Modules/Files_IO/Files_IO.md)  
   &nbsp;&nbsp;- [JSON serialization/deserialization](https://github.com/iBrokeTheCode/python-roadmap/blob/main/Standard_Library_Modules/Core_Modules/JSON/JSON.md)  
   &nbsp;&nbsp;- [`argparse` for CLI scripts](https://github.com/iBrokeTheCode/python-roadmap/blob/main/Standard_Library_Modules/Core_Modules/Argparse/Argparse.md)

   2.5. **Advanced Python Features** (8 h)  
   &nbsp;&nbsp;- [List comprehension](https://github.com/iBrokeTheCode/python-roadmap/blob/main/Fundamentals/Lists/Lists.md#list-comprehension) & [Dict comprehension](https://github.com/iBrokeTheCode/python-roadmap/blob/main/Fundamentals/Dicts/Dicts.md#dictionary-comprehensions)  
   &nbsp;&nbsp;- [Generators & iterators](https://github.com/iBrokeTheCode/python-roadmap/blob/main/Advanced/Generators_and_Iterators/Generators_and_Iterators.md)  
   &nbsp;&nbsp;- [Context managers (`with`)](https://github.com/iBrokeTheCode/python-roadmap/blob/main/Advanced/Context_Managers/Context_Managers.md)

3. **Version Control** (8 h)

   3.1. **Git Basics** (4 h)  
   &nbsp;&nbsp;- [`git init`/`clone`/`add`/`commit`](https://github.com/ibrokethecode/git-tutorial?tab=readme-ov-file#-basic-commands)  
   &nbsp;&nbsp;- [Branching & merging](https://github.com/ibrokethecode/git-tutorial?tab=readme-ov-file#-branching)

   3.2. **Remote Repos** (2 h)  
   &nbsp;&nbsp;- [Git Flow](https://github.com/ibrokethecode/git-tutorial?tab=readme-ov-file#git-flow)  
   &nbsp;&nbsp;- [GitHub/GitLab workflows](https://github.com/ibrokethecode/git-tutorial?tab=readme-ov-file#github-flow)  
   &nbsp;&nbsp;- [Pull/Merge requests](https://github.com/ibrokethecode/git-tutorial?tab=readme-ov-file#-pull-requests-prs)

   3.3. **Advanced Git** (2 h)  
   &nbsp;&nbsp;- Rebasing & interactive rebase  
   &nbsp;&nbsp;- Hooks & submodules

4. **Databases** (20 h)

   4.1. **Relational & SQL Primer** (6 h)  
   &nbsp;&nbsp;- CRUD operations  
   &nbsp;&nbsp;- Joins, aggregations, subqueries

   4.2. **PostgreSQL Deep Dive** (10 h)  
   &nbsp;&nbsp;- Schemas, indexes, constraints  
   &nbsp;&nbsp;- Transactions & isolation levels  
   &nbsp;&nbsp;- Extensions (PostGIS, pgcrypto)

   4.3. **NoSQL Overview (MongoDB basics)** (4 h)  
   &nbsp;&nbsp;- Document model & CRUD  
   &nbsp;&nbsp;- When to choose NoSQL

5. **ORM & Data Migrations** (12 h)

   5.1. **Django**  
   &nbsp;&nbsp;- [Django Fundamentals](./notes/django/README.md)

   5.2. **Django ORM Fundamentals** (6 h)  
   &nbsp;&nbsp;- [ORM Deep Dive](https://github.com/ibrokethecode/orm-deep-dive?tab=readme-ov-file#orm-deep-dive-tutorial)  
   &nbsp;&nbsp;- [Models, querysets, managers](https://github.com/iBrokeTheCode/orm-deep-dive/blob/main/notes/lesson-02.md)  
   &nbsp;&nbsp;- [M2M Relationships](https://github.com/iBrokeTheCode/orm-deep-dive/blob/main/notes/lesson-08.md) & [Foreign Keys](https://github.com/iBrokeTheCode/orm-deep-dive/blob/main/notes/lesson-03.md)  
   &nbsp;&nbsp;- [Lookups](https://github.com/iBrokeTheCode/orm-deep-dive/blob/main/notes/lesson-06.md)

   5.3. **SQLModel & Alembic (FastAPI)** (4 h)  
   &nbsp;&nbsp;- Defining models  
   &nbsp;&nbsp;- Auto‑generating migrations

   5.4. **Migrations & Seeding** (2 h)  
   &nbsp;&nbsp;- [`makemigrations`/`migrate`](https://github.com/iBrokeTheCode/orm-deep-dive/blob/main/notes/lesson-02.md)  
   &nbsp;&nbsp;- Fixtures & seed scripts

6. **Building REST APIs** (20 h)

   6.1. **REST Principles & JSON** (4 h)  
   &nbsp;&nbsp;- Resources, verbs, status codes  
   &nbsp;&nbsp;- JSON schemas & validation

   6.2. **Django REST Framework** (8 h)

   &nbsp;&nbsp;- [Django REST Framework Deep Dive](https://github.com/iBrokeTheCode/django-rest-framework)  
   &nbsp;&nbsp;- [Serializers](https://github.com/iBrokeTheCode/django-rest-framework/blob/main/notes/lesson-02.md) & [ModelViewSets, GenericViews](https://github.com/iBrokeTheCode/django-rest-framework/blob/main/notes/lesson-06.md)  
   &nbsp;&nbsp;- [Routers & URL conf](https://github.com/iBrokeTheCode/django-rest-framework/blob/main/notes/lesson-20.md)  
   &nbsp;&nbsp;- [Browsable API](https://github.com/iBrokeTheCode/django-rest-framework/blob/main/notes/lesson-02.md) & [permissions](https://github.com/iBrokeTheCode/django-rest-framework/blob/main/notes/lesson-08.md)

   6.3. **FastAPI** (8 h)  
   &nbsp;&nbsp;- Path/Query/Body parameters  
   &nbsp;&nbsp;- Dependency injection  
   &nbsp;&nbsp;- OpenAPI docs & validation

7. **Authentication & Authorization** (12 h)

   7.1. **Session‑based Auth** (2 h)  
   &nbsp;&nbsp;- Django’s built‑in system

   7.2. **Token‑based Auth** (4 h)  
   &nbsp;&nbsp;- [DRF Token Auth](https://github.com/iBrokeTheCode/django-rest-framework/blob/main/notes/lesson-12.md)  
   &nbsp;&nbsp;- FastAPI OAuth2 password flow

   7.3. **JWT & OAuth2** (6 h)  
   &nbsp;&nbsp;- JWT structure & security  
   &nbsp;&nbsp;- Refresh tokens & revocation  
   &nbsp;&nbsp;- Third‑party OAuth (Google, GitHub)

8. **Testing** (12 h)

   8.1. **Unit Testing with pytest** (4 h)  
   &nbsp;&nbsp;- [Introduction to Pytest and Unittest](https://github.com/iBrokeTheCode/python-roadmap/blob/main/testing/Unit_Testing.md)  
   &nbsp;&nbsp;- Fixtures, parametrization

   8.2. **Integration Tests** (4 h)  
   &nbsp;&nbsp;- Testing DB interactions  
   &nbsp;&nbsp;- API endpoint tests

   8.3. **End‑to‑End & Acceptance** (4 h)  
   &nbsp;&nbsp;- Selenium / Playwright basics  
   &nbsp;&nbsp;- CI integration

9. **CI/CD & Automation** (10 h)

   9.1. **GitHub Actions / GitLab CI** (4 h)  
   &nbsp;&nbsp;- Writing workflow YAML  
   &nbsp;&nbsp;- Matrix builds & caching

   9.2. **Automated Testing & Linting** (3 h)  
   &nbsp;&nbsp;- Running pytest, flake8, mypy

   9.3. **Deployment Pipelines** (3 h)  
   &nbsp;&nbsp;- Build → Test → Deploy steps  
   &nbsp;&nbsp;- Notifications & rollbacks

10. **Advanced Database Topics** (15 h)  
    10.1. **ACID & Isolation** (4 h)  
    10.2. **[N+1 Problem](https://github.com/iBrokeTheCode/orm-deep-dive/blob/main/notes/lesson-07.md#n1-problem) & [Query Optimization](https://github.com/iBrokeTheCode/orm-deep-dive/blob/main/notes/lesson-07.md)** (4 h)  
    10.3. **Indexing Strategies** (4 h)  
    10.4. **Normalization & Denormalization** (3 h)

11. **Scaling Databases** (10 h)  
    11.1. **Read/Write Replication** (4 h)  
    11.2. **Sharding & Partitioning** (3 h)  
    11.3. **Connection Pooling** (3 h)

12. **Software Architecture & Patterns** (15 h)  
    12.1. **Monolith & Modular Monolith** (3 h)  
    12.2. **Microservices Overview** (3 h)  
    12.3. **Common Design Patterns** (9 h)  
    &nbsp;&nbsp;- Factory  
    &nbsp;&nbsp;- Repository  
    &nbsp;&nbsp;- Observer  
    &nbsp;&nbsp;- Strategy  
    &nbsp;&nbsp;- etc.

13. **Development Principles** (10 h)  
    13.1. **Test‑Driven Development (TDD)** (4 h)  
    13.2. **Domain‑Driven Design (DDD) Basics** (4 h)  
    13.3. **SOLID & Clean Code** (2 h)

14. **Containerization & Deployment** (15 h)  
    14.1. **Docker Basics** (6 h)  
    &nbsp;&nbsp;- [Docker](./notes/containers/docker/README.md)  
    &nbsp;&nbsp;- [Fundamentals](./notes/containers/docker/lesson-02.md)  
    &nbsp;&nbsp;- Images, containers, volumes, networks  
    &nbsp;&nbsp;- [Podman](./notes/containers/podman/README.md)

    14.2. **Docker Compose** (4 h)  
    &nbsp;&nbsp;- Multi‑service setups

    14.3. **Cloud Deployment** (5 h)  
    &nbsp;&nbsp;- Heroku, AWS ECS, DigitalOcean App Platform

15. **Monitoring & Observability** (10 h)  
    15.1. **Logging Best Practices** (3 h)  
    15.2. **Metrics & Health Checks** (4 h)  
    15.3. **Distributed Tracing & Alerts** (3 h)

16. **Next Steps & Advanced Topics** (15 h)  
    16.1. **Caching (Redis, CDN)** (4 h)  
    16.2. **Message Brokers (RabbitMQ, Kafka)** (4 h)  
    16.3. **Search Engines (Elasticsearch)** (3 h)  
    16.4. **Real‑Time & WebSockets** (4 h)

**Total Estimated Time: 234 hours**
