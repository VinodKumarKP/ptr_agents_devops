from agent_core.agents.bedrock_agent import BedRockAgent


class DevOpsCodeRemediationAgent(BedRockAgent):
    def __init__(self, agent_name, agent_config=None, llm=None, **kwargs):
        super().__init__(agent_name,
                         llm=llm,
                         agent_config=agent_config,
                         **kwargs)
