# Continual Learning AI App

## Architecture Diagram (ASCII)

## Setup
1. Copy `.env.example` to `.env` and fill values.
2. Run `docker-compose up -d` to start services.
3. For backend, `cd backend; pip install -r requirements.txt` (dev) or use Docker.
4. For frontend, `cd frontend; npm install; npm run dev`.

## Environment Variables
- `DATABASE_URL=postgresql://user:pass@postgres:5432/db`
- `REDIS_URL=redis://redis:6379/0`
- `MILVUS_HOST=milvus`
- `MILVUS_PORT=19530`
- `REPLAY_BUFFER_MAX=100000`
- `TTL_DAYS=90`
- `JWT_SECRET=secret`
- Others in .env.example.

## Step-by-Step Example
1. Ingest: `curl -X POST /api/ingest -d '{"content": "text"}'`
2. Prune dry-run: `curl -X POST /api/prune -d '{"dry_run": true}'`
3. Train request: `curl -X POST /api/train-request'`
4. Approve: `curl -X POST /api/approve-train/{job_id}'`
5. View logs: `curl /api/audit`

## Security & Safety
- No auto-deploy; human approve required.
- Audit logs immutable.
- GDPR: Soft/hard delete, but unlearning limited—retrain excluding data.
- No model self-modify.
- TLS enforce in prod.
- Rollback: Load previous artifact.

## DB DDL
```sql
CREATE TYPE role_enum AS ENUM ('user', 'approver', 'admin');
CREATE TABLE users (
    id UUID PRIMARY KEY,
    email TEXT UNIQUE NOT NULL,
    role role_enum NOT NULL,
    created_at TIMESTAMP NOT NULL
);

CREATE TABLE data_items (
    id UUID PRIMARY KEY,
    owner_id UUID REFERENCES users(id),
    source TEXT,
    content TEXT,
    summary TEXT,
    created_at TIMESTAMP NOT NULL,
    last_accessed_at TIMESTAMP,
    ttl_days INT DEFAULT 90,
    soft_deleted BOOL DEFAULT FALSE,
    metadata JSONB
);

CREATE TABLE embeddings_meta (
    id UUID PRIMARY KEY REFERENCES data_items(id),
    norm FLOAT,
    created_at TIMESTAMP NOT NULL
);

CREATE TYPE status_enum AS ENUM ('pending', 'preparing', 'ready_for_approval', 'approved', 'running', 'completed', 'failed');
CREATE TABLE train_jobs (
    id UUID PRIMARY KEY,
    requestor_id UUID REFERENCES users(id),
    status status_enum NOT NULL,
    artifact_path TEXT,
    metrics JSONB,
    created_at TIMESTAMP NOT NULL,
    approved_by UUID REFERENCES users(id),
    approved_at TIMESTAMP
);

CREATE TABLE audit_logs (
    id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(id),
    action TEXT NOT NULL,
    target_type TEXT,
    target_id UUID,
    details JSONB,
    timestamp TIMESTAMP NOT NULL
);

CREATE TABLE prune_logs (
    id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(id),
    dry_run BOOL,
    details JSONB,
    timestamp TIMESTAMP NOT NULL
);