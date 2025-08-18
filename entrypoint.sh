#!/bin/bash
if [ -z "$AGENT_NAME}" ]; then
    echo "Error: $AGENT_NAME environment variable is required"
    exit 1
fi
exec python /app/agentic_registry_agents/core/agent_http.py "${AGENT_NAME}"