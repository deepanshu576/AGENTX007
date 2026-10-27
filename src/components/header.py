import streamlit as st
from pathlib import Path


# Find the project root
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Your logo
LOGO_PATH = PROJECT_ROOT / "assets" / "logo.png"


def header_home():

    # Center the logo
    left, center, right = st.columns([1, 2, 1])

    with center:
        st.image(
            str(LOGO_PATH),
            width=260
        )


def header_dashboard():

    left, center, right = st.columns([1, 2, 1])

    with center:
        st.image(
            str(LOGO_PATH),
            width=180
        )