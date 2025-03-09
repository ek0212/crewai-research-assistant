from crewai import Agent, Task, Crew, Process
from litellm import completion
import os
from crewai_tools import SerperDevTool

class BasicCrew:
    def __init__(self):
        # Initialize the LLM
        os.environ['GEMINI_API_KEY'] = os.environ.get("GEMINI_API_KEY") or os.environ["GOOGLE_API_KEY"]
        self.llm = "gemini/gemini-1.5-flash"
        print(f"LLM Type: {self.llm}")  # Add this line
        
        # Initialize the tool for internet searching capabilities
        tool = SerperDevTool(serper_api_key=os.environ["SERPER_API_KEY"])

        # Create Researcher Agent
        self.researcher = Agent(
            role='Researcher',
            goal='Research and analyze information thoroughly',
            backstory='Expert at gathering and analyzing information',
            llm=self.llm,
            verbose=True,
            tools=[tool]
        )
        
        # Create Writer Agent
        self.writer = Agent(
            role='Writer',
            goal='Create clear and engaging content',
            backstory='Skilled writer with expertise in creating compelling narratives',
            llm=self.llm,
            verbose=True,
            tools=[tool]
        )
    
    async def run_crew(self, user_input):
        try:
            # Create tasks
            research_task = Task(
                description=f"Research the following topic thoroughly: {user_input}",
                agent=self.researcher,
                expected_output="A comprehensive report on the topic"
            )
            
            write_task = Task(
                description=f"Based on the research, create a comprehensive response about: {user_input}",
                agent=self.writer,
                expected_output="A clear and engaging response to the topic"
            )
            
            crew = Crew(
                agents=[self.researcher, self.writer],
                tasks=[research_task, write_task],
                verbose=True,
                process=Process.sequential
            )
            
            # Kickoff the crew
            crew_output = crew.kickoff()
            
            # Get and return final output
            if crew_output and crew_output.tasks_output:
                final_output = str(crew_output.tasks_output[-1].raw)
                yield {"type": "complete", "message": final_output}
            else:
                yield {"type": "error", "message": "No output generated."}
            
        except Exception as e:
            yield {"type": "error", "message": str(e)}