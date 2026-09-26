import streamlit as st

from agent import ask_study_tutor


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="StudyMuse AI",
    page_icon="🎀",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* -------------------------------------------------------
       MAIN BACKGROUND
    ------------------------------------------------------- */

    .stApp {
        background:
            radial-gradient(
                circle at 10% 10%,
                rgba(255, 182, 217, 0.25),
                transparent 30%
            ),
            radial-gradient(
                circle at 90% 20%,
                rgba(221, 180, 255, 0.20),
                transparent 30%
            ),
            linear-gradient(
                135deg,
                #fff7fb 0%,
                #fff9fc 45%,
                #fdf7ff 100%
            );
    }


    /* -------------------------------------------------------
       REMOVE STREAMLIT DEFAULT TOP SPACE
    ------------------------------------------------------- */

    .block-container {
        padding-top: 2rem;
        padding-bottom: 5rem;
        max-width: 1200px;
    }


    /* -------------------------------------------------------
       SIDEBAR
    ------------------------------------------------------- */

    section[data-testid="stSidebar"] {
        background:
            linear-gradient(
                180deg,
                #fff0f7 0%,
                #fff7fb 50%,
                #f9f0ff 100%
            );

        border-right: 1px solid rgba(225, 120, 170, 0.15);
    }


    /* -------------------------------------------------------
       LOGO / BRAND
    ------------------------------------------------------- */

    .brand {
        text-align: center;
        padding: 10px 0 25px 0;
    }

    .brand-icon {
        font-size: 42px;
        margin-bottom: 5px;
    }

    .brand-name {
        font-size: 25px;
        font-weight: 800;
        background:
            linear-gradient(
                90deg,
                #e84393,
                #c56cf0
            );

        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .brand-tagline {
        color: #8d7182;
        font-size: 12px;
        margin-top: 3px;
    }


    /* -------------------------------------------------------
       HERO SECTION
    ------------------------------------------------------- */

    .hero {
        background:
            linear-gradient(
                135deg,
                rgba(255, 255, 255, 0.88),
                rgba(255, 240, 248, 0.82)
            );

        border: 1px solid rgba(235, 137, 185, 0.20);

        border-radius: 28px;

        padding: 38px 42px;

        margin-bottom: 25px;

        box-shadow:
            0 20px 60px rgba(220, 95, 155, 0.10);
    }


    .hero-badge {
        display: inline-block;

        background:
            linear-gradient(
                90deg,
                #ffe1ef,
                #f4e3ff
            );

        color: #c2387a;

        padding: 7px 14px;

        border-radius: 50px;

        font-size: 12px;

        font-weight: 700;

        margin-bottom: 14px;
    }


    .hero-title {
        font-size: 42px;
        line-height: 1.15;
        font-weight: 850;
        color: #301c2b;
        margin: 0;
    }


    .hero-title span {
        background:
            linear-gradient(
                90deg,
                #e84393,
                #c56cf0
            );

        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }


    .hero-description {
        color: #806a78;
        font-size: 16px;
        line-height: 1.7;
        max-width: 720px;
        margin-top: 15px;
    }


    /* -------------------------------------------------------
       FEATURE CARDS
    ------------------------------------------------------- */

    .feature-card {
        background: rgba(255, 255, 255, 0.75);

        border: 1px solid rgba(226, 130, 180, 0.16);

        border-radius: 20px;

        padding: 20px;

        min-height: 135px;

        box-shadow:
            0 10px 35px rgba(216, 100, 160, 0.07);

        transition: 0.25s ease;
    }


    .feature-icon {
        font-size: 25px;
        margin-bottom: 10px;
    }


    .feature-title {
        font-size: 15px;
        font-weight: 750;
        color: #392432;
    }


    .feature-text {
        color: #8a7581;
        font-size: 12px;
        line-height: 1.5;
        margin-top: 5px;
    }


    /* -------------------------------------------------------
       CHAT AREA
    ------------------------------------------------------- */

    .chat-header {
        font-size: 18px;
        font-weight: 750;
        color: #3a2532;

        margin-top: 25px;
        margin-bottom: 10px;
    }


    /* -------------------------------------------------------
       USER CHAT
    ------------------------------------------------------- */

    [data-testid="stChatMessage"]:has(
        [data-testid="chatAvatarIcon-user"]
    ) {

        background:
            linear-gradient(
                135deg,
                #ffe2f0,
                #f9e9ff
            );

        border-radius: 22px;

        border: 1px solid rgba(226, 130, 180, 0.15);

        margin-bottom: 12px;
    }


    /* -------------------------------------------------------
       ASSISTANT CHAT
    ------------------------------------------------------- */

    [data-testid="stChatMessage"]:has(
        [data-testid="chatAvatarIcon-assistant"]
    ) {

        background:
            rgba(255, 255, 255, 0.86);

        border-radius: 22px;

        border: 1px solid rgba(207, 148, 191, 0.15);

        box-shadow:
            0 8px 25px rgba(170, 100, 160, 0.05);

        margin-bottom: 12px;
    }


    /* -------------------------------------------------------
       CHAT INPUT
    ------------------------------------------------------- */

    [data-testid="stChatInput"] {

        border-radius: 20px !important;
    }


    [data-testid="stChatInput"] textarea {

        border-radius: 20px !important;

        border: 1px solid rgba(225, 120, 170, 0.25) !important;

        background: rgba(255, 255, 255, 0.92) !important;

        padding: 15px !important;

        box-shadow:
            0 10px 35px rgba(220, 100, 160, 0.08) !important;
    }


    /* -------------------------------------------------------
       BUTTONS
    ------------------------------------------------------- */

    .stButton > button {

        width: 100%;

        border-radius: 14px;

        border: 1px solid rgba(226, 130, 180, 0.20);

        background:
            linear-gradient(
                135deg,
                #ffe0ed,
                #f1e2ff
            );

        color: #9e3268;

        font-weight: 700;

        transition: 0.2s ease;
    }


    .stButton > button:hover {

        transform: translateY(-2px);

        box-shadow:
            0 8px 25px rgba(221, 105, 163, 0.15);
    }


    /* -------------------------------------------------------
       SELECT BOX
    ------------------------------------------------------- */

    div[data-baseweb="select"] > div {

        border-radius: 14px !important;

        border-color: rgba(226, 130, 180, 0.20) !important;

        background: rgba(255, 255, 255, 0.75) !important;
    }


    /* -------------------------------------------------------
       SIDEBAR DIVIDER
    ------------------------------------------------------- */

    hr {
        border-color: rgba(225, 120, 170, 0.12);
    }


    /* -------------------------------------------------------
       STATUS CARD
    ------------------------------------------------------- */

    .status-card {

        background:
            linear-gradient(
                135deg,
                #fff,
                #fff0f7
            );

        border:
            1px solid rgba(225, 120, 170, 0.15);

        border-radius: 18px;

        padding: 15px;

        margin-top: 20px;
    }


    .status-dot {

        display: inline-block;

        width: 8px;

        height: 8px;

        background: #45d483;

        border-radius: 50%;

        margin-right: 6px;
    }


    .status-text {

        font-size: 12px;

        color: #806b78;
    }


    /* -------------------------------------------------------
       FOOTER
    ------------------------------------------------------- */

    .footer {

        text-align: center;

        color: #a18b98;

        font-size: 11px;

        padding-top: 35px;
    }


    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        """
        <div class="brand">

            <div class="brand-icon">🎀</div>

            <div class="brand-name">
                StudyMuse AI
            </div>

            <div class="brand-tagline">
                Your intelligent study companion
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


    st.divider()


    st.markdown("### 🎓 Learning Level")

    difficulty = st.selectbox(
        "Choose your level",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ],
        label_visibility="collapsed"
    )


    st.divider()


    st.markdown("### ✨ What I can do")

    st.markdown(
        """
        <div style="line-height: 2; color:#806b78; font-size:13px;">
        📖 Explain difficult concepts<br>
        🧠 Answer study questions<br>
        📝 Create revision points<br>
        🧮 Solve calculations<br>
        💭 Remember study context
        </div>
        """,
        unsafe_allow_html=True
    )


    st.divider()


    st.markdown(
        """
        <div class="status-card">

            <span class="status-dot"></span>

            <span class="status-text">
                AI Tutor Online
            </span>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# HERO
# ============================================================

st.markdown(
    """
    <div class="hero">

        <div class="hero-badge">
            ✦ AI-POWERED LEARNING
        </div>

        <h1 class="hero-title">
            Study smarter with
            <span>your AI tutor.</span>
        </h1>

        <p class="hero-description">
            Ask questions, understand difficult concepts,
            practice what you've learned, and turn confusing
            topics into simple explanations.
        </p>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# FEATURE CARDS
# ============================================================

col1, col2, col3 = st.columns(3)


with col1:

    st.markdown(
        """
        <div class="feature-card">

            <div class="feature-icon">
                🧠
            </div>

            <div class="feature-title">
                Smart Explanations
            </div>

            <div class="feature-text">
                Get concepts explained according
                to your learning level.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


with col2:

    st.markdown(
        """
        <div class="feature-card">

            <div class="feature-icon">
                💡
            </div>

            <div class="feature-title">
                Learn, Don't Memorize
            </div>

            <div class="feature-text">
                Understand ideas through examples
                and simple explanations.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


with col3:

    st.markdown(
        """
        <div class="feature-card">

            <div class="feature-icon">
                🎯
            </div>

            <div class="feature-title">
                Revision Ready
            </div>

            <div class="feature-text">
                Finish every answer with concise
                revision points.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# CHAT HEADER
# ============================================================

st.markdown(
    '<div class="chat-header">💬 Chat with your Study Tutor</div>',
    unsafe_allow_html=True
)


# ============================================================
# SESSION CHAT MEMORY
# ============================================================

if "messages" not in st.session_state:

    st.session_state.messages = []


# ============================================================
# DISPLAY PREVIOUS MESSAGES
# ============================================================

for message in st.session_state.messages:

    avatar = "🎀" if message["role"] == "assistant" else "🌸"

    with st.chat_message(
        message["role"],
        avatar=avatar
    ):

        st.markdown(message["content"])


# ============================================================
# CHAT INPUT
# ============================================================

question = st.chat_input(
    "Ask anything you're studying..."
)


# ============================================================
# HANDLE QUESTION
# ============================================================

if question:

    # -----------------------------------------------
    # USER MESSAGE
    # -----------------------------------------------

    with st.chat_message(
        "user",
        avatar="🌸"
    ):

        st.markdown(question)


    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )


    # -----------------------------------------------
    # AI RESPONSE
    # -----------------------------------------------

    with st.chat_message(
        "assistant",
        avatar="🎀"
    ):

        with st.spinner("Thinking..."):

            try:

                answer = ask_study_tutor(
                    question,
                    difficulty
                )

                st.markdown(answer)


            except Exception as e:

                answer = (
                    "I couldn't process that request. "
                    "Please try again.\n\n"
                    f"Technical details: {str(e)}"
                )

                st.error(answer)


    # -----------------------------------------------
    # SAVE RESPONSE
    # -----------------------------------------------

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
        ✦ StudyMuse AI · Powered by CrewAI + Groq
    </div>
    """,
    unsafe_allow_html=True
)
