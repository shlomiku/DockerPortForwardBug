#!/bin/bash
set -e
export REDIS_URL=redis://redis:6379

export CELERY_BROKER_URL=$REDIS_URL/0

exec "$@"
