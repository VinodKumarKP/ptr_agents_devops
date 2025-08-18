from agent_core.core.agent_http import AgentHTTPServer as BaseAgentHTTPServer, main, parse_args

from agentic_registry_agents.core.agent_executor import AgentExecutor


class AgentHTTPServer(BaseAgentHTTPServer):

    def __init__(self, agent_name):
        agent_executor = AgentExecutor(agent_name=agent_name)
        super().__init__(agent_name=agent_name, agent_executor=agent_executor)


if __name__ == "__main__":
    args = parse_args()
    server = AgentHTTPServer(agent_name=args.agent_name)
    main(server=server)
