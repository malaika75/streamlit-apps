import streamlit as st

#ek input feild for get user input 
#or do feilds from unit or to unit ky kis unit se kis unit me converte krna hy 

def unit (value, from_unit , to_unit):
    conversion_formula = {
        ("meters", "feet"): lambda x: x * 3.28084,
    ("feet", "meters"): lambda x: x * 0.3048,
    ("kg", "lbs"): lambda x: x * 2.20462,
    ("lbs", "kg"): lambda x: x * 0.453592,
    ("Celsius", "Fahrenheit"): lambda x: (x * 9/5) + 32,
    ("Fahrenheit", "Celsius"): lambda x: (x - 32) * 5/9,
    }
    if from_unit == to_unit:
        return value
    
    conversion = conversion_formula.get((from_unit,to_unit))

    if conversion:
        return conversion(value)
    else:
        return "invalid conversion"
    
st.title("🔄UNIT CONVERTER")
value = st.number_input("Enter your desire value:", min_value=0.0,format="%.2f")
from_unit = st.selectbox("from unit", ["meters","feet", "kg", "lbs","Celsius","Fahrenheit" ])
to_unit = st.selectbox("to unit", ["meters","feet", "kg", "lbs","Celsius","Fahrenheit" ])

if st.button("convert"):
    results = unit(value, from_unit, to_unit)
    st.write(f'converted value {results}')
