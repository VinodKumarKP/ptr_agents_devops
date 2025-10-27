import os
import sys

# Add project root to path
file_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(os.path.dirname(file_dir)))
sys.path.insert(0, project_root)

# Also add the agent_core path
agent_core_path = '/Users/vinodkumarkp/PycharmProjects/agent_core'
if agent_core_path not in sys.path:
    sys.path.insert(0, agent_core_path)

from oai_agent_core.core.agent_http import AgentHTTPServer as BaseAgentHTTPServer, main as http_main
from .agent import SourceInsightAgent


def main():
    server = BaseAgentHTTPServer(agent_name=os.path.basename(os.path.dirname(__file__)),
                                 config_root=os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
                                 agent=SourceInsightAgent())
    http_main(server)


if __name__ == "__main__":
    main()
