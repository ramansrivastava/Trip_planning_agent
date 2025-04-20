import os
from crewai import Crew
from textwrap import dedent
from agents import CustomAgents
from tasks import CustomTasks

# Install duckduckgo-search for this example:
# !pip install -U duckduckgo-search




# This is the main class that you will use to define your custom crew.
# You can define as many agents and tasks as you want in agents.py and tasks.py


class TripCrew:

  def __init__(self, origin, cities, date_range, interests, destination):
    self.cities = cities
    self.origin = origin
    self.interests = interests
    self.date_range = date_range
    self.destination = destination

  def run(self):
    agents = CustomAgents(destination=self.destination)
    tasks = CustomTasks()

    city_selector_agent = agents.City_selection_expert()
    local_expert_agent = agents.Local_tour_guide()
    travel_concierge_agent = agents.Expert_travel_agent()

    identify_task = tasks.identify_task(
      city_selector_agent,
      self.origin,
      self.cities,
      self.interests,
      self.date_range
    )
    gather_task = tasks.gather_task(
      local_expert_agent,
      self.origin,
      self.interests,
      self.date_range
    )
    plan_task = tasks.plan_task(
      travel_concierge_agent, 
      self.origin,
      self.interests,
      self.date_range
    )

    crew = Crew(
      agents=[city_selector_agent, local_expert_agent, travel_concierge_agent],
      tasks=[identify_task, gather_task, plan_task],
      verbose=True
    )

    result = crew.kickoff()
    return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
  print("## Welcome to Trip Planner Crew")
  print('-------------------------------')
  location = input(
    dedent("""
      From where will you be traveling from?
    """))
  destination = input(
    dedent("""
      Where would you like to travel to?
    """))
  cities = input(
    dedent("""
      What are the specific cities you are interested in visiting in {}?
    """.format(destination)))
  date_range = input(
    dedent("""
      What is the date range you are interested in traveling?
    """))
  interests = input(
    dedent("""
      What are some of your high level interests and hobbies?
    """))
  
  trip_crew = TripCrew(location, cities, date_range, interests, destination)
  result = trip_crew.run()
  print("\n\n########################")
  print("## Here is you Trip Plan")
  print("########################\n")
  print(result)