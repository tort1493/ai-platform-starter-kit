import streamlit as st

st.set_page_config(page_title="AI Platform Starter Kit", layout="wide")

st.title("AI Platform Starter Kit")
st.caption(
    "Reusable foundation for AI demos and early production-minded applications."
)

st.markdown(
    """
    This starter kit is built for taking an AI idea beyond a notebook. It gives you a consistent
    project shape with a demo surface, API scaffold, tests, Docker packaging, CI, and the standard
    documentation artifacts expected in a stronger portfolio or internal delivery workflow.
    """
)

col1, col2, col3 = st.columns(3)
col1.metric("App surfaces", "2", "Streamlit + FastAPI")
col2.metric("Core lanes", "4", "app / src / scripts / tests")
col3.metric("Delivery artifacts", "8", "docs included")

st.subheader("What You Can Reuse")
st.write("- `app/` for the interactive demo layer")
st.write("- `infra/api/` for service endpoints")
st.write("- `src/` for domain logic")
st.write("- `scripts/` for training, eval, or setup tasks")
st.write("- `tests/` for lightweight validation")
st.write("- `docs/` for lead-level product and operations artifacts")

st.subheader("Typical Workflow")
st.write("1. Clone the repo as a project baseline")
st.write("2. Replace the sample logic with a real use case")
st.write("3. Add evaluation, risk controls, and operating docs")
st.write("4. Deploy the Streamlit demo or API when the project is ready")

st.subheader("Good Fit")
st.write("- AI portfolio projects")
st.write("- Internal prototypes that need structure")
st.write("- Teams standardizing how AI demos are packaged")
