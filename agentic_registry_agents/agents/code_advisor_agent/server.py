import os

from oai_agent_core.core.agent_http import AgentHTTPServer as BaseAgentHTTPServer, main as http_main
from agentic_registry_agents.agents.code_advisor_agent.agent import CodeAdvisorAgent


def main():
    server = BaseAgentHTTPServer(agent_name=os.path.basename(os.path.dirname(__file__)),
                                 config_root=os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
                                 agent=CodeAdvisorAgent())
    http_main(server)


if __name__ == "__main__":
    main()
