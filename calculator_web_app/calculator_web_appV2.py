# url for vising the website - "https://web-calculator1714.streamlit.app"

import streamlit as st
import math as m
import requests

def about():
    st.title("Basic and Advanced Calculator", text_alignment="center")
    with st.expander("Expand for help"):
        st.markdown("""
                    #### Guide:
                    - You can select the kind of operation you want to carry out or the feature you want to use from the sidebar
                    - Operations and features provided as of 09-08-2026 are:
                        1. Arithematical operations
                        2. Algebraic operations
                        3. Trigonometric operations
                        4. BMI Calculator
                        5. Currency Converter
                        6. Length Converter
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
            try:
                st.success("Required solution calculated")
                degree = m.radians(num1)
                st.text(f"cosec({num1}°) = {1/m.sin(degree)}°")
            except ZeroDivisionError:
                st.text("Undefined")
            
            
    elif oper == "Secant":
        num1 = st.number_input("Enter the reference angle i.e., theta here")
        if st.button("Calculate"):
            st.success("Required solution calculated")
            degree = m.radians(num1)
            st.text(f"sec({num1}°) = {1/m.cos(degree)}°")
            
    elif oper == "Cotangent":
        num1 = st.number_input("Enter the reference angle i.e., theta here")
        if st.button("Calculate"):
            try:
                st.success("Required solution calculated")
                degree = m.radians(num1)
                st.text(f"cot({num1}°) = {1/m.tan(degree)}°")
            except ZeroDivisionError:
                st.text("Undefined")

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
    st.title("Currency Converter", text_alignment="center")

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
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                rate = data["rates"][new_curr]
                amt = def_amt * rate
                st.success("Conversion successful")
                st.write(f"{def_amt:.2f} {short_curr} = {amt:.2f} {new_curr}")
            else:
                st.error("Conversion Failed!")
        except requests.exceptions.ConnectionError:
            st.error("Please connect to an internet connection")

    st.slider("Plese give us a rating out of 10", min_value=0, max_value=10)
    st.button("Register rating")

lengths = {
    "Miles": {
        "Miles": 1,
        "Kilometers": 1.609344,
        "Angstroms": 16093440000000,
        "Nanometers": 1609344000000,
        "Microns": 1609344000,
        "Millimeters": 1609344,
        "Centimeters": 160934.4,
        "Meters": 1609.344,
        "Inches": 63360,
        "Feet": 5280,
        "Yards": 1760,
        "Nautical miles": 0.868976
    },
    "Angstroms": {
        "Miles": 0.000000000000062,
        "Kilometers": 0.0000000000001,
        "Angstroms": 1,
        "Nanometers": 0.1,
        "Microns": 0.0001,
        "Millimeters": 0.0000001,
        "Centimeters": 0.00000001,
        "Meters": 0.0000000001,
        "Inches": 0.000000003937008,
        "Feet": 0.000000000328084,
        "Yards": 0.000000000109361,
        "Nautical miles": 0.000000000000054
    },
    "Nanometers": {
        "Miles": 0.000000000000621,
        "Kilometers": 0.000000000001,
        "Angstroms": 10,
        "Nanometers": 1,
        "Microns": 0.001,
        "Millimeters": 0.000001,
        "Centimeters": 0.0000001,
        "Meters": 0.0000001,
        "Inches": 0.000000039370079,
        "Feet": 0.00000000328084,
        "Yards": 0.000000001093613,
        "Nautical miles": 0.00000000000054
    },
    "Microns": {
        "Miles": 0.000000000621371,
        "Kilometers": 0.000000001,
        "Angstroms": 10000,
        "Nanometers": 1000,
        "Microns": 1,
        "Millimeters": 0.001,
        "Centimeters": 0.0001,
        "Meters": 0.0000001,
        "Inches": 0.000039,
        "Feet": 0.000003,
        "Yards": 0.000001,
        "Nautical miles": 0.000000000539957
    },
    "Millimeters": {
        "Miles": 0.000000621371192,
        "Kilometers": 0.000001,
        "Angstroms": 10000000,
        "Nanometers": 1000000,
        "Microns": 1000,
        "Millimeters": 1,
        "Centimeters": 0.1,
        "Meters": 0.001,
        "Inches": 0.03937,
        "Feet": 0.003281,
        "Yards": 0.001094,
        "Nautical miles": 0.000000539956803
    },
    "Centimeters": {
        "Miles": 0.000006,
        "Kilometers": 0.00001,
        "Angstroms": 100000000,
        "Nanometers": 10000000,
        "Microns": 10000,
        "Millimeters": 10,
        "Centimeters": 1,
        "Meters": 0.01,
        "Inches": 0.393701,
        "Feet": 0.032808,
        "Yards": 0.010936,
        "Nautical miles": 0.000005
    },
    "Meters": {
        "Miles": 0.000621,
        "Kilometers": 0.001,
        "Angstroms": 10000000000,
        "Nanometers": 1000000000,
        "Microns": 1000000,
        "Millimeters": 1000,
        "Centimeters": 100,
        "Meters": 1,
        "Inches": 39.37008,
        "Feet": 3.28084,
        "Yards": 1.093613,
        "Nautical miles": 0.00054
    },
    "Kilometers": {
        "Miles": 0.621371,
        "Kilometers": 1,
        "Angstroms": 10000000000000,
        "Nanometers": 1000000000000,
        "Microns": 1000000000,
        "Millimeters": 1000000,
        "Centimeters": 100000,
        "Meters": 1000,
        "Inches": 39370.08,
        "Feet": 3280.84,
        "Yards": 1093.613,
        "Nautical miles": 0.539957 
    },
    "Inches": {
        "Miles": 0.000016,
        "Kilometers": 0.00025,
        "Angstroms": 254000000,
        "Nanometers": 25400000,
        "Microns": 25400,
        "Millimeters": 25.4,
        "Centimeters": 2.54,
        "Meters": 0.0254,
        "Inches": 1,
        "Feet": 0.083333,
        "Yards": 0.027778,
        "Nautical miles": 0.000014 
    },
    "Feet": {
        "Miles": 0.000189,
        "Kilometers": 0.000305,
        "Angstroms": 3048000000,
        "Nanometers": 304800000,
        "Microns": 304800,
        "Millimeters": 304.8,
        "Centimeters": 30.48,
        "Meters": 0.3048,
        "Inches": 12,
        "Feet": 1,
        "Yards": 0.333333,
        "Nautical miles": 0.000165 
    },
    "Yards": {
        "Miles": 0.000568,
        "Kilometers": 0.000914,
        "Angstroms": 9144000000,
        "Nanometers": 914400000,
        "Microns": 914400,
        "Millimeters": 914.4,
        "Centimeters": 91.44,
        "Meters": 0.9144,
        "Inches": 36,
        "Feet": 3,
        "Yards": 1,
        "Nautical miles": 0.000494 
    },
    "Nautical miles": {
        "Miles": 1.150779,
        "Kilometers": 1.852,
        "Angstroms": 18520000000000,
        "Nanometers": 1852000000000,
        "Microns": 1852000000,
        "Millimeters": 1852000,
        "Centimeters": 185200,
        "Meters": 1852,
        "Inches": 72913.39,
        "Feet": 6076.115,
        "Yards": 2025.372,
        "Nautical miles": 1 
    }
}


def len_conv():
    st.title("Length Converter", text_alignment="center")
    st.text("Select the conversion units from the following dropdowns and enter the length is text fields accordingly to get the correct result or answers")
    def_unit = st.selectbox("Convert from:", ["Miles", "Kilometers", "Angstroms", "Nanometers", "Microns", "Millimeters", "Centimeters", "Meters", "Inches", "Feet", "Yards", "Nautical miles"], key="dropdown1")
    def_value = st.number_input(f"Enter value in {def_unit} here")
    conv_unit = st.selectbox("Convert to:", ["Miles", "Kilometers", "Angstroms", "Nanometers", "Microns", "Millimeters", "Centimeters", "Meters", "Inches", "Feet", "Yards", "Nautical miles"], key="dropdown2")
    if st.button("Convert"):
        st.success("Solution calculated")
        if def_unit == "Miles":
            new_val = float(def_value * lengths["Miles"][conv_unit])
            st.text(f"{def_value} {def_unit} = {new_val} {conv_unit}")
        elif def_unit == "Angstroms":
            new_val = float(def_value * lengths["Angstroms"][conv_unit])
            st.text(f"{def_value} {def_unit} = {new_val} {conv_unit}")
        elif def_unit == "Nanometers":
            new_val = float(def_value * lengths["Nanometers"][conv_unit])
            st.text(f"{def_value} {def_unit} = {new_val} {conv_unit}")
        elif def_unit == "Microns":
            new_val = float(def_value * lengths["Microns"][conv_unit])
            st.text(f"{def_value} {def_unit} = {new_val} {conv_unit}")
        elif def_unit == "Millimeters":
            new_val = float(def_value * lengths["Millimeters"][conv_unit])
            st.text(f"{def_value} {def_unit} = {new_val} {conv_unit}")
        elif def_unit == "Centimeters":
            new_val = float(def_value * lengths["Centimeters"][conv_unit])
            st.text(f"{def_value} {def_unit} = {new_val} {conv_unit}")
        elif def_unit == "Meters":
            new_val = float(def_value * lengths["Meters"][conv_unit])
            st.text(f"{def_value} {def_unit} = {new_val} {conv_unit}")
        elif def_unit == "Kilometers":
            new_val = float(def_value * lengths["Kilometers"][conv_unit])
            st.text(f"{def_value} {def_unit} = {new_val} {conv_unit}")
        elif def_unit == "Inches":
            new_val = float(def_value * lengths["Inches"][conv_unit])
            st.text(f"{def_value} {def_unit} = {new_val} {conv_unit}")
        elif def_unit == "Feet":
            new_val = float(def_value * lengths["Feet"][conv_unit])
            st.text(f"{def_value} {def_unit} = {new_val} {conv_unit}")
        elif def_unit == "Yards":
            new_val = float(def_value * lengths["Yards"][conv_unit])
            st.text(f"{def_value} {def_unit} = {new_val} {conv_unit}")
        elif def_unit == "Nautical miles":
            new_val = float(def_value * lengths["Nautical miles"][conv_unit])
            st.text(f"{def_value} {def_unit} = {new_val} {conv_unit}")
    
    st.slider("Plese give us a rating out of 10", min_value=0, max_value=10)
    st.button("Register rating")

def inter():
    st.title("Interest Calcuator", text_alignment="center")
    InterType = st.selectbox("Select the type of Interest you are calculating", ["Type of interest", "Simple Interest", "Compound Interest"])
    if (InterType == "Simple Interest"):
        p = st.number_input("Enter principal here (in ₹)", min_value=0.00)
        r = st.number_input("Enter rate here (in p.a.)", min_value=0.00)
        t = st.number_input("Enter time here (in years)", min_value=0.00)
        if st.button(f"Calculate {InterType}"):
            st.success(f"{InterType} calculated")
            st.text(f"Simple Interest = ₹ {p*r*t}")
            st.text(f"Amount = ₹ {p+(p*r*t)}")
    elif (InterType == "Compound Interest"):
        p = st.number_input("Enter principal here (in ₹)", min_value=0.00)
        r = st.number_input("Enter rate here (in p.a.)", min_value=0.00)
        t = st.number_input("Enter time here (in years)", min_value=0.00)
        ci_type = st.selectbox("Compound interest have been compounded:", ["Select below", "Yearly", "Half-Yearly"])
        if st.button(f"Calculate {InterType}"):
            if (ci_type == "Yearly"):
                st.success(f"{InterType} calculated")
                st.text(f"Compound Interest = ₹ {(p*((1+(r/100))**t))-p}")
                st.text(f"Amount = ₹ {p*((1+(r/100))**t)}")
            elif (ci_type == "Half-Yearly"):
                st.success(f"{InterType} calculated")
                st.text(f"Compound Interest = ₹ {(p*((1+(r/200))**(t*2)))-p}")
                st.text(f"Amount = ₹ {p*((1+(r/200))**(t*2))}")
            else:
                st.error("Please select the type of compound interest reckoned")
            
            
def gst():
    st.title("GST Calculator", text_alignment="center")
    st.text("This GST calculator is aligned to the gst rates presribed by the Indian Government as of 22.08.2026. Any further chnages announced by the govrnment will be tried to reflect here within 10 - 15 days", text_alignment="center")
    amt = st.number_input("Enter the amount here in ₹ (exclusive of any GST or Tax)", min_value=0.00)
    tran_type = st.selectbox("Enter the type of transaction", ["Select a type of transaction", "Intra - State", "Inter - State"], key="dropdown1")
    gst = st.selectbox(f"Enter the GST% applied to the product", ["Select the rate of GST", "0%", "5%", "18%", "40%"], key="dropdown2")
    if st.button("Calculate amount"):
        if tran_type != "Select a type of transaction" and gst != "Select the rate of GST":
            if tran_type == "Intra - State":
                if gst == "0%":
                    st.text(f"CGST: ₹0.00")
                    st.text(f"SGST: ₹0.00")
                    st.text(f"Total amound to be paid (inclusive of all taxes and GST): ₹{amt:.2f}")
                elif gst == "5%":
                    st.text(f"CGST: ₹{(0.025*amt):.2f}")
                    st.text(f"SGST: ₹{(0.025*amt):.2f}")
                    st.text(f"Total amound to be paid (inclusive of all taxes and GST): ₹{amt+((0.025*amt)*2):.2f}")
                elif gst == "18%":
                    st.text(f"CGST: ₹{0.09*amt:.2f}")
                    st.text(f"SGST: ₹{0.09*amt:.2f}")
                    st.text(f"Total amound to be paid (inclusive of all taxes and GST): ₹{amt+((0.09*amt)*2):.2f}")
                elif gst == "40%":
                    st.text(f"CGST: ₹{0.2*amt:.2f}")
                    st.text(f"SGST: ₹{0.2*amt:.2f}")
                    st.text(f"Total amound to be paid (inclusive of all taxes and GST): ₹{amt+((0.2*amt)*2):.2f}")
            elif tran_type == "Inter - State":
                if gst == "0%":
                    st.text(f"IGST: ₹0.00")
                    st.text(f"Total amound to be paid (inclusive of all taxes and GST): ₹{amt:.2f}")
                elif gst == "5%":
                    st.text(f"IGST: ₹{0.05*amt:.2f}")
                    st.text(f"Total amound to be paid (inclusive of all taxes and GST): ₹{amt+((0.05*amt)):.2f}")
                elif gst == "18%":
                    st.text(f"IGST: ₹{0.18*amt:.2f}")
                    st.text(f"Total amound to be paid (inclusive of all taxes and GST): ₹{amt+((0.18*amt)):.2f}")
                elif gst == "40%":
                    st.text(f"IGST: ₹{0.4*amt:.2f}")
                    st.text(f"Total amound to be paid (inclusive of all taxes and GST): ₹{amt+((0.4*amt)):.2f}")
        elif tran_type == "Select a type of transaction" and gst == "Select the rate of GST":
            st.error("GST or type of transaction fields have been left blank")
        elif tran_type == "Select a type of transaction" or gst == "Select the rate of GST":
            st.error("GST or type of transaction fields have been left blank")


def weight_mass():
    st.title("Work on this converter has been started. It will be live within the next 1 - 1.5 months", text_alignment="center")

def future_ideas():
    st.markdown("""
                ### Future and upcoming plans (as of 08-08-2026)

                - ~~Have decided to add an inbuilt bmi calculator~~
                - Scientific operations like mod will be added
                - Will be adding scientific functions like absolute and fix for Java and QBasic programmers   
                - People will be able to carry out logarithmic operations in a few months
                - People will be able to plot graphs like line graph, bar graph and pie charts by providing data here
                - ~~Inbuilt currency converter~~ and volume converter will also be added to the web app. You can visit my separate currency converter web app on **https://currency-converter1714.streamlit.app**
                - Other converters that will be added to the app are:
                    1. ~~Length~~
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
    st.Page(bmi, title="BMI Calculator", icon="👟"),
    st.Page(curr_conv, title="Currency Converter", icon="💱"),
    st.Page(len_conv, title="Length Converter", icon="📏"),
    st.Page(inter, title="Interest Calculator", icon="🏦"),
    st.Page(gst, title="GST Calculator", icon="💸"),
    st.Page(weight_mass, title="Weight and Mass Converter", icon=":material/balance:"),
    st.Page(future_ideas, title="Upcoming Features", icon="🕒")
]

pg = st.navigation(pages)
pg.run()