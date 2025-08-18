from typing import Dict, Type

from agent_core.core.base_agent import BaseAgent
from agent_core.core.constants import Constants as CoreConstants

from agentic_registry_agents.agents.source_insight_agent.agent import SourceInsightAgent


class Constants:
    # Registry of available agent types
    AGENT_REGISTRY: Dict[str, Type[BaseAgent]] = {
        CoreConstants.MCP: SourceInsightAgent
    }
