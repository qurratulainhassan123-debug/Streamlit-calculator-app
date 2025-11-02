import streamlit as st

# Streamlit app title
st.set_page_config(page_title="Simple Calculator", page_icon="🧮", layout="centered")
st.title("🧮 Simple Calculator")

st.write("Perform basic arithmetic operations easily!")

# Input fields
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

# Operation selection
operation = st.selectbox(
    "Select operation",
    ("Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)")
)

# Calculate result
if st.button("Calculate"):
    if operation == "Addition (+)":
        result = num1 + num2
        st.success(f"✅ Result: {result}")
    elif operation == "Subtraction (-)":
        result = num1 - num2
        st.success(f"✅ Result: {result}")
    elif operation == "Multiplication (×)":
        result = num1 * num2
        st.success(f"✅ Result: {result}")
    elif operation == "Division (÷)":
        if num2 != 0:
            result = num1 / num2
            st.success(f"✅ Result: {result}")
        else:
            st.error("❌ Cannot divide by zero!")

# Footer
st.markdown("---")
st.caption("Made with ❤️ using Streamlit")
