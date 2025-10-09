import os
import sys
from pathlib import Path

# Add project root to Python path
file_root = os.path.dirname(os.path.abspath(__file__))
project_root = Path(file_root).parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

file_root = os.path.dirname(os.path.abspath(__file__))
path_list = [
    file_root,
    os.path.dirname(file_root),
    os.path.dirname(os.path.dirname(file_root))
]
for path in path_list:
    if path not in sys.path:
        sys.path.append(path)


from oai_agent_core.core.agent_http import AgentHTTPServer as BaseAgentHTTPServer, main, parse_args

from agentic_registry_agents.core.agent_executor import AgentExecutor


class AgentHTTPServer(BaseAgentHTTPServer):

    def __init__(self, agent_name):
        agent_executor = AgentExecutor(agent_name=agent_name)
        super().__init__(agent_name=agent_name, agent_executor=agent_executor)


if __name__ == "__main__":
    args = parse_args()
    server = AgentHTTPServer(agent_name=args.agent_name)
    main(server=server)
