import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Race Ahead Pvt Ltd", layout="wide")

# ---------- Custom CSS ----------
st.markdown("""
    <style>
        .stApp {
            background-color: #0B1A34; /* dark navy */
        }
        h1, h2, h3, h4, h5, h6, p, li {
            color: white !important;
            font-family: 'Arial Rounded MT Bold', cursive;
        }
        .centered {
            text-align: center;
        }
        /* Welcome heading */
        .welcome-heading {
            font-size: 48px;  /* bigger font like main heading */
            text-align: center;
            font-weight: bold;
        }
        /* What can you do bullets */
        .features-bullet li {
            font-size: 25px; /* bigger text to match image */
            list-style-type: disc; /* normal dot */
            margin-bottom: 10px;
        }
        /* Why choose Race Ahead bullets */
        .why-bullet li {
            font-size: 20px;
            list-style-type: disc; /* normal dot */
            margin-bottom: 10px;
        }
        .footer {
            text-align: center;
            color: white;  /* changed to white */
            font-size: 18px;
            margin-top: 40px;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# ---------- Helper ----------
def safe_image(path: str, caption: str = "", use_container_width: bool = True):
    if Path(path).exists():
        st.image(path, caption=caption, use_container_width=use_container_width)
    else:
        st.warning(f"⚠️ Missing: {path}")

# ---------- Banner ----------
safe_image("banner_main.png")  # Your main banner

# ---------- Main Heading ----------
st.markdown("<h1 class='centered'> · · ─ ·ʚɞ· ─ · ·𝓡𝓪𝓬𝓮 𝓐𝓱𝓮𝓪𝓭 : 𝓨𝓸𝓾𝓻 𝓢𝓹𝓸𝓻𝓽𝓼 𝓜𝓪𝓽𝓬𝓱 𝓢𝓬𝓱𝓮𝓭𝓾𝓵𝓮𝓻 & 𝓣𝓻𝓪𝓬𝓴𝓮𝓻· · ─ ·ʚɞ· ─ · ·</h1>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# Big welcome heading
st.markdown("<div class='welcome-heading'>ᴡᴇʟᴄᴏᴍᴇ! ʟᴇᴛ'ꜱ ɢᴇᴛ ꜱᴛᴀʀᴛᴇᴅִ ࣪𖤐.ᐟ</div>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

#heading 2 + image 3
col1, col2 = st.columns([1,1])

with col1:
    st.markdown("<h3>⊹₊⟡⋆ᴡʜᴀᴛ ᴄᴀɴ ʏᴏᴜ ᴅᴏ?!⊹₊⟡⋆</h3>", unsafe_allow_html=True)
    st.markdown("""
    <ul class='features-bullet'>
        <li>View upcoming & past matches</li>
        <li>Monitor player performance</li>
        <li>Select players for your team</li>
        <li>Match with players in the same category</li>
    </ul>
    """, unsafe_allow_html=True)

with col2:
    safe_image("image3.jpg")

st.markdown("<br>", unsafe_allow_html=True)

# ---------- Image4 + Image5 together ----------
c1, c2 = st.columns(2)
with c1:
    safe_image("image4.jpg")
with c2:
    safe_image("image5.jpg")

st.markdown("<br>", unsafe_allow_html=True)

# ---------- Why choose Race Ahead ----------
st.markdown("<h2 class='centered'>ʚɞᴡʜʏ ᴄʜᴏᴏꜱᴇ ʀᴀᴄᴇ ᴀʜᴇᴀᴅ?ʚɞ</h2>", unsafe_allow_html=True)
st.markdown("""
<ul class='why-bullet'>
    <li>Smart matchmaking based on sport & age</li>
    <li>Hassle-free scheduling for tournaments</li>
    <li>Clear performance tracking</li>
    <li>Smooth and fun user experience</li>
</ul>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ---------- Image1 + Image2 parallel with captions ----------
c3, c4 = st.columns(2)
with c3:
    safe_image("image1.jpg", caption="Let’s Play!")
with c4:
    safe_image("image2.jpg", caption="Game On!")

# ---------- Footer ----------
st.markdown("""
<div class="footer">
𝜗𝜚⋆𝐂𝐫𝐞𝐚𝐭𝐞𝐝 𝐛𝐲 <b>𝐓𝐚𝐧𝐲𝐚 𝐍𝐚𝐢𝐫</b> 𝐟𝐨𝐫 <b>𝐑𝐚𝐜𝐞 𝐀𝐡𝐞𝐚𝐝 𝐏𝐯𝐭.𝐋𝐭𝐝</b> | 𝐈𝐧𝐭𝐞𝐫𝐧𝐬𝐡𝐢𝐩 𝐏𝐫𝐨𝐣𝐞𝐜𝐭𝜗𝜚⋆
</div>
""", unsafe_allow_html=True)
