# Import necessary tools/libraries
import streamlit as st  # Imports Streamlit for making web apps
import random  # Imports random number generator
import time  # Imports time-related functions
import requests  # Imports tool for making web requests

# Set the title of our web app with an emoji
st.title("💰 Money Making Machine 💰")

# Add a cool header with emojis
st.markdown("### 🚀 Welcome to the Ultimate Money-Making Experience! 🚀")

# Add a divider for visual separation
st.markdown("---")

# Function to create random amount of money
def generate_money():
    return random.randint(1, 1000)  # Gives random number between 1 and 1000

# Create a section for generating money with emojis and columns
st.subheader("💸 Instant Cash Generator 💸")
col1, col2 = st.columns([3, 1])  # Create two columns for layout
with col1:
    if st.button("🎰 Generate Money 🎰", help="Click to generate random money!"):  # When user clicks the button
        with st.spinner("Counting your money... 💵"):  # Show a spinner while loading
            time.sleep(5)  # Wait for 5 seconds
            amount = generate_money()  # Get random amount
            st.success(f"🎉 You made ${amount}! 🎉")  # Show success message with amount

# Add a divider for visual separation
st.markdown("---")

# Function to get side hustle ideas from a server
def fetch_side_hustle():
    try:
        # Try to get data from local server or deployed server
        response = requests.get(
            "https://fast-api-two-plum.vercel.app/side_hustles"
        )
        if response.status_code == 200:  # If request successful
            hustles = response.json()  # Convert response to JSON
            return hustles["side_hustle"]  # Return the hustle idea
        else:
            return "Freelancing"  # Default response if server fails
    except:
        return "Something went wrong!"  # Error message if request fails

# Create a section for side hustle ideas with emojis and columns
st.subheader("💡 Side Hustle Ideas 💡")
col1, col2 = st.columns([3, 1])  # Create two columns for layout
with col1:
    if st.button("💼 Generate Hustle 💼", help="Click to get a side hustle idea!"):  # When user clicks button
        idea = fetch_side_hustle()  # Get a hustle idea
        st.success(f"🚀 Try this: {idea} 🚀")  # Show the idea

# Add a divider for visual separation
st.markdown("---")

# Function to get money-related quotes from server
def fetch_money_quote():
    try:
        # Try to get quote from local server or deployed server
        response = requests.get(
            "https://fast-api-two-plum.vercel.app/money_quotes"
        )
        if response.status_code == 200:  # If request successful
            quotes = response.json()  # Convert response to JSON
            return quotes["money_quote"]  # Return the quote
        else:
            return "Money is the root of all evil!"  # Default quote if server fails
    except:
        return "Something went wrong!"  # Error message if request fails

# Create a section for motivation quotes with emojis and columns
st.subheader("🔥 Money-Making Motivation 🔥")
col1, col2 = st.columns([3, 1])  # Create two columns for layout
with col1:
    if st.button("✨ Get Inspired ✨", help="Click to get a motivational quote!"):  # When user clicks button
        quote = fetch_money_quote()  # Get a quote
        st.info(f"💬 {quote} 💬")  # Show the quote

# Add a footer with a fun message
st.markdown("---")
st.markdown("### 🌟 Keep hustling, and you'll be a millionaire in no time! 🌟")