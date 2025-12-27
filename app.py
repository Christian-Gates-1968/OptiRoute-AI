"""
OptiRoute AI - Streamlit Dashboard
Interactive frontend for the intelligent GenAI routing system.
"""

import streamlit as st
from router import ModelRouter
import time
import os
import json
from datetime import datetime
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="OptiRoute AI",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better UI
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #1f77b4;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.2rem;
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# History persistence functions
HISTORY_FILE = Path("data/history.json")
STATS_FILE = Path("data/stats.json")

def ensure_data_dir():
    """Ensure data directory exists."""
    HISTORY_FILE.parent.mkdir(exist_ok=True)

def load_history():
    """Load history from JSON file."""
    ensure_data_dir()
    if HISTORY_FILE.exists():
        try:
            with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            return []
    return []

def save_history(history):
    """Save history to JSON file."""
    ensure_data_dir()
    try:
        with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
            json.dump(history, f, indent=2, ensure_ascii=False)
    except Exception as e:
        st.error(f"Failed to save history: {str(e)}")

def load_stats():
    """Load stats from JSON file."""
    ensure_data_dir()
    if STATS_FILE.exists():
        try:
            with open(STATS_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            return {"total_requests": 0, "fast_model_count": 0, "smart_model_count": 0}
    return {"total_requests": 0, "fast_model_count": 0, "smart_model_count": 0}

def save_stats(total, fast, smart):
    """Save stats to JSON file."""
    ensure_data_dir()
    try:
        with open(STATS_FILE, 'w', encoding='utf-8') as f:
            json.dump({
                "total_requests": total,
                "fast_model_count": fast,
                "smart_model_count": smart
            }, f, indent=2)
    except Exception as e:
        st.error(f"Failed to save stats: {str(e)}")

# Initialize session state
if "history" not in st.session_state:
    st.session_state.history = load_history()
    
if "total_requests" not in st.session_state:
    stats = load_stats()
    st.session_state.total_requests = stats["total_requests"]
if "fast_model_count" not in st.session_state:
    stats = load_stats()
    st.session_state.fast_model_count = stats["fast_model_count"]
if "smart_model_count" not in st.session_state:
    stats = load_stats()
    st.session_state.smart_model_count = stats["smart_model_count"]

if "show_result" not in st.session_state:
    st.session_state.show_result = None

# Initialize router
@st.cache_resource
def get_router():
    """Initialize and cache the ModelRouter instance."""
    try:
        return ModelRouter()
    except ValueError as e:
        st.error(f"⚠️ Configuration Error: {str(e)}")
        st.info("Please ensure your .env file contains OPENAI_API_KEY and GROQ_API_KEY")
        st.stop()

router = get_router()

# Header
st.markdown('<div class="main-header">🚀 OptiRoute AI</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Intelligent GenAI Router - Optimizing Cost & Performance</div>', unsafe_allow_html=True)

# Sidebar - Project Info and Stats
with st.sidebar:
    st.header("📊 Dashboard Stats")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Requests", st.session_state.total_requests)
        st.metric("⚡ Fast Model", st.session_state.fast_model_count)
    with col2:
        estimated_savings = st.session_state.fast_model_count * 0.02  # Assume $0.02 saved per fast route
        st.metric("Cost Savings", f"${estimated_savings:.2f}")
        st.metric("🧠 Smart Model", st.session_state.smart_model_count)
    
    st.divider()
    
    st.header("ℹ️ About OptiRoute")
    st.markdown("""
    **OptiRoute AI** is an intelligent middleware that:
    
    - 🎯 **Analyzes** prompt complexity
    - ⚡ **Routes** simple queries to fast models (Llama 3.1 via Groq)
    - 🧠 **Escalates** complex queries to Llama 3.3 70B via Groq
    - 💰 **Saves** costs through smart routing
    
    **Tech Stack:**
    - Frontend: Streamlit
    - Backend: LangChain
    - Models: Llama 3 (Groq)
    - Deployment: Docker
    """)
    
    # Show deployment environment
    is_docker = os.path.exists('/.dockerenv')
    if is_docker:
        st.success("🐳 Running in Docker Container")
    else:
        st.info("💻 Running Locally")
    
    st.divider()
    
    st.header("🔧 Routing Logic")
    st.markdown("""
    **Simple Queries** (Fast Model):
    - Word count ≤ 15
    - No reasoning keywords
    
    **Complex Queries** (Smart Model):
    - Word count > 15
    - Contains: explain, analyze, compare, why, etc.
    """)

# Main content area
st.header("💬 Ask a Question")

# Input area
prompt = st.text_area(
    "Enter your prompt:",
    placeholder="Type your question here... (e.g., 'What is Python?' or 'Explain the differences between REST and GraphQL APIs')",
    height=100,
    key="prompt_input"
)

col1, col2, col3 = st.columns([1, 1, 2])

with col1:
    submit_button = st.button("🚀 Submit", type="primary", use_container_width=True)
with col2:
    clear_button = st.button("🗑️ Clear History", use_container_width=True)

if clear_button:
    st.session_state.history = []
    st.session_state.total_requests = 0
    st.session_state.fast_model_count = 0
    st.session_state.smart_model_count = 0
    # Clear persisted data
    save_history([])
    save_stats(0, 0, 0)
    st.rerun()

# Process the prompt
if submit_button and prompt:
    with st.spinner("🔄 Analyzing and routing your query..."):
        start_time = time.time()
        
        # Get response from router
        result = router.get_response(prompt)
        
        end_time = time.time()
        response_time = end_time - start_time
        
        # Update session state
        st.session_state.total_requests += 1
        if result["analysis"]["provider"] == "groq":
            st.session_state.fast_model_count += 1
        else:
            st.session_state.smart_model_count += 1
        
        # Add to history
        st.session_state.history.insert(0, {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "prompt": prompt,
            "result": result,
            "response_time": response_time
        })
        
        # Persist to file
        save_history(st.session_state.history)
        save_stats(
            st.session_state.total_requests,
            st.session_state.fast_model_count,
            st.session_state.smart_model_count
        )
        
        # Store result to show after rerun
        st.session_state.show_result = {
            "result": result,
            "response_time": response_time,
            "prompt": prompt
        }
        
        # Rerun to update dashboard
        st.rerun()

# Display the most recent result if available
if st.session_state.show_result:
    result = st.session_state.show_result["result"]
    response_time = st.session_state.show_result["response_time"]
    
    if result["success"]:
        st.success("✅ Response Generated Successfully")
        
        # Routing decision
        st.subheader("🎯 Routing Decision")
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Model Used", result["model"])
        with col2:
            st.metric("Complexity", result["analysis"]["complexity"].upper())
        with col3:
            st.metric("Word Count", result["analysis"]["word_count"])
        with col4:
            st.metric("Response Time", f"{response_time:.2f}s")
        
        st.info(f"**Routing Reason:** {result['analysis']['reason']}")
        
        # Response
        st.subheader("💡 Response")
        st.markdown(f"**{result['response']}**")
        
        # Clear the show_result flag
        st.session_state.show_result = None
        
    else:
        st.error(f"❌ Error: {result['error']}")
        st.session_state.show_result = None

elif submit_button and not prompt:
    st.warning("⚠️ Please enter a prompt before submitting.")

# Display history
if st.session_state.history:
    st.divider()
    st.header("📜 Request History")
    
    for idx, entry in enumerate(st.session_state.history[:5]):  # Show last 5
        with st.expander(f"{entry['timestamp']} - {entry['prompt'][:50]}..."):
            st.markdown(f"**Prompt:** {entry['prompt']}")
            st.markdown(f"**Model:** {entry['result']['model']}")
            st.markdown(f"**Complexity:** {entry['result']['analysis']['complexity'].upper()}")
            st.markdown(f"**Response Time:** {entry['response_time']:.2f}s")
            if entry['result']['success']:
                st.markdown(f"**Response:** {entry['result']['response']}")
            else:
                st.error(f"Error: {entry['result']['error']}")

# Footer
st.divider()
st.markdown("""
<div style='text-align: center; color: #666; padding: 1rem;'>
    Built by a Founding Engineer | Demonstrating Cost Optimization & Scalability
</div>
""", unsafe_allow_html=True)
