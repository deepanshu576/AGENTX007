import streamlit as st


VIDEO_URL = "https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260613_180732_a54afbf6-b30d-470e-861f-669871f09f67.mp4"


def style_animated_background():

    st.html(f"""
    <style>

        /* Full-screen animated background */
        #agentx-background-video {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            object-fit: cover;
            z-index: -100;
            pointer-events: none;
        }}

        /* Dark overlay for readability */
        #agentx-video-overlay {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            background: rgba(20, 25, 80, 0.65);
            z-index: -99;
            pointer-events: none;
        }}

        /* Transparent Streamlit background */
        .stApp {{
            background: transparent !important;
        }}

        [data-testid="stAppViewContainer"] {{
            background: transparent !important;
        }}

        [data-testid="stHeader"] {{
            background: transparent !important;
        }}

        [data-testid="stMain"] {{
            background: transparent !important;
        }}

    </style>

    <video
        id="agentx-background-video"
        autoplay
        muted
        loop
        playsinline
        preload="auto"
    >
        <source src="{VIDEO_URL}" type="video/mp4">
    </video>

    <div id="agentx-video-overlay"></div>
    """)


def style_background_home():
    """
    Keep this function for compatibility with existing imports.
    It now uses the same animated background.
    """
    style_animated_background()


def style_background_dashboard():
    """
    Keep this function for compatibility with existing imports.
    It now uses the same animated background.
    """
    style_animated_background()


def style_base_layout():

    st.markdown("""
    <style>

        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;600;700;800&display=swap');

        /* Hide Streamlit top menu */
        #MainMenu , footer , header {
            visibility: hidden;
        }

        /* Page spacing */
        .block-container {
            padding-top: 1.5rem !important;
        }

        /* Headings */
        h1 {
            font-family: 'Orbitron', sans-serif !important;
            font-size: 3.5rem !important;
            line-height: 1.1 !important;
            margin-bottom: 0rem !important;
        }

        h2 {
            font-family: 'Orbitron', sans-serif !important;
            font-size: 2rem !important;
            line-height: 0.9 !important;
            margin-bottom: 0rem !important;
        }

        h3, h4, p {
            font-family: 'Outfit', sans-serif;
        }

        /* Buttons */
        button {
            border-radius: 1.5rem !important;
            background-color: #5865F2 !important;
            color: white !important;
            padding: 10px 20px !important;
            border: none !important;
            transition: transform 0.25s ease-in-out !important;
        }

        button[kind="secondary"] {
            border-radius: 1.5rem !important;
            background-color: #EB459E !important;
            color: white !important;
            padding: 10px 20px !important;
            border: none !important;
            transition: transform 0.25s ease-in-out !important;
        }

        button[kind="tertiary"] {
            border-radius: 1.5rem !important;
            background-color: black !important;
            color: white !important;
            padding: 10px 20px !important;
            border: none !important;
            transition: transform 0.25s ease-in-out !important;
        }

        button:hover {
            transform: scale(1.05);
        }

    </style>
    """, unsafe_allow_html=True)