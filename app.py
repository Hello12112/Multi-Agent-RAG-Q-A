# # app.py
# import streamlit as st
# from tools import agent_router

# st.set_page_config(page_title="Multi-Agent RAG Q&A Assistant")

# st.title("📚 Multi-Agent RAG Q&A")
# query = st.text_input("Ask me anything...")

# if query:
#     with st.spinner("Thinking..."):
#         response = agent_router(query)
#         st.success("✅ Answer generated!")

#         st.markdown(f"🔁 Agent Path Chosen:** {response['route']}")

#         if 'context' in response:
#             st.markdown("**📄 Top Retrieved Chunks:**")
#             for i, chunk in enumerate(response['context']):
#                 st.markdown(f"**Chunk {i+1}:** {chunk}")

#         st.markdown(f"**💬 Final Answer:** {response['result']}")
# import streamlit as st
# from tools import agent_router

# # Set up the Streamlit page configuration
# st.set_page_config(page_title="Multi-Agent RAG Q&A Assistant")

# # Title of the app
# st.title("📚 Multi-Agent RAG Q&A")

# # Text input field for the user to ask a query
# query = st.text_input("Ask me anything...")

# # Function to handle the response and display UI elements
# if query:
#     with st.spinner("Thinking..."):
#         try:
#             # Get the response from the agent_router function
#             response = agent_router(query)
            
#             # Display success message after processing the query
#             st.success("✅ Answer generated!")
            
#             # Display the agent path (route) chosen for the query
#             st.markdown(f"🔁 Agent Path Chosen: **{response['route']}**")
            
#             # Display context if available
#             if 'context' in response:
#                 st.markdown("**📄 Top Retrieved Chunks:**")
#                 for i, chunk in enumerate(response['context']):
#                     st.markdown(f"**Chunk {i+1}:** {chunk}")
            
#             # Display the final answer
#             st.markdown(f"**💬 Final Answer:** {response['result']}")

#         except Exception as e:
#             # In case of any error, display an error message
#             st.error(f"⚠️ Error occurred: {e}")

# # Debug Mode (Optional)
# if st.checkbox('Show Debug Log', False):
#     with open('agent.log', 'r') as log_file:
#         st.text_area("Debug Log", log_file.read(), height=300)
# app.py

import streamlit as st
from tools import agent_router

# Page config
st.set_page_config(page_title="Multi-Agent RAG Q&A Assistant")

# Title
st.title("📚 Multi-Agent RAG Q&A")

# Layout with search bar and file uploader
col1, col2 = st.columns([5, 1])

with col1:
    query = st.text_input("Ask me anything...")

with col2:
    uploaded_files = st.file_uploader("📂", type=["pdf", "docx", "txt"], accept_multiple_files=True, label_visibility="collapsed")

# Show uploaded files (optional display for debug or future ingestion)
if uploaded_files:
    st.markdown("### 📥 Uploaded Documents:")
    for file in uploaded_files:
        st.markdown(f"- {file.name}")

# Process query if provided
if query:
    with st.spinner("Thinking..."):
        try:
            response = agent_router(query)

            st.success("✅ Answer generated!")
            st.markdown(f"🔁 Agent Path Chosen: **{response['route']}**")

            if 'context' in response:
                st.markdown("**📄 Top Retrieved Chunks:**")
                for i, chunk in enumerate(response['context']):
                    st.markdown(f"**Chunk {i+1}:** {chunk}")

            st.markdown(f"**💬 Final Answer:** {response['result']}")
        
        except Exception as e:
            st.error(f"⚠️ Error occurred: {e}")

# Optional: Show debug logs
if st.checkbox('Show Debug Log', False):
    with open('agent.log', 'r') as log_file:
        st.text_area("Debug Log", log_file.read(), height=300)
