# Odoo — Local Development Project

This repository provides **Odoo 17** running in Docker, plus a set of HR add-ons (including a custom module **`hr_military`**).
It is intended for quick local setup for development.

---

## Stack

- **Odoo:** `odoo:17.0`
- **PostgreSQL:** `postgres:17`
- **Docker Compose** for orchestration

---

## Repository Layout

- `compose.yaml` — Docker Compose file (Odoo + Postgres)
- `config/odoo.conf` — Odoo configuration (`addons_path`, etc.)
- `addons/custom/` — custom modules
  - `addons/custom/hr_military/` — custom HR military records module
- `addons/oca/hr/` — **OCA/hr** add-ons (included as a git submodule)


---

## Requirements

- Docker Compose v2

---

## Run the Project (Quick Start)

### 1) Start containers

```bash
docker compose up -d --remove-orphans
```

Follow logs:
```bash
docker compose logs -f web
```

### 2) Open Odoo

- URL: http://localhost:8069
- Create a new database (e.g. `dev_db`)
- The master password depends on your setup (often `admin` in dev images)

---

## Installing Modules

1. Go to **Apps**.
2. Search and install:
   - `hr_military`
   - or any OCA modules, e.g. `hr_employee_ppe`

---

## Custom Module: `hr_military`

The module extends **HR → Employees** with “Military Records” fields such as:
- Reserved status
- Mobilized status
- TCC & SP reference (directory)
- Registry / reference number (if configured)

---
