from crewai import Agent

# Function for creating agents
def create_agents(company="CrewAI"):
    
    # Define company-specific information
    company_info = {
        "CrewAI": {
            "website": "https://crewai.com",
            "docs_url": "https://crewai.com/docs/introduction",
            "description": "AI agent framework for building multi-agent systems"
        },
        "OpenAI": {
            "website": "https://openai.com",
            "docs_url": "https://platform.openai.com/docs",
            "description": "Leading AI research and deployment company"
        },
        "Microsoft": {
            "website": "https://microsoft.com",
            "docs_url": "https://docs.microsoft.com",
            "description": "Global technology company"
        },
        "Google": {
            "website": "https://google.com",
            "docs_url": "https://developers.google.com/docs",
            "description": "Technology and internet services company"
        },
        "Amazon": {
            "website": "https://amazon.com",
            "docs_url": "https://docs.aws.amazon.com",
            "description": "E-commerce and cloud computing company"
        }
    }
    
    # Get company info or use defaults for custom companies
    company_data = company_info.get(company, {
        "website": f"https://{company.lower().replace(' ', '')}.com",
        "docs_url": f"https://{company.lower().replace(' ', '')}.com/docs",
        "description": f"Technology company: {company}"
    })
    
    support_agent = Agent(
        role=f"Senior Support Agent Representative",
        goal=f"Be the most friendly and helpful support agent in your team",
        backstory=(
            f"You work at {company} ({company_data['website']}) and you are a senior support agent. "
            f"You are known for your friendly and helpful nature. You are working on providing support to {{customer}}, "
            f"a super important customer for your company. "
            f"You need to make sure that you provide the best possible support to {{customer}}. "
            f"Make sure to provide full complete answers, and make no assumptions. "
            f"Use {company_data['docs_url']} and other resources to provide accurate information."
        ),
        allow_delegation=False,
        verbose=True,
    )

    support_quality_assurance_agent = Agent(
        role=f"Support Quality Assurance Specialist at {company}",
        goal=f"Get recognition for providing the best support quality assurance at {company}",
        backstory=(
            f"You work at {company} ({company_data['website']}) and are now working with your team "
            f"on a request from {{customer}} ensuring that the support representative is providing the best support possible.\n"
            f"You need to make sure that the support representative is following the best practices and guidelines "
            f"for providing support. It is providing complete answers without any assumptions. "
            f"Ensure responses align with {company}'s standards and values."
        ),
        verbose=True,
    )

    return support_agent, support_quality_assurance_agent