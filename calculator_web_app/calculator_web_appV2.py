import streamlit as st
import math as m

def about():
    st.title("Basic and Advanced Calculator")
    with st.expander("Expand for help"):
        st.markdown("""
                    #### Guide:
                    - You can select the kind of operation you want to carry out from the sidebar
                    - Operations supported as of 08-08-2026 are:
                        1. Arithematical operations
                        2. Algebraic operations
                        3. Trigonometric operations
                    - You can check the source code by clicking on the github icon appearing on the ribbon right at the top right corner
                    """)
    st.markdown("A quality product created by **Hitesh Kumar**.")

def arithematic():
    st.title("Arithematic Calculator")
    st.text("You can carry out the supported arithematical operation here by selecting th operand from the dropdown appearing below")    
    oper = st.selectbox("Enter your operand here:", ["Operand","Addition", "Subtraction", "Mulitplication", "Division"])
    if oper == "Addition":
        num1 = st.number_input("Enter the first number here")
        num2 = st.number_input("Enter the second number here")
        if st.button("Calculate"):
            st.success("Answer calculated")
            st.text(f"{num1} + {num2} = {num1 + num2}")

    elif oper == "Subtraction":
        num1 = st.number_input("Enter the first number here")
        num2 = st.number_input("Enter the second number here")
        if st.button("Calculate"):
            st.success("Answer calculated")
            st.text(f"{num1} - {num2} = {num1 - num2}")
            
    elif oper == "Mulitplication":
        num1 = st.number_input("Enter the first number here")
        num2 = st.number_input("Enter the second number here")
        if st.button("Calculate"):
            st.success("Answer calculated")
            st.text(f"{num1} x {num2} = {num1 * num2}")
            
    elif oper == "Division":
        num1 = st.number_input("Enter the first number here")
        num2 = st.number_input("Enter the second number here")
        if st.button("Calculate"):
            st.success("Required solution calculated")
            st.text(f"{num1} / {num2} = {num1 / num2}")

    st.slider("Plese give us a rating out of 10", min_value=0, max_value=10)
    st.button("Register rating")
            

def algebraic():
    st.title("Algebraic Calculator")
    st.text("You can carry out the supported algebraic operation here by selecting th operand from the dropdown appearing below")    
    oper = st.selectbox("Enter your operand here:", ["Operand","Exponents", "Square root", "Cube root", "Factorial"])
    if oper == "Exponents":
        num1 = st.number_input("Enter the base here")
        num2 = st.number_input("Enter the power here")
        if st.button("Calculate"):
            st.success("Required solution calculated")
            st.text(f"{num1} ^ {num2} = {num1 * num2}")
            
    elif oper == "Square root":
        num1 = st.number_input("Enter the number here")
        if st.button("Calculate"):
            st.success("Required solution calculated")
            st.text(f"The square root of {num1} is {m.sqrt(num1)}.")
            
    elif oper == "Cube root":
        num1 = st.number_input("Enter the number here")
        if st.button("Calculate"):
            st.success("Required solution calculated")
            st.text(f"The cube root of {num1} is {m.cbrt(num1)}.")
            
    elif oper == "Factorial":
        num1 = int(st.number_input("Enter the number here", min_value=0))
        if st.button("Calculate"):
            st.success("Required solution calculated")
            st.text(f"The factorial of {num1} is {m.factorial(num1)}.")

    st.slider("Plese give us a rating out of 10", min_value=0, max_value=10)
    st.button("Register rating")

def trigonometric():
    st.title("Trigonometric Calculator")
    st.text("You can carry out all the trigonometric functions here by selecting an operand appearing in the dopdown menu below")    
    oper = st.selectbox("Enter your operand here:", ["Operand", "Sine", "Cosine", "Tangent", "Cosecant", "Secant", "Cotangent"])
    if oper == "Sine":
        num1 = st.number_input("Enter the reference angle i.e., theta here")
        if st.button("Calculate"):
            st.success("Required solution calculated")
            degree = m.radians(num1)
            st.text(f"sin({num1}°) = {m.sin(degree)}°")
            
    elif oper == "Cosine":
        num1 = st.number_input("Enter the reference angle i.e., theta here")
        if st.button("Calculate"):
            st.success("Required solution calculated")
            degree = m.radians(num1)
            st.text(f"cos({num1}°) = {m.cos(degree)}°")
            
    elif oper == "Tangent":
        num1 = st.number_input("Enter the reference angle i.e., theta here")
        if st.button("Calculate"):
            st.success("Required solution calculated")
            degree = m.radians(num1)
            st.text(f"tan({num1}°) = {m.tan(degree)}°")
            
    elif oper == "Cosecant":
        num1 = st.number_input("Enter the reference angle i.e., theta here")
        if st.button("Calculate"):
            st.success("Required solution calculated")
            degree = m.radians(num1)
            st.text(f"cosec({num1}°) = {1/m.sin(degree)}°")
            
    elif oper == "Secant":
        num1 = st.number_input("Enter the reference angle i.e., theta here")
        if st.button("Calculate"):
            st.success("Required solution calculated")
            degree = m.radians(num1)
            st.text(f"sec({num1}°) = {1/m.cos(degree)}°")
            
    elif oper == "Cotangent":
        num1 = st.number_input("Enter the reference angle i.e., theta here")
        if st.button("Calculate"):
            st.success("Required solution calculated")
            degree = m.radians(num1)
            st.text(f"cot({num1}°) = {1/m.tan(num1)}°")

    st.slider("Plese give us a rating out of 10", min_value=0, max_value=10)
    st.button("Register rating")

def bmi():
    st.markdown("""
                # Page under construction right now 🚧
                """)

def future_ideas():
    st.markdown("""
                ### Future and upcoming plans

                - Have decided to add an inbuilt bmi calculator
                - Scientific opeartions like mod will be added
                - Will be adding scientific functions like absolute and fix for Java and QBasic programmers   
                - People will be able to carry out logarithmic operations in a few months
                - People will be able to plot graphs like line graph, bar graph and pie charts by providing data here
                - Inbuilt currency converter and volume converter will also be added to the web app. You can visit my separate currency converter web app on **https://currency-converter1714.streamlit.app**
                - Other converters that will be added to the app are:
                    1. Length
                    2. Weight and Mass
                    3. Temperature
                    4. Energy 
                    5. Area
                    6. Speed
                    7. Time Power
                    8. Power
                    9. Data
                    10. Pressure
                    11. Angle


                These features will be coming out and be released shortly. The work has been started at the backend. Meanwhile you can try out other web apps created by me like:
                - https://currency-converter1714.streamlit.app
                - https://______________________.streamlit.app
                """)

pages = [
    st.Page(about, title="About", icon="🔢"),
    st.Page(arithematic, title="Arithematical Operations", icon="➕"),
    st.Page(algebraic, title="Algebraic Operations", icon="🔍"),
    st.Page(trigonometric, title="Trigonometric Operations", icon="📐"),
    st.Page(bmi, title="BMI Calculator", icon="⚖️"),
    st.Page(future_ideas, title="Upcomg Features", icon="🕒")
]

pg = st.navigation(pages)
pg.run()