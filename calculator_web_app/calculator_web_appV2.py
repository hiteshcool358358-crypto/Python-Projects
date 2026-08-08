import streamlit as st
import math as m
import requests

def about():
    st.title("Basic and Advanced Calculator", text_alignment="center")
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
    st.title("Arithematic Calculator", text_alignment="center")
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
    st.title("Algebraic Calculator", text_alignment="center")
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
    st.title("Trigonometric Calculator", text_alignment="center")
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
    st.title("BMI Calculator", text_alignment="center")
    st.text("Enter your wight in kgs and height in cms below to get to know your BMI. Our app will automatically tell that whether you are underweight, overweight, normal or obese")
    weight = float(st.number_input("Enter your weight in kgs", min_value=0.00))
    height = float(st.number_input("Enter your height in cms", min_value=0.00))
    if st.button("Calculate BMI"):
        bmi = round((weight/(height / 100) ** 2), 2)
        st.success("Your BMI has been calculated!")
        st.text(f"Your BMI is {bmi}")
        if bmi<18.5:
            st.text("You are underweight.")
        elif bmi>=18.5 and bmi<25:
            st.text("You are normal weight.")
        elif bmi>=25 and bmi<30:
            st.text("You are overweight.")
        else:
            st.text("You are obese.")

    st.slider("Plese give us a rating out of 10", min_value=0, max_value=10)
    st.button("Register rating")

def curr_conv():
    st.title("Currency Converter 💱")

    with st.expander("Expand for help"):
        st.markdown("""
                    ##### Guide:
                    - You should be connected to an internet or ethernet connection
                    - If it doesn't work, try using it with a vpn
                    """)
    def_curr = st.selectbox("Enter the currency in which you want to enter the amount of conversion:", ["United States Dollar", "Indian Rupee", "Japanese Yen", "Great British Pound", "Euro", "Pakistani Rupee", "UAE Dhiram", "Singapore Dollar", "Canadian Dollar", "Australian Dollar"], key="first dropdown")

    if def_curr == "United States Dollar":
        short_curr = "USD"
        url = f"https://api.exchangerate-api.com/v4/latest/{short_curr}"
    elif def_curr == "Indian Rupee":
        short_curr = "INR"
        url = f"https://api.exchangerate-api.com/v4/latest/{short_curr}"        
    elif def_curr == "Japanese Yen":
        short_curr = "JPY"
        url = f"https://api.exchangerate-api.com/v4/latest/{short_curr}"
    elif def_curr == "Great British Pound":
        short_curr = "GBP"
        url = f"https://api.exchangerate-api.com/v4/latest/{short_curr}"
    elif def_curr == "Euro":
        short_curr = "EUR"
        url = f"https://api.exchangerate-api.com/v4/latest/{short_curr}"
    elif def_curr == "Pakistani Rupee":
        short_curr = "PKR"
        url = f"https://api.exchangerate-api.com/v4/latest/{short_curr}"
    elif def_curr == "UAE Dhiram":
        short_curr = "AED"
        url = f"https://api.exchangerate-api.com/v4/latest/{short_curr}"
    elif def_curr == "Singapore Dollar":
        short_curr = "SGD"
        url = f"https://api.exchangerate-api.com/v4/latest/{short_curr}"
    elif def_curr == "Canadian Dollar":
        short_curr = "CAD"
        url = f"https://api.exchangerate-api.com/v4/latest/{short_curr}"
    elif def_curr == "Australian Dollar":
        short_curr = "AUD"
        url = f"https://api.exchangerate-api.com/v4/latest/{short_curr}"

    def_amt = st.number_input("Enter the amount for conversion:", min_value=0.00)
    conv_curr = st.selectbox("Enter the currency in which you want to enter the amount of conversion:", ["United States Dollar", "Indian Rupee", "Japanese Yen", "Great British Pound", "Euro", "Pakistani Rupee", "UAE Dhiram", "Singapore Dollar", "Canadian Dollar", "Australian Dollar"], key="second dropdown")

    if conv_curr == "United States Dollar":
        new_curr = "USD"   
    elif conv_curr == "Indian Rupee":
        new_curr = "INR"  
    elif conv_curr == "Japanese Yen":
        new_curr = "JPY"
    elif conv_curr == "Great British Pound":
        new_curr = "GBP"
    elif conv_curr == "Euro":
        new_curr = "EUR"
    elif conv_curr == "Pakistani Rupee":
        new_curr = "PKR"
    elif conv_curr == "UAE Dhiram":
        new_curr = "AED"
    elif conv_curr == "Singapore Dollar":
        new_curr = "SGD"
    elif conv_curr == "Canadian Dollar":
        new_curr = "CAD"
    elif conv_curr == "Australian Dollar":
        new_curr = "AUD"

    if st.button("Convert"):
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            rate = data["rates"][new_curr]
            amt = def_amt * rate
            st.success("Conversion successful")
            st.write(f"{def_amt:.2f} {short_curr} = {amt:.2f} {new_curr}")
        else:
            st.error("Conversion Failed!")

    st.slider("Plese give us a rating out of 10", min_value=0, max_value=10)
    st.button("Register rating")

def len_conv():
    st.markdown("""
                # This page or app is under construction 🚧
                """)

def future_ideas():
    st.markdown("""
                ### Future and upcoming plans (as of 08-08-2026)

                - ~~Have decided to add an inbuilt bmi calculator~~
                - Scientific operations like mod will be added
                - Will be adding scientific functions like absolute and fix for Java and QBasic programmers   
                - People will be able to carry out logarithmic operations in a few months
                - People will be able to plot graphs like line graph, bar graph and pie charts by providing data here
                - ~~Inbuilt currency converter and volume converter will also be added to the web app.~~ You can visit my separate currency converter web app on **https://currency-converter1714.streamlit.app**
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
                - Currency converter - https://currency-converter1714.streamlit.app
                - Calculator V1 - https://python-projects-calculator.streamlit.app
                """)

pages = [
    st.Page(about, title="About", icon="🔢"),
    st.Page(arithematic, title="Arithematical Operations", icon="➕"),
    st.Page(algebraic, title="Algebraic Operations", icon="🔍"),
    st.Page(trigonometric, title="Trigonometric Operations", icon="📐"),
    st.Page(bmi, title="BMI Calculator", icon="⚖️"),
    st.Page(curr_conv, title="Currency Converter", icon="💱"),
    st.Page(len_conv, title="Length Converter", icon="📏"),
    st.Page(future_ideas, title="Upcoming Features", icon="🕒")
]

pg = st.navigation(pages)
pg.run()