from crewai import Task
from tools import agent_tools

def create_tasks(support_agent, support_quality_assurance_agent, company="CrewAI"):
    
    search_tool, scrape_tool, docs_scrape_tool = agent_tools(company)

    inquiry_resolution = Task(
        description=(
            f"{{customer}} just reached out with a super important task: {{inquiry}}\n\n"
            f"{{person}} from {{customer}} is asking for help with {{inquiry}}\n"
            f"Make sure to use everything you know to provide the best possible support.\n"
            f"You must strive to provide a complete and accurate response to the customer's inquiry. "
            f"Use {company}'s documentation and resources when available."
        ),
        expected_output=(
            "A detailed, informative response to the customer's inquiry that addresses all aspects of their question.\n"
            "The response should include references to everything you used to find the answer, including external data or solutions.\n"
            "Ensure the answer is complete, leaving no questions unanswered, and maintain a helpful and friendly tone throughout the response."
        ),
        tools=[docs_scrape_tool],
        agent=support_agent
    )

    quality_assurance_review = Task(
        description=(
            f"Review the response drafted by the Senior Support Representative for {{customer}}'s inquiry and ensure that the answer is comprehensive, accurate, and adheres to high quality standards for customer support at {company}.\n"
            f"Verify that all parts of the customer's query has been addressed thoroughly with the helpful and friendly tone.\n"
            f"Check for references and sources used to find the answer, and ensure that the response is well-supported "
            f"and leaves no questions unanswered. Ensure the response aligns with {company}'s brand and values."
        ),
        expected_output=(
            "A final, detailed and informative response to the customer's inquiry that is complete, accurate, "
            "and adheres to high quality standards for customer support.\n"
            "This response should fully address the customer's inquiry, incorporating all relevant feedbacks and improvements.\n"
            f"Do not be too formal, {company} is a modern and approachable company, so keep it casual and friendly. "
            f"But maintain a professional tone and ensure that the response is complete and accurate."
        ),
        agent=support_quality_assurance_agent
    )

    return inquiry_resolution, quality_assurance_review