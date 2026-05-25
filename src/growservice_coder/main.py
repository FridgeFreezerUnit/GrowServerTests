from growservice_coder.crew import GrowServerCrew

def run():
    """
    Run the CrewAI agent for GrowServer development.
    """
    crew = GrowServerCrew()
    result = crew.crew().kickoff()
    print(result)
    return result

if __name__ == "__main__":
    run()