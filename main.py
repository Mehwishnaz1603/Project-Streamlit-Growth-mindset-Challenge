import streamlit as st
import random
from datetime import datetime

# --- PAGE CONFIG ---
st.set_page_config(page_title="Growth Mindset", page_icon="🌱", layout="centered")

# --- BACKGROUND COLOR ---
st.markdown(
    """
    <style>
        body {
            background-color: #f0f8ff;
        }
        .stApp {
            background-color: #f0f8ff;
        }
    </style>
    """,
    unsafe_allow_html=True
)


# --- MOTIVATIONAL QUOTES ---
quotes = [
    "“Success is not final, failure is not fatal: it is the courage to continue that counts.” – Winston Churchill",
    "“The only limit to our realization of tomorrow is our doubts of today.” – Franklin D. Roosevelt",
    "“Your mindset is everything. Keep it positive, keep it strong.”",
    "“Strive for progress, not perfection.”",
    "“Difficulties strengthen the mind, as labor does the body.” – Seneca",
    "“Believe you can and you're halfway there.” – Theodore Roosevelt",
    "“Small steps in the right direction can turn out to be the biggest step of your life.”"
]

random_quote = random.choice(quotes)

# --- SESSION STATE INIT ---
if "saved_goal" not in st.session_state:
    st.session_state.saved_goal = ""
if "motivation_count" not in st.session_state:
    st.session_state.motivation_count = 0
if "journal_entries" not in st.session_state:
    st.session_state.journal_entries = []

# --- TITLE ---
st.title("🌱 Growth Mindset")

# --- QUOTE SECTION ---
st.subheader("💡 Inspirational Quote")
st.write(f"*{random_quote}*")

# --- GOAL TRACKER ---
st.subheader("📌 Growth Goal Tracker")
goal = st.text_input("Set a personal growth goal:")
if st.button("Save Goal"):
    st.session_state.saved_goal = goal
    st.success(f"Goal saved: {goal}")

if st.session_state.saved_goal:
    st.info(f"🎯 Current Goal: {st.session_state.saved_goal}")
    st.checkbox("✅ I made progress on my goal today!")

# --- MOOD TRACKER ---
st.subheader("🧠 Mood Tracker")
mood = st.radio("How are you feeling today?", ["😊 Happy", "😐 Neutral", "😔 Low"])
st.write(f"You selected: {mood}")

# --- DAILY JOURNAL ---
st.subheader("📓 Daily Reflection Journal")
today_journal = st.text_area("Write a quick reflection for today:")
if st.button("Save Reflection"):
    entry = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "text": today_journal
    }
    st.session_state.journal_entries.append(entry)
    st.success("Reflection saved!")

# --- MOTIVATION COUNTER ---
st.subheader("🚀 Motivation Boost")
if st.button("I'm feeling motivated! 💥"):
    st.session_state.motivation_count += 1
st.metric(label="Motivation Count", value=st.session_state.motivation_count)

# --- JOURNAL HISTORY ---
if st.session_state.journal_entries:
    st.subheader("📚 Past Reflections")
    for entry in reversed(st.session_state.journal_entries):
        st.markdown(f"**{entry['date']}**")
        st.write(entry['text'])
        st.markdown("---")

# --- FOOTER ---
st.write("---")
st.write("💡 Stay consistent and keep growing every day! 🌟")

# --- FOOTER ---
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: gray; font-size: 0.9em;'>
        🌱 Built with ❤️ using Streamlit<br>
        Made by <b>Mehwish Naz</b> | © 2025 Growth Mindset App
    </div>
    """,
    unsafe_allow_html=True
)

