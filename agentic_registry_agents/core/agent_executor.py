import os
import sys
from pathlib import Path

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

from oai_agent_core.core.agent_executor import AgentExecutor as BaseAgentExecutor
from agentic_registry_agents.core.constants import Constants


class AgentExecutor(BaseAgentExecutor):

    def __init__(self, agent_name):
        super().__init__(agent_name=agent_name,
                         agent_registry=Constants.AGENT_REGISTRY,
                         config_root=os.path.dirname((os.path.dirname(__file__)))
                         )
