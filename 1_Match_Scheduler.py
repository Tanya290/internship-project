import streamlit as st
import pandas as pd
import datetime
import random
import numpy as np

# =========================
# Page Config
# =========================
st.set_page_config(page_title="Match Scheduler", layout="wide")

# =========================
# Banner 1
# =========================
st.image("banner_3.jpg", use_container_width=True)
st.write("")
st.write(" ")

# =========================
# Load Data
# =========================
matches_df = pd.read_excel("updated_players_1000.xlsx")
stats_df = pd.read_excel("player_stats_1000.xlsx")

st.write("")
st.write(" ")

# =========================
# Ensure datetime format
# =========================
matches_df['Match Date'] = pd.to_datetime(
    matches_df['Match Date'], errors='coerce')

# =========================
# Cute Title
# =========================
st.markdown(
    "<h1 style='text-align:center; color:white;'>✧･ﾟ: *✧･ﾟ:*  MATCH SCHEDULER  *:･ﾟ✧*:･ﾟ✧</h1>",
    unsafe_allow_html=True
)
st.write("")
st.write(" ")

# =========================
# Player Selection
# =========================
all_players = pd.unique(matches_df[['Player 1', 'Player 2']].values.ravel('K'))
selected_player = st.selectbox(
    "✧･ﾟ: *✧･ﾟ:*  CHOOSE YOUR PLAYER.  *:･ﾟ✧*:･ﾟ✧",
    sorted(all_players)
)
st.write("")
st.write(" ")

# =========================
# Force 4 past and 4 future matches
# =========================
players = list(all_players)
sports = matches_df['Sport'].unique()
categories = matches_df['Category'].unique()

extra_matches = []

for _ in range(4):
    extra_matches.append([
        selected_player,
        np.random.choice([p for p in players if p != selected_player]),
        np.random.choice(sports),
        np.random.choice(categories),
        datetime.datetime.now() - datetime.timedelta(days=np.random.randint(1, 60)),
        datetime.time(np.random.randint(9, 18), 0)
    ])

for _ in range(4):
    extra_matches.append([
        selected_player,
        np.random.choice([p for p in players if p != selected_player]),
        np.random.choice(sports),
        np.random.choice(categories),
        datetime.datetime.now() + datetime.timedelta(days=np.random.randint(1, 60)),
        datetime.time(np.random.randint(9, 18), 0)
    ])

extra_df = pd.DataFrame(
    extra_matches,
    columns=['Player 1', 'Player 2', 'Sport',
             'Category', 'Match Date', 'Match Time']
)

matches_df = pd.concat([matches_df, extra_df], ignore_index=True)

# =========================
# Normalize (logic-safe)
# =========================
matches_df['Match Date'] = pd.to_datetime(
    matches_df['Match Date'], errors='coerce').dt.normalize()
matches_df['Match Time'] = pd.to_datetime(
    matches_df['Match Time'], errors='coerce').dt.strftime('%H:%M')

# Randomly assign times ONLY where Match Time is missing
time_slots = ['09:00', '10:00', '11:00',
              '12:00', '14:00', '15:00', '16:00', '17:00']

matches_df.loc[matches_df['Match Time'].isna(), 'Match Time'] = \
    np.random.choice(time_slots, size=matches_df['Match Time'].isna().sum())


# =========================
# Filter Matches
# =========================
player_matches = matches_df[
    (matches_df['Player 1'] == selected_player) |
    (matches_df['Player 2'] == selected_player)
].copy()

today = pd.Timestamp.today().normalize()
past_matches = player_matches[player_matches['Match Date'] < today]
future_matches = player_matches[player_matches['Match Date'] >= today]

# =========================
# DISPLAY COPIES (UI ONLY)
# =========================
past_display = past_matches.copy()
future_display = future_matches.copy()

past_display['Match Date'] = past_display['Match Date'].dt.strftime('%Y-%m-%d')
future_display['Match Date'] = future_display['Match Date'].dt.strftime(
    '%Y-%m-%d')

# =========================
# Past Matches
# =========================
st.markdown("### ✧･ﾟ: *✧･ﾟ:*  PAST MATCHES  *:･ﾟ✧*:･ﾟ✧")
if not past_display.empty:
    st.dataframe(
        past_display[['Player 1', 'Player 2', 'Sport',
                      'Category', 'Match Date', 'Match Time']],
        use_container_width=True
    )
else:
    st.info("No past matches found for this player.")

st.write("")
st.write(" ")

# =========================
# Future Matches
# =========================
st.markdown("### ✧･ﾟ: *✧･ﾟ:*  FUTURE MATCHES  *:･ﾟ✧*:･ﾟ✧")
if not future_display.empty:
    st.dataframe(
        future_display[['Player 1', 'Player 2', 'Sport',
                        'Category', 'Match Date', 'Match Time']],
        use_container_width=True
    )
else:
    st.info("No future matches scheduled for this player.")

st.write("")
st.write(" ")

# =========================
# Player Stats
# =========================
st.markdown("### ✧･ﾟ: *✧･ﾟ:*  PLAYER STATS  *:･ﾟ✧*:･ﾟ✧")
player_stats = stats_df[stats_df['Player Name'] == selected_player]
if not player_stats.empty:
    st.table(player_stats)
else:
    st.info("No stats found for this player.")

st.write("")
st.write(" ")

# =========================
# Fun Section
# =========================
fun_facts = [
    "🏆 Did you know? Badminton was originally called 'Poona' in India!",
    "⚽ The fastest red card in football history was just 2 seconds after kickoff.",
    "🎾 A tennis ball is made of over 2 miles of string.",
    "🏀 The highest basketball jump ever recorded was over 48 inches!",
    "🏏 Cricket balls are made with a core of cork, layered with tightly wound string."
]

st.markdown("### ✧･ﾟ: *✧･ﾟ:*  FUN FACT  *:･ﾟ✧*:･ﾟ✧")
st.success(random.choice(fun_facts))

st.write("")
st.write(" ")

# =========================
# Banner 2
# =========================
st.image("banner_4.jpg", use_container_width=True)
