from crewai_tools import WebsiteSearchTool
from crewai_tools import ScrapeWebsiteTool

def agent_tools(company="CrewAI"):
    """
    Create tools for agents with company-specific configurations
    
    Args:
        company (str): The company the agents will represent
        
    Returns:
        tuple: (search_tool, scrape_tool, docs_scrape_tool)
    """
    
    # Define company-specific documentation URLs
    company_docs = {
        "CrewAI": "https://crewai.com/docs/introduction",
        "OpenAI": "https://platform.openai.com/docs",
        "Microsoft": "https://docs.microsoft.com",
        "Google": "https://developers.google.com/docs",
        "Amazon": "https://docs.aws.amazon.com"
    }
    
    # Get company-specific docs URL or use a default
    docs_url = company_docs.get(company, f"https://{company.lower().replace(' ', '')}.com/docs")
    
    # Tools for Agents
    search_tool = WebsiteSearchTool()
    scrape_tool = ScrapeWebsiteTool()

    docs_scrape_tool = ScrapeWebsiteTool(
        url=docs_url
    )

    return search_tool, scrape_tool, docs_scrape_tool
