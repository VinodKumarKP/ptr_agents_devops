import os

from oai_agent_server.main import AgentHTTPServer as BaseAgentHTTPServer, main as http_main
from agentic_registry_agents.agents.source_insight_agent.agent import SourceInsightAgent


def main():
    server = BaseAgentHTTPServer(agent_name=os.path.basename(os.path.dirname(__file__)),
                                 config_root=os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
                                 agent=SourceInsightAgent())
    http_main(server)


if __name__ == "__main__":
    main()
