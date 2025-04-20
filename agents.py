from crewai import Agent
from textwrap import dedent
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic.v1 import BaseModel, SecretStr, Field
from tools.search_tools import SearchTools
from tools.calculator_tools import CalculatorTools
from typing import Optional
import google.generativeai as genai
from tenacity import retry, stop_after_attempt, wait_exponential

class CustomAgents(BaseModel):
    gemini: Optional[ChatGoogleGenerativeAI] = Field(default=None)
    destination: str = Field(default="")
    
    class Config:
        arbitrary_types_allowed = True

    def __init__(self, destination: str = ""):
        super().__init__(destination=destination)
        # Configure the Gemini API
        genai.configure(api_key='Enter you api key')
        
        self.gemini = ChatGoogleGenerativeAI(
            model="models/gemini-1.5-flash-8b",
            google_api_key=SecretStr('Enter you api key'),
            temperature=0.7,
            convert_system_message_to_human=True,
            client=None,  # Replace with actual client if available
            client_options=None,  # Replace with actual client options if available
            transport=None  # Replace with actual transport if available
        )

    def Expert_travel_agent(self):
        return Agent(
            role="Expert travel agent",
            backstory=dedent(f"""Expert travel agent with 10 years of experience in planning trips."""),
            goal=dedent(f"""Create a travel itinerary for {self.destination} for the given days,
                        include budget, things to pack, and places to visit"""),
            allow_delegation=False,
            tools=[SearchTools.search_internet,
                   CalculatorTools.calculate],
            verbose=True,
            llm=self.gemini,
        )

    def City_selection_expert(self):
        return Agent(
            role="City selection expert",
            backstory=dedent(f"""Expert at analyzing travel data to determine the best destination for travel """),
            goal=dedent(f"""select the best city for a trip to {self.destination} based on the weather,seasons, prices and user's interests"""),
            allow_delegation=False,
            tools=[SearchTools.search_internet],
            verbose=True,
            llm=self.gemini,
        )
    
    def Local_tour_guide(self):
        return Agent(
            role="Local tour guide",
            backstory=dedent(f"""knowledgeable local guide with extensive information about the city and its attractions"""),
            goal=dedent(f"""Provive the best insights about the {self.destination}, things to do in the city and its customs"""),
            allow_delegation=False,
            tools=[SearchTools.search_internet],
            verbose=True,
            llm=self.gemini,
        )
