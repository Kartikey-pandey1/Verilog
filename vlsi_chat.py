import streamlit as st
from pathlib import Path

# Set Streamlit app config
st.set_page_config(page_title="VLSI Chat Assistant", page_icon="🤖", layout="wide")

# Session state for chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Title
st.title("🤖 VLSI Chat Assistant")
st.markdown("Ask things like: `simulate`, `show netlist`, `show layout`, `show code`")

# Input box
user_input = st.chat_input("Type your VLSI command...")

# Show chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"], unsafe_allow_html=True)

# Process user input
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    response = ""

    # === Response logic (replace later with real backend) ===
    if "simulate" in user_input.lower():
        waveform = Path("output/waveform.png")
        if waveform.exists():
            response = "📈 Simulation result:"
            st.session_state.messages.append({"role": "assistant", "content": response})
            with st.chat_message("assistant"):
                st.markdown(response)
                st.image(waveform)
        else:
            response = "❌ Simulation not found."

    elif "layout" in user_input.lower():
        layout = Path("output/layout.png")
        if layout.exists():
            response = "🧱 Layout view:"
            st.session_state.messages.append({"role": "assistant", "content": response})
            with st.chat_message("assistant"):
                st.markdown(response)
                st.image(layout)
        else:
            response = "❌ Layout image not found."

    elif "netlist" in user_input.lower():
        netlist_svg = Path("output/netlist.svg")
        if netlist_svg.exists():
            response = "🔧 Netlist diagram:"
            st.session_state.messages.append({"role": "assistant", "content": response})
            with st.chat_message("assistant"):
                st.markdown(response)
                with open(netlist_svg) as f:
                    st.components.v1.html(f.read(), height=500, scrolling=True)
        else:
            response = "❌ Netlist SVG not found."

    elif "code" in user_input.lower():
        code = Path("code/design.v")
        if code.exists():
            content = code.read_text()
            response = f"```verilog\n{content}\n```"
        else:
            response = "❌ Verilog code not found."

        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.markdown(response)

    else:
        response = "🧠 I can respond to: `simulate`, `layout`, `netlist`, `code`."
        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.markdown(response)

