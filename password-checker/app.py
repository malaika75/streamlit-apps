import re #ragex matlab regular expression
import streamlit as st
import string
import random

st.set_page_config(page_title="Password Checker", layout="centered")

st.markdown(
    """
    <style>
        /* Center align the input box */
        div.stTextInput > div {
            display: flex;
            justify-content: center;
            border : 2px solid #008080;
            padding:10px
            margin:4px
        }

        /* Heading color */
        h1 {
            text-align: center;
            color: #008080; /* Teal */
        }
    </style>
    """,
    unsafe_allow_html=True
)


# Password Checker Project
# This program will evaluate a user's password strength based on predefined conditions.
# We will categorize passwords into three types: Weak, Moderate, and Strong.
# - If the user provides a weak password, we will suggest a stronger one.
# - The function will assign a score based on password strength.
# - The goal is to guide users toward creating secure passwords.

# This function creates a strong password based on the given length.  
# It first collects letters (A-Z, a-z), numbers (0-9), and special characters (!@#$%^&*).  
# All these characters are stored in a single variable.  
# Then, the function randomly picks characters from this set using `random.choice()`.  
# Finally, it joins them together to create a unique password.  
# This ensures every generated password is different and secure.  

def suggest_password(length= 12):
   length = max(8 , length)
   characters = random.choices(string.ascii_letters + string.digits + "!@#$%^&*", k=length - 4)
   password =     [random.choice(string.ascii_lowercase),
                       random.choice(string.ascii_uppercase),
                       random.choice(string.digits),
                       random.choice("!@#$%^&*")] + characters
                     
   random.shuffle(password)
   return ''.join(password)
 

def email_checking(email):
   pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

   if re.match(pattern , email):
      st.write("✅valid email")
   else:
      st.write("❌invalid email")

#ek fuction jo hold kry ga scores ko 
#ek condition ky password 8 charcter long ho
#jo contain kary upper case or lower case letter
#include atleast one digit
#have one special character like (!@#$&*^)
     

def password_checking(password):
    score = 0

    if len(password) >= 8:
     score += 1
    else:
       st.write("password should be at least 8 characters long")

    if re.search(r"[A-Z]" , password) and re.search(r"[a-z]", password):
      score += 1
    else:
       st.write("❌ include both uppercase or lowercase letters")

    if re.search(r"\d" , password):
       score += 1
    else:
       st.write("❌include at least one digit [0.9]")

    if re.search(r"[!@#$%^&*]", password):
       score += 1
    else:
       st.write("❌include at least one special character")

    if score == 4:
       st.write("✅ strong password done!")
    elif score == 3:
       st.write("⚠ moderate password - consider adding more security")
    else: 
       st.write("❌ week password improve it using suggestions")
       st.write(f"strong suggestions: {suggest_password()}")
       
          

st.title("🔐 password_checking meter")


st.markdown(
    '<div style="text-align: center;">'
    '<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSMTm25GDpVw281drFRvtI3HCGSNa7iGU8MAg&s" width="120">'
    '</div>',
    unsafe_allow_html=True
)

user_email = st.text_input("Enter your email")
user_password = st.text_input("Enter your password" , type='password')



if user_email:
  email_checking(user_email)

if user_password:  
 password_checking(user_password)


