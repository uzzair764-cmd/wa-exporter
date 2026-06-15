import streamlit as st

st.set_page_config(
    page_title="Data Tools",
    page_icon="whatsapp.png",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        display: none;
    }

    [data-testid="collapsedControl"] {
        display: none;
    }

    .block-container {
        padding-top: 4rem;
        max-width: 1100px;
    }

    .main-title {
        text-align: center;
        font-size: 3rem;
        font-weight: 800;
        margin-bottom: 0.4rem;
    }

    .subtitle {
        text-align: center;
        color: #777;
        font-size: 1.1rem;
        margin-bottom: 3rem;
    }

    .tool-card {
        height: 300px;
        border-radius: 28px;
        border: 1px solid #e8e8e8;
        background: #ffffff;
        box-shadow: 0 10px 30px rgba(0,0,0,0.06);
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        font-size: 2rem;
        font-weight: 800;
        color: #111;
        text-decoration: none;
        transition: all 0.18s ease-in-out;
    }

    .tool-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 16px 42px rgba(0,0,0,0.11);
        border-color: #d0d0d0;
        color: #111;
        text-decoration: none;
    }

    .tool-card.disabled {
        color: #aaa;
        background: #f8f8f8;
        cursor: not-allowed;
    }

    .tool-card.disabled:hover {
        transform: none;
        box-shadow: 0 10px 30px rgba(0,0,0,0.06);
        border-color: #e8e8e8;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="main-title">Data Tools</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Choose a tool to start processing.</div>',
    unsafe_allow_html=True
)

left, right = st.columns(2, gap="large")

with left:
    st.page_link(
        "pages/1_WA_Exporter.py",
        label="WA EXPORTER",
        icon="📤",
        use_container_width=True
    )

with right:
    st.page_link(
        "pages/2_Call_Center_Cleaner.py",
        label="CALL CENTER CLEANER",
        icon="📞",
        use_container_width=True
    )

st.markdown(
    """
    <style>
    div[data-testid="stPageLink"] > a {
        height: 300px;
        border-radius: 28px;
        border: 1px solid #e8e8e8;
        background: #ffffff;
        box-shadow: 0 10px 30px rgba(0,0,0,0.06);
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        font-size: 2rem;
        font-weight: 800;
        color: #111;
        text-decoration: none;
        transition: all 0.18s ease-in-out;
    }

    div[data-testid="stPageLink"] > a:hover {
        transform: translateY(-4px);
        box-shadow: 0 16px 42px rgba(0,0,0,0.11);
        border-color: #d0d0d0;
        color: #111;
        text-decoration: none;
    }

    div[data-testid="stPageLink"] p {
        font-size: 2rem;
        font-weight: 800;
    }
    </style>
    """,
    unsafe_allow_html=True
)
