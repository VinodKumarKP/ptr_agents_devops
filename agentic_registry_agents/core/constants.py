import os
import sys
from pathlib import Path
from typing import Dict, Type

# Add project root to Python path
file_root = os.path.dirname(os.path.abspath(__file__))
project_root = Path(file_root).parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

file_root = os.path.dirname(os.path.abspath(__file__))
path_list = [
    file_root,
    os.path.dirname(file_root),
    os.path.dirname(os.path.dirname(file_root))
]
for path in path_list:
    if path not in sys.path:
        sys.path.append(path)

from agent_core.core.base_agent import BaseAgent
from agent_core.core.constants import Constants as CoreConstants

from agentic_registry_agents.agents.source_insight_agent.agent import SourceInsightAgent


class Constants:
    # Registry of available agent types
    AGENT_REGISTRY: Dict[str, Type[BaseAgent]] = {
        CoreConstants.MCP: SourceInsightAgent
    }
