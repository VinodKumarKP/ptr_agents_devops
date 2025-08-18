from agent_core.agents.multi_agent import MultiAgent


class IntelligentDecisioningAgent(MultiAgent):
    def __init__(self, agent_name, agent_config=None, llm=None, **kwargs):
        super().__init__(agent_name,
                         llm=llm,
                         agent_config=agent_config,
                         **kwargs)
