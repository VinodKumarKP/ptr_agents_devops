import os

from oai_agent_core.core.agent_http import AgentHTTPServer as BaseAgentHTTPServer, main as http_main
from agentic_registry_agents.agents.servicenow_agent.agent import ServiceNowAgent


def main():
    server = BaseAgentHTTPServer(agent_name=os.path.basename(os.path.dirname(__file__)),
                                 config_root=os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
                                 agent=ServiceNowAgent())
    http_main(server)


if __name__ == "__main__":
    main()
