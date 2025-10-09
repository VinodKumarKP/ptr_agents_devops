import os

from oai_agent_core.agents.bedrock_agent import BedRockAgent


class DevOpsCodeRemediationAgent(BedRockAgent):
    def __init__(self, agent_config=None, llm=None, **kwargs):
        agent_name = os.path.basename(os.path.dirname(__file__))
        kwargs.pop('agent_name')
        super().__init__(agent_name,
                         llm=llm,
                         agent_config=agent_config,
                         **kwargs)
