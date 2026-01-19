# Microservices Starter

This is the starting point for Lab 4: Microservices Architecture.

## Architecture Overview

```
                    ┌─────────────────┐
                    │   API Gateway   │
                    │   (Node.js)     │
                    └────────┬────────┘
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
        ▼                    ▼                    ▼
┌───────────────┐   ┌───────────────┐   ┌───────────────┐
│ Order Service │   │   Inventory   │   │ Notification  │
│   (Python)    │   │   (Go/Java)   │   │   (Node.js)   │
└───────┬───────┘   └───────┬───────┘   └───────────────┘
        │                   │                    ▲
        │                   │                    │
        └───────────┬───────┘                    │
                    ▼                            │
            ┌───────────────┐                    │
            │   RabbitMQ    │────────────────────┘
            └───────────────┘
```

## Directory Structure

Each service gets its own directory:

```
starter/
├── api-gateway/       # Node.js Express gateway
├── order-service/     # Python FastAPI service
├── inventory-service/ # Go or Java service
├── notification-service/ # Node.js event consumer
└── README.md
```

## What You'll Build

1. **API Gateway** - Route requests, authentication, rate limiting
2. **Order Service** - Create/manage orders, publish events
3. **Inventory Service** - Stock management, consume order events
4. **Notification Service** - Send emails/SMS on order events

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

```bash
codex "Create a Python FastAPI order service with endpoints for 
creating orders, getting order status, and publishing order events 
to RabbitMQ when orders are created."
```
