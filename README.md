# 🧠 CrewAI Custom Agent Framework

Welcome to my implementation of a **custom agent-based workflow** using the [CrewAI](https://crewai.com/) framework. This project is designed to streamline the creation and execution of autonomous agents that collaborate to accomplish complex tasks.

## 📁 agents.py

This file defines **custom agents** that form the core of the Crew.

To create an agent, I specify:

1. **Role** – The role or expertise of the agent.  
2. **Backstory** – A brief narrative to give the agent context and personality.  
3. **Goal** – What the agent is ultimately trying to achieve.  
4. **Tools** *(optional)* – Any tools or capabilities the agent has access to.  
5. **Allow Delegation** *(optional)* – Whether the agent is allowed to delegate tasks to others.

[More Details about Agent](https://docs.crewai.com/concepts/agents)

## 📝 task.py

This file defines the **custom tasks** that are assigned to agents.

Each task includes:

1. **Description** – What the task is about.  
2. **Agent** – The agent responsible for handling the task.  
3. **Expected Output** – What we expect the agent to return upon completion.

[More Details about Task](https://docs.crewai.com/concepts/tasks)

## 🚀 main.py (crew)

This is the main entry point of the project where I bring everything together — agents, tasks, and execution logic.

Here's how the Crew is assembled and run:

1. **Agents** – A list of the agents I've defined.  
2. **Tasks** – A list of the tasks for the agents to perform.  
3. **Verbose** *(optional)* – Enable this to print outputs of each task (default: `False`).  
4. **Debug** *(optional)* – Enable to view detailed debug logs (default: `False`).

[More Details about Crew](https://docs.crewai.com/concepts/crew)
