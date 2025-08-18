import os

from agent_core.core.agent_executor import AgentExecutor as BaseAgentExecutor
from agentic_registry_agents.core.constants import Constants


class AgentExecutor(BaseAgentExecutor):

    def __init__(self, agent_name):
        super().__init__(agent_name=agent_name,
                         agent_registry=Constants.AGENT_REGISTRY,
                         config_root=os.path.dirname((os.path.dirname(__file__)))
                         )
