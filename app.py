# Importing Libraries
import warnings
import streamlit as st
import os
from crewai import Crew

from agents import create_agents
from tasks import create_tasks
from tools import agent_tools
from utils import get_openai_api_key

# Warning Control
warnings.filterwarnings('ignore')

# Page Configuration
st.set_page_config(
    page_title="Multi-Agent Customer Support",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for minimal design
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 3rem;
    }

    .input-container {
        background: #f8f9fa;
        padding: 2rem;
        border-radius: 10px;
        border: 1px solid #e9ecef;
        margin-bottom: 2rem;
    }
    .result-container {
        background: #ffffff;
        padding: 2rem;
        border-radius: 10px;
        border: 1px solid #e9ecef;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .stButton > button {
        background: linear-gradient(90deg, #1f77b4, #ff7f0e);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    .agent-info {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
    }

    .footer {
        font-size: 1rem;
        color: #666;
        text-align: center;
        position: fixed;
        left: 0;
        bottom: 0;
        padding: 0.5rem 0;
        z-index: 9999;
        margin: 0;
}
</style>
""", unsafe_allow_html=True)

def setup_openai_api():
    """Setup OpenAI API key"""
    try:
        open_ai_api_key = get_openai_api_key()
        os.environ['OPENAI_API_KEY'] = open_ai_api_key
        return True
    except Exception as e:
        st.error(f"Error setting up OpenAI API: {str(e)}")
        return False

# Place the process_inquiry function here, before main()
def process_inquiry(customer, person, inquiry, company):
    """Process the customer inquiry using CrewAI agents"""
    # Progress indicator
    progress_bar = st.progress(0)
    status_text = st.empty()
    try:
        # Initialize progress
        status_text.text("🔄 Initializing agents...")
        progress_bar.progress(20)
        # Create agents with company context
        support_agent, support_quality_assurance_agent = create_agents(company)
        status_text.text("📋 Creating tasks...")
        progress_bar.progress(40)
        inquiry_resolution, quality_assurance_review = create_tasks(support_agent, support_quality_assurance_agent, company)
        status_text.text("🤖 Setting up crew...")
        progress_bar.progress(60)
        crew = Crew(
            agents=[support_agent, support_quality_assurance_agent],
            tasks=[inquiry_resolution, quality_assurance_review],
            verbose=True,
            memory=True,
        )
        status_text.text("🚀 Processing inquiry...")
        progress_bar.progress(80)
        # Prepare inputs
        inputs = {
            "customer": customer,
            "person": person,
            "inquiry": inquiry
        }
        # Execute crew
        result = crew.kickoff(inputs)
        progress_bar.progress(100)
        status_text.text("✅ Complete!")
        # Display results
        st.markdown('<div class="result-container">', unsafe_allow_html=True)
        st.markdown("### 🎯 Response")
        # Display the result in a nice format
        st.markdown(result)
        # Add some metadata
        st.markdown("---")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f"**Customer:** {customer}")
        with col2:
            st.markdown(f"**Contact:** {person}")
        with col3:
            st.markdown(f"**Company:** {company}")
        st.markdown('</div>', unsafe_allow_html=True)
    except Exception as e:
        progress_bar.progress(0)
        status_text.text("❌ Error occurred")
        st.error(f"Error processing inquiry: {str(e)}")

def main():
    # Header
    st.markdown('<h1 class="main-header">🤖 Multi-Agent Customer Support</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Intelligent AI agents working together to provide exceptional customer support</p>', unsafe_allow_html=True)
    
    # Sidebar for configuration
    with st.sidebar:
        st.markdown("### ⚙️ Configuration")
        
        # Company selection
        available_companies = ["CrewAI", "OpenAI", "Microsoft", "Google", "Amazon", "Custom"]
        company = st.selectbox(
            "Select Company",
            available_companies,
            help="Choose the company your agents will represent"
        )
        
        if company == "Custom":
            company = st.text_input("Enter custom company name:", placeholder="e.g., TechCorp Inc.")
        
        # API Key Configuration
        st.markdown("### 🔑 API Configuration")
        
        # Option to manually enter API key
        use_manual_key = st.checkbox("Manually enter API key", help="Check this if you want to enter the API key manually instead of using environment variables")
        
        if use_manual_key:
            api_key = st.text_input(
                "OpenAI API Key",
                type="password",
                placeholder="sk-...",
                help="Enter your OpenAI API key here"
            )
            
            if api_key:
                os.environ['OPENAI_API_KEY'] = api_key
                st.success("✅ API key configured")
            else:
                st.warning("⚠️ Please enter your OpenAI API key")
                return
        else:
            # Try to get API key from environment
            if setup_openai_api():
                st.success("✅ OpenAI API configured (from environment)")
            else:
                st.error("❌ OpenAI API not found in environment")
                st.info("💡 Check the 'Manually enter API key' option above to enter it manually")
                return
        
        # Agent Information
        st.markdown("### 🤖 Agents")
        st.markdown("""
        - **Support Agent**: Handles customer inquiries
        - **QA Agent**: Reviews and improves responses
        """)
        
        # Tools Information
        st.markdown("### 🛠️ Tools")
        st.markdown("""
        - Web Search
        - Website Scraping
        - Documentation Search
        """)
    
    # Main content area
    col1, col2,col3,col4,col5 = st.columns([3, 5,1,4,3])
    
    with col2:
        st.markdown("### 📝 Customer Inquiry")
        
        # Input fields
        customer = st.text_input(
            "Customer/Company Name",
            placeholder="e.g., DeepLearningAI, TechCorp Inc.",
            help="Name of the customer or company making the inquiry"
        )
        
        person = st.text_input(
            "Contact Person",
            placeholder="e.g., John Doe, Sarah Smith",
            help="Name of the person making the inquiry"
        )
        
        inquiry = st.text_area(
            "Customer Inquiry",
            placeholder="Describe your issue or question here...",
            height=150,
            help="Detailed description of the customer's inquiry or issue"
        )
        
        # Submit button
        if st.button("🚀 Process Inquiry", use_container_width=True):
            if not all([customer, person, inquiry]):
                st.warning("Please fill in all fields before processing.")
            else:
                process_inquiry(customer, person, inquiry, company)

    with col4:
        st.markdown("### 📊 Information Section")
        section = st.selectbox(
            "Select Info Section",
            ("System Status", "Quick Stats")
        )
        
        if section == "System Status":
            # Status indicators
            status_col1, status_col2 = st.columns(2)
            
            with status_col1:
                st.metric("Agents", "2 Active")
                st.metric("Tools", "3 Available")
            
            with status_col2:
                st.metric("Memory", "Enabled")
                st.metric("API", "Connected")
        
        elif section == "Quick Stats":
            st.markdown("""
            - **Response Time**: ~30-60 seconds
            - **Accuracy**: High (QA reviewed)
            - **Sources**: Web + Documentation
            """)
            
    st.markdown('<h6 class="footer">Developed by Saad Toor | saadtoorx</h6>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
