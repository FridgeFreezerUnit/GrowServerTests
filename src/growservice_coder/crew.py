from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from growservice_coder.tools import custom_tool  # We'll add this later if needed

@CrewBase
class GrowServerCrew:
    """GrowServer Coder Crew"""

    @agent
    def coder(self) -> Agent:
        return Agent(
            role="Senior TypeScript & Growtopia Server Developer",
            goal="Add new features, fix bugs, and improve GrowServer codebase following best practices.",
            backstory="""You are an elite full-stack TypeScript engineer specialized in Growtopia private servers.
            You deeply understand GrowServer's architecture (Turborepo, growtopia.js, Drizzle ORM, PostgreSQL).
            You always explore the code first, plan changes, write clean typed code, and consider performance & security.""",
            verbose=True,
            memory=True,
            allow_delegation=False,
        )

    @task
    def coding_task(self) -> Task:
        return Task(
            description="Implement the requested feature or fix for GrowServer. Always explore the codebase first.",
            expected_output="Clear summary of changes made, files modified, and testing instructions.",
            agent=self.coder(),
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            memory=True,
        )