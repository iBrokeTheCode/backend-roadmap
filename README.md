# Python Backend Developer Roadmap

## Related Resources

- [Suggested Roadmap](./notes/roadmap/README.md)
- [Prompts](./notes/prompts/)
- [Python Notes](https://github.com/iBrokeTheCode/python-roadmap)
- [Git Notes](https://github.com/ibrokethecode/git-tutorial)
- [Django Notes](./notes/django/README.md)
- [Django ORM Notes](https://github.com/ibrokethecode/orm-deep-dive?tab=readme-ov-file#orm-deep-dive-tutorial)
- [Django REST Framework](https://github.com/iBrokeTheCode/django-rest-framework)
- [FastAPI Notes](https://github.com/iBrokeTheCode/fastapi-course)
- [Docker Notes](https://github.com/iBrokeTheCode/backend-roadmap/blob/main/notes/containers/docker/README.md)

## Roadmap

1. **Foundations**

   1.1. **Internet Fundamentals**  
   &nbsp;&nbsp;- Domain names & DNS resolution  
   &nbsp;&nbsp;- HTTP/HTTPS protocols & status codes  
   &nbsp;&nbsp;- Hosting basics (shared, VPS, containers)  
   &nbsp;&nbsp;- SSL/TLS & CDN overview

   1.2. **Dev Environment & Tooling**  
   &nbsp;&nbsp;- Python versions & virtual environments (`venv`, `pyenv`)  
   &nbsp;&nbsp;- IDEs/editors (VS Code, PyCharm)  
   &nbsp;&nbsp;- Linters & formatters (`flake8`, `black`)  
   &nbsp;&nbsp;- [Dependency management with Poetry](https://github.com/iBrokeTheCode/python-roadmap/blob/main/Tools/poetry.md)

2. **Python Core**

   2.1. **Syntax, Data Types & Control Flow**  
   &nbsp;&nbsp;- [Variables, numbers, strings, booleans](https://github.com/iBrokeTheCode/python-roadmap/blob/main/Fundamentals/Variables_Types_Operators.md)  
   &nbsp;&nbsp;- [Lists](https://github.com/iBrokeTheCode/python-roadmap/blob/main/Fundamentals/Lists/Lists.md), [tuples](https://github.com/iBrokeTheCode/python-roadmap/blob/main/Fundamentals/Tuples/Tuples.md), [sets](https://github.com/iBrokeTheCode/python-roadmap/blob/main/Fundamentals/Sets/Sets.md), [dicts](https://github.com/iBrokeTheCode/python-roadmap/blob/main/Fundamentals/Dicts/Dicts.md)  
   &nbsp;&nbsp;- [`if`/`elif`/`else`, loops (`for`/`while`)](https://github.com/iBrokeTheCode/python-roadmap/blob/main/Fundamentals/Control_Flow.md)

   2.2. **Functions, Modules & Packages**  
   &nbsp;&nbsp;- [Defining functions, args/kwargs](https://github.com/iBrokeTheCode/python-roadmap/blob/main/Fundamentals/Functions/Advanced_Functions.md)  
   &nbsp;&nbsp;- [`import` system, creating packages](https://github.com/iBrokeTheCode/python-roadmap/blob/main/Standard_Library_Modules/Modules_Packages/Modules_Packages.md)

   2.3. **OOP in Python**  
   &nbsp;&nbsp;- [Classes, instances, methods](https://github.com/iBrokeTheCode/python-roadmap/blob/main/OOP/OOP_Pillars.md#1-classes--objects)  
   &nbsp;&nbsp;- [Inheritance, polymorphism, encapsulation](https://github.com/iBrokeTheCode/python-roadmap/blob/main/OOP/OOP_Pillars.md#3-encapsulation-inheritance-polymorphism-abstraction)

   2.4. **Working with Files & Data**  
   &nbsp;&nbsp;- `pathlib` & [file I/O](https://github.com/iBrokeTheCode/python-roadmap/blob/main/Standard_Library_Modules/Files_IO/Files_IO.md)  
   &nbsp;&nbsp;- [JSON serialization/deserialization](https://github.com/iBrokeTheCode/python-roadmap/blob/main/Standard_Library_Modules/Core_Modules/JSON/JSON.md)  
   &nbsp;&nbsp;- [`argparse` for CLI scripts](https://github.com/iBrokeTheCode/python-roadmap/blob/main/Standard_Library_Modules/Core_Modules/Argparse/Argparse.md)

   2.5. **Advanced Python Features**  
   &nbsp;&nbsp;- [List comprehension](https://github.com/iBrokeTheCode/python-roadmap/blob/main/Fundamentals/Lists/Lists.md#list-comprehension) & [Dict comprehension](https://github.com/iBrokeTheCode/python-roadmap/blob/main/Fundamentals/Dicts/Dicts.md#dictionary-comprehensions)  
   &nbsp;&nbsp;- [Generators & iterators](https://github.com/iBrokeTheCode/python-roadmap/blob/main/Advanced/Generators_and_Iterators/Generators_and_Iterators.md)  
   &nbsp;&nbsp;- [Context managers (`with`)](https://github.com/iBrokeTheCode/python-roadmap/blob/main/Advanced/Context_Managers/Context_Managers.md)

3. **Version Control**

   3.1. **Git Basics**  
   &nbsp;&nbsp;- [`git init`/`clone`/`add`/`commit`](https://github.com/ibrokethecode/git-tutorial?tab=readme-ov-file#-basic-commands)  
   &nbsp;&nbsp;- [Branching & merging](https://github.com/ibrokethecode/git-tutorial?tab=readme-ov-file#-branching)

   3.2. **Remote Repos**  
   &nbsp;&nbsp;- [Git Flow](https://github.com/ibrokethecode/git-tutorial?tab=readme-ov-file#git-flow)  
   &nbsp;&nbsp;- [GitHub/GitLab workflows](https://github.com/ibrokethecode/git-tutorial?tab=readme-ov-file#github-flow)  
   &nbsp;&nbsp;- [Pull/Merge requests](https://github.com/ibrokethecode/git-tutorial?tab=readme-ov-file#-pull-requests-prs)

   3.3. **Advanced Git**  
   &nbsp;&nbsp;- Rebasing & interactive rebase  
   &nbsp;&nbsp;- Hooks & submodules

4. **Databases**

   4.1. **Relational & SQL Primer**  
   &nbsp;&nbsp;- CRUD operations  
   &nbsp;&nbsp;- Joins, aggregations, subqueries

   4.2. **PostgreSQL Deep Dive**  
   &nbsp;&nbsp;- Schemas, indexes, constraints  
   &nbsp;&nbsp;- Transactions & isolation levels  
   &nbsp;&nbsp;- Extensions (PostGIS, pgcrypto)

   4.3. **NoSQL Overview (MongoDB basics)**  
   &nbsp;&nbsp;- Document model & CRUD  
   &nbsp;&nbsp;- When to choose NoSQL

5. **ORM & Data Migrations**

   5.1. **Django ORM Fundamentals**  
   &nbsp;&nbsp;- [Models, querysets, managers](https://github.com/iBrokeTheCode/orm-deep-dive/blob/main/notes/lesson-02.md)  
   &nbsp;&nbsp;- [M2M Relationships](https://github.com/iBrokeTheCode/orm-deep-dive/blob/main/notes/lesson-08.md) & [Foreign Keys](https://github.com/iBrokeTheCode/orm-deep-dive/blob/main/notes/lesson-03.md)  
   &nbsp;&nbsp;- [Lookups](https://github.com/iBrokeTheCode/orm-deep-dive/blob/main/notes/lesson-06.md)

   5.2. **SQLModel & Alembic (FastAPI)**  
   &nbsp;&nbsp;- Defining models  
   &nbsp;&nbsp;- Auto‑generating migrations

   5.3. **Migrations & Seeding**  
   &nbsp;&nbsp;- [`makemigrations`/`migrate`](https://github.com/iBrokeTheCode/orm-deep-dive/blob/main/notes/lesson-02.md)  
   &nbsp;&nbsp;- Fixtures & seed scripts

6. **Building REST APIs**

   6.1. **REST Principles & JSON**  
   &nbsp;&nbsp;- Resources, verbs, status codes  
   &nbsp;&nbsp;- JSON schemas & validation

   6.2. **Django REST Framework**  
   &nbsp;&nbsp;- [Serializers](https://github.com/iBrokeTheCode/django-rest-framework/blob/main/notes/lesson-02.md) & [ModelViewSets, GenericViews](https://github.com/iBrokeTheCode/django-rest-framework/blob/main/notes/lesson-06.md)  
   &nbsp;&nbsp;- [Routers & URL conf](https://github.com/iBrokeTheCode/django-rest-framework/blob/main/notes/lesson-20.md)  
   &nbsp;&nbsp;- [Browsable API](https://github.com/iBrokeTheCode/django-rest-framework/blob/main/notes/lesson-02.md) & [permissions](https://github.com/iBrokeTheCode/django-rest-framework/blob/main/notes/lesson-08.md)

   6.3. **FastAPI**  
   &nbsp;&nbsp;- [Path/Query/Body parameters](https://github.com/iBrokeTheCode/fastapi-course/blob/main/notes/lesson-01.md)  
   &nbsp;&nbsp;- Dependency injection  
   &nbsp;&nbsp;- OpenAPI docs & validation

7. **Authentication & Authorization**

   7.1. **Session‑based Auth**  
   &nbsp;&nbsp;- Django’s built‑in system

   7.2. **Token‑based Auth**  
   &nbsp;&nbsp;- [DRF Token Auth](https://github.com/iBrokeTheCode/django-rest-framework/blob/main/notes/lesson-12.md)  
   &nbsp;&nbsp;- FastAPI OAuth2 password flow

   7.3. **JWT & OAuth2**  
   &nbsp;&nbsp;- JWT structure & security  
   &nbsp;&nbsp;- Refresh tokens & revocation  
   &nbsp;&nbsp;- Third‑party OAuth (Google, GitHub)

8. **Testing**

   8.1. **Unit Testing with pytest**  
   &nbsp;&nbsp;- [Introduction to Pytest and Unittest](https://github.com/iBrokeTheCode/python-roadmap/blob/main/testing/Unit_Testing.md)  
   &nbsp;&nbsp;- [Django Testing (unittest)](./notes/django/django-testing/)  
   &nbsp;&nbsp;- Fixtures, parametrization

   8.2. **Integration Tests**  
   &nbsp;&nbsp;- Testing DB interactions  
   &nbsp;&nbsp;- API endpoint tests

   8.3. **End‑to‑End & Acceptance**  
   &nbsp;&nbsp;- Selenium / Playwright basics  
   &nbsp;&nbsp;- CI integration

9. **CI/CD & Automation**

   9.1. **GitHub Actions / GitLab CI**  
   &nbsp;&nbsp;- Writing workflow YAML  
   &nbsp;&nbsp;- Matrix builds & caching

   9.2. **Automated Testing & Linting**  
   &nbsp;&nbsp;- Running pytest, flake8, mypy

   9.3. **Deployment Pipelines**  
   &nbsp;&nbsp;- Build → Test → Deploy steps  
   &nbsp;&nbsp;- Notifications & rollbacks

10. **Advanced Database Topics**  
    10.1. **ACID & Isolation**  
    10.2. **[N+1 Problem](https://github.com/iBrokeTheCode/orm-deep-dive/blob/main/notes/lesson-07.md#n1-problem) & [Query Optimization](https://github.com/iBrokeTheCode/orm-deep-dive/blob/main/notes/lesson-07.md)**  
    10.3. **Indexing Strategies**  
    10.4. **Normalization & Denormalization**

11. **Scaling Databases**  
    11.1. **Read/Write Replication**  
    11.2. **Sharding & Partitioning**  
    11.3. **Connection Pooling**

12. **Software Architecture & Patterns**  
    12.1. **Monolith & Modular Monolith**  
    12.2. **Microservices Overview**  
    12.3. **Common Design Patterns**  
    &nbsp;&nbsp;- Factory  
    &nbsp;&nbsp;- Repository  
    &nbsp;&nbsp;- Observer  
    &nbsp;&nbsp;- Strategy  
    &nbsp;&nbsp;- etc.

13. **Development Principles**  
    13.1. **Test‑Driven Development (TDD)**  
    13.2. **Domain‑Driven Design (DDD) Basics**  
    13.3. **SOLID & Clean Code**

14. **Containerization & Deployment**  
    14.1. **Docker Basics**  
    &nbsp;&nbsp;- [Fundamentals](./notes/containers/docker/lesson-02.md)  
    &nbsp;&nbsp;- [Images](./notes/containers/docker/lesson-03.md), [containers](./notes/containers/docker/lesson-04.md), [volumes](./notes/containers/docker/lesson-06.md), [networks](./notes/containers/docker/lesson-05.md)  
    &nbsp;&nbsp;- [Podman](./notes/containers/podman/README.md)

    14.2. **Docker Compose**  
    &nbsp;&nbsp;- [Multi‑service setups](./notes/containers/docker/lesson-07.md)

    14.3. **Cloud Deployment**  
    &nbsp;&nbsp;- Heroku, AWS ECS, DigitalOcean App Platform

15. **Monitoring & Observability**  
    15.1. **Logging Best Practices**  
    15.2. **Metrics & Health Checks**  
    15.3. **Distributed Tracing & Alerts**

16. **Next Steps & Advanced Topics**  
    16.1. **Caching (Redis, CDN)**  
    16.2. **Message Brokers (RabbitMQ, Kafka)**  
    16.3. **Search Engines **  
    16.4. **Real‑Time & WebSockets**
