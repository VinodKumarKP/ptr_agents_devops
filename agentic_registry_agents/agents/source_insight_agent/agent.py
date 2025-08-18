from agent_core.agents.langchain_agent import LangChainAgent


class SourceInsightAgent(LangChainAgent):
    def __init__(self, agent_name, agent_config=None, llm=None, **kwargs):
        super().__init__(agent_name,
                         llm=llm,
                         agent_config=agent_config,
                         **kwargs)
