try:
    import streamlit as st
    from typing import TYPE_CHECKING
except ImportError:
    raise ImportError("streamlit is not installed. Please run: pip install streamlit")

st.title("Chai Streamlit Example")
st.subheader("Brewed with Streamlit.")
st.text("Welcome to your first interactive app")
st.write("Choose your favorite chai:")

chai = st.selectbox("Select a chai flavor", ["Masala Chai", "Ginger Chai", "Cardamom Chai", "Tulsi Chai"])
st.write(f"You selected {chai}, Excellent choice! Enjoy your {chai}!")

st.success("Your choice has been brewed to perfection! ☕️")