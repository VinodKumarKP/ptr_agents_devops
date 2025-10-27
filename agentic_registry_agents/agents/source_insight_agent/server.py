import os

file_dir = os.path.dirname(os.path.abspath(__file__))
# Ensure the project root is in sys.path
project_root = os.path.dirname(os.path.dirname(os.path.dirname(file_dir)))
import sys
if project_root not in sys.path:
    sys.path.insert(0, project_root)

print(sys.path)

from oai_agent_core.core.agent_http import AgentHTTPServer as BaseAgentHTTPServer, main as http_main
from agentic_registry_agents.agents.source_insight_agent.agent import SourceInsightAgent


def main():
    server = BaseAgentHTTPServer(agent_name=os.path.basename(os.path.dirname(__file__)),
                                 config_root=os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
                                 agent=SourceInsightAgent())
    http_main(server)


if __name__ == "__main__":
    main()
