# Microservices Starter

This is the starting point for Lab 4: Microservices Architecture.

## Architecture Overview

```
                    ┌─────────────────┐
                    │   nginx/Kong    │
                    │   API Gateway   │
                    └────────┬────────┘
                             │
    ┌────────────┬───────────┼───────────┬────────────┐
    │            │           │           │            │
    ▼            ▼           ▼           ▼            ▼
┌────────┐ ┌─────────┐ ┌───────────┐ ┌──────────┐ ┌─────────┐
│  Auth  │ │  Order  │ │Notification│ │Analytics │ │ Message │
│Node.js │ │ Python  │ │    Go     │ │  Java    │ │  Queue  │
└────┬───┘ └────┬────┘ └─────┬─────┘ └────┬─────┘ │RabbitMQ │
     │          │            │            │       └────┬────┘
     │          └────────────┴────────────┴────────────┘
     │                       │
     ▼                       ▼
┌──────────┐          ┌───────────┐
│PostgreSQL│          │  MongoDB  │
└──────────┘          └───────────┘
```

## Directory Structure

You'll create these service directories:

```
starter/
├── auth-service/         # Node.js/Express with JWT
├── order-service/        # Python/FastAPI
├── notification-service/ # Go with RabbitMQ consumer
├── analytics-service/    # Java/Spring Boot
├── nginx/                # API Gateway config
└── README.md
```

## What You'll Build

1. **Auth Service** (Node.js) - JWT authentication, user management
2. **Order Service** (Python) - Order CRUD, payment integration, event publishing
3. **Notification Service** (Go) - Email/SMS on order events, RabbitMQ consumer
4. **Analytics Service** (Java) - Real-time metrics, MongoDB aggregations

## Infrastructure

The `docker-compose.yml` in the parent directory provides:
- RabbitMQ (message queue)
- PostgreSQL (order service)
- MongoDB (inventory service)
- Redis (caching)

```bash
# Start infrastructure
docker-compose up -d

# Access RabbitMQ management
open http://localhost:15672  # admin/admin
```

## First Codex Prompt

Start with the auth service:

```bash
codex "Create a Node.js auth service with Express, JWT authentication,
user registration/login endpoints, and PostgreSQL for user storage.
Include password hashing with bcrypt and refresh token support."
```

Then build the order service:

```bash
codex "Create a Python FastAPI order service with endpoints for
creating orders, getting order status, and publishing order events
to RabbitMQ when orders are created."
```
