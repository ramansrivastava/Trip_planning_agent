from crewai import Task


class CustomTasks:
    def identify_task(self, agent, origin, cities, interests, date_range):
        return Task(
            description=f"Analyze travel preferences to identify the best cities to visit based on origin: {origin}, cities: {cities}, interests: {interests}, and date range: {date_range}.",
            expected_output="A list of the best cities to visit with reasons.",
            agent=agent
        )

    def gather_task(self, agent, origin, interests, date_range):
        return Task(
            description=f"Gather information about local attractions and activities for origin: {origin}, interests: {interests}, and date range: {date_range}.",
            expected_output="Detailed information about attractions and activities.",
            agent=agent
        )

    def plan_task(self, agent, origin, interests, date_range):
        return Task(
            description=f"Create a travel itinerary with daily activities, transportation, accommodations, and budget for origin: {origin}, interests: {interests}, and date range: {date_range}.",
            expected_output="A complete travel itinerary.",
            agent=agent
        )
