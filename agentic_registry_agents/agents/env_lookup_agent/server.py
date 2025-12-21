import os

from oai_agent_server.main import AgentHTTPServer as BaseAgentHTTPServer, main as http_main
from agentic_registry_agents.agents.env_lookup_agent.agent import EnvLookupAgent


def main():
    server = BaseAgentHTTPServer(agent_name=os.path.basename(os.path.dirname(__file__)),
                                 config_root=os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
                                 agent=EnvLookupAgent())
    http_main(server)


if __name__ == "__main__":
    main()
