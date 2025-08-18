import asyncio

from agentic_registry_agents.agents.source_insight_agent.agent import SourceInsightAgent
# from agent_core.core.agent_executor import AgentExecutor
from agentic_registry_agents.core.agent_executor import AgentExecutor

async def main():
    try:
        # agent = SourceInsightAgent("source_insight_agent")
        agent_invoker = AgentExecutor(agent_name="source_insight_agent")
        await agent_invoker.initialize()
        user_message = 'analyze the repository https://github.com/VinodKumarKP-cpg/python_project.git'
        # Example of calling the synchronous invocation
        response = await agent_invoker.invoke(user_message)
        print(response)
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())