from langchain.agents import initialize_agent, Tool
from langchain.chat_models import ChatOpenAI  # or use your preferred LLM
from backend.calender_utils import check_availability, book_appointment

llm = ChatOpenAI(temperature=0)

tools = [
    Tool(name="Check Availability", func=check_availability, description="Check calendar availability."),
    Tool(name="Book Appointment", func=book_appointment, description="Book an appointment.")
]

agent = initialize_agent(tools=tools, llm=llm, agent="zero-shot-react-description", verbose=True)

async def process_message(message: str):
    return agent.run(message)
