import streamlit as st

# Function to calculate priority score using the provided equation
def calculate_priority_score(impact_level, effort_level):
    μ = 0.7
    priority_score = μ * impact_level + (1 - μ) * effort_level
    return priority_score

# Streamlit UI components and layout
st.title("Project Priority Calculator")

# Input fields for Impact Level and Effort Level
impact_level = st.selectbox('Enter the Impact Level:', (1, 2, 3, 4), index=0)
effort_level = st.selectbox('Enter the Effort Level:', (1, 2, 3, 4), index=0)

# Calculate button
if st.button("Calculate"):
    try:
        # Calculate priority score
        priority_score = calculate_priority_score(impact_level, effort_level)
        # Display the result
        st.success(f"Final Priority Score (PS): {priority_score:.2f}")
    except Exception as e:
        # Handle errors gracefully and display a user-friendly error message
        st.error("An error occurred while calculating the priority score. Please try again.")

# Add an informational section
st.markdown(
    """
    ### Information:
    - The Priority Score (PS) is calculated using the formula: PS = μl + (1 - μ)E
    - Where μ (mu) is 0.7, l is the Impact Level, and E is the Effort Level.
    """
)
