import os

from agent_core.core.agent_http import AgentHTTPServer as BaseAgentHTTPServer, main as http_main


def main():
    server = BaseAgentHTTPServer(agent_name=os.path.basename(os.path.dirname(__file__)),
                                 config_root=os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    http_main(server)


if __name__ == "__main__":
    main()
