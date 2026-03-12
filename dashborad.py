import streamlit as st

st.set_page_config(
    page_title="דשבורד קטן",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("📊 דשבורד קטן")

# Sidebar
st.sidebar.header("אפשרויות")
option = st.sidebar.selectbox(
    "בחר קטגוריה",
    ("סטטיסטיקה", "נתונים", "מידע נוסף")
)

if option == "סטטיסטיקה":
    st.subheader("סטטיסטיקות עיקריות")
    col1, col2, col3 = st.columns(3)
    col1.metric("משתמשים פעילים", "157")
    col2.metric("הכנסות (₪)", "15,700", "+5%")
    col3.metric("ביקורים החודש", "1,200")
elif option == "נתונים":
    st.subheader("נתונים לדוגמה")
    import pandas as pd
    data = {
        "שם": ["יוסי", "מיכל", "נועם"],
        "דירוג": [5, 4, 3],
        "הכנסה (₪)": [1200, 980, 660],
    }
    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)
else:
    st.subheader("מידע נוסף")
    st.info("ברוכים הבאים לדשבורד הקטן! כאן תוכל לראות מידע בסיסי וסטטיסטיקות כלליות.")
