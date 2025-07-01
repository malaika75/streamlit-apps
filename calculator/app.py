import streamlit as st

# Styling
st.markdown("""
    <style>
    .stApp { text-align: center; background-color: #f7f7f7; }
    div.stButton > button {
        width: 100%; height: 50px; font-size: 18px;
        border-radius: 8px; background: #4CAF50; color: white; border: none;
        cursor: pointer;
    }
    div.stButton > button:hover { background: #45a049; }
    
    input[data-testid="stTextInput"] {
        color: black !important;
        font-weight: bold !important;
        font-size: 20px !important;
        text-align: right !important;
    }

    </style>
""", unsafe_allow_html=True)

st.title("💎 Simple Calculator")

# Session State for Display
if "calc_input" not in st.session_state:
    st.session_state.calc_input = ""

# Function to Update Display
def update_display(value):
    st.session_state.calc_input += str(value)

# Function to Evaluate Expression
def evaluate_expression():
    try:
        st.session_state.calc_input = str(eval(st.session_state.calc_input))
    except:
        st.session_state.calc_input = "Error"

# Function to Clear Display
def clear_display():
    st.session_state.calc_input = ""

# Display Box
st.text_input("Enter Calculation", st.session_state.calc_input, key="display", disabled=True)

# Buttons Grid
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("7"): update_display("7")
    if st.button("4"): update_display("4")
    if st.button("1"): update_display("1")
    if st.button("C"): clear_display()

with col2:
    if st.button("8"): update_display("8")
    if st.button("5"): update_display("5")
    if st.button("2"): update_display("2")
    if st.button("0"): update_display("0")

with col3:
    if st.button("9"): update_display("9")
    if st.button("6"): update_display("6")
    if st.button("3"): update_display("3")
    if st.button("="): evaluate_expression()

with col4:
    if st.button("+"): update_display("+")
    if st.button("-"): update_display("-")
    if st.button("*"): update_display("*")
    if st.button("/"): update_display("/")


# import streamlit as st

# # def calc(sum, sub, multi, divide):



# st.title("💎simple calculator")

# number_one = st.number_input("enter number")
# number_two = st.number_input("enter second number")

# col1 ,col2, = st.columns(2)

# with col1:
#     if st.button("➕"):
#         st.write("result:", number_one + number_two)
#     if st.button("➖"):
#         st.write("result:", number_one - number_two)
#     if st.button("//"):
#         st.write("result:", number_one // number_two)
# with col2:
#     if st.button("➗"):
#         st.write("result:", number_one / number_two)
#     if st.button("✖"):
#         st.write("result:", number_one * number_two)
#     if st.button("**"):
#         st.write("result:", number_one ** number_two)