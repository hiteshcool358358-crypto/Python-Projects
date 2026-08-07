import streamlit as st
import math as m

def arithematic():
    st.title("Basic and Advanced Calculator")
    st.subheader("This is a calculator supporting  Arithematical, Algebraic and Trigonometric operations")    
    oper = st.selectbox("Enter your operand here:", ["Operand","Addition", "Subtraction", "Mulitplication", "Division"])
    if oper == "Addition":
        num1 = st.number_input("Enter the first number here")
        num2 = st.number_input("Enter the second number here")
        if st.button("Calculate"):
            st.success("Answer calculated")
            st.text(f"{num1} + {num2} = {num1 + num2}")
            rating = st.slider("Please give us a rating out of 10:", min_value=0, max_value=10, step=1)
            st.text(f"Rating given by the user: {rating}")  
    elif oper == "Subtraction":
        num1 = st.number_input("Enter the first number here")
        num2 = st.number_input("Enter the second number here")
        if st.button("Calculate"):
            st.success("Answer calculated")
            st.text(f"{num1} - {num2} = {num1 - num2}")
            rating = st.slider("Please give us a rating out of 10:", min_value=0, max_value=10, step=1)
            st.text(f"Rating given by the user: {rating}")
    elif oper == "Mulitplication":
        num1 = st.number_input("Enter the first number here")
        num2 = st.number_input("Enter the second number here")
        if st.button("Calculate"):
            st.success("Answer calculated")
            st.text(f"{num1} x {num2} = {num1 * num2}")
            rating = st.slider("Please give us a rating out of 10:", min_value=0, max_value=10, step=1)
            st.text(f"Rating given by the user: {rating}")
    elif oper == "Division":
        num1 = st.number_input("Enter the first number here")
        num2 = st.number_input("Enter the second number here")
        if st.button("Calculate"):
            st.success("Required solution calculated")
            st.text(f"{num1} / {num2} = {num1 / num2}")
            rating = st.slider("Please give us a rating out of 10:", min_value=0, max_value=10, step=1)
            st.text(f"Rating given by the user: {rating}")

def algebraic():
    st.title("Basic and Advanced Calculator")
    st.subheader("This is a calculator supporting  Arithematical, Algebraic and Trigononetric operations")    
    oper = st.selectbox("Enter your operand here:", ["Operand","Exponents", "Square root", "Cube root", "Factorial"])
    if oper == "Exponents":
        num1 = st.number_input("Enter the base here")
        num2 = st.number_input("Enter the power here")
        if st.button("Calculate"):
            st.success("Required solution calculated")
            st.text(f"{num1} ^ {num2} = {num1 * num2}")
            rating = st.slider("Please give us a rating out of 10:", min_value=0, max_value=10, step=1)
            st.text(f"Rating given by the user: {rating}")
    elif oper == "Square root":
        num1 = st.number_input("Enter the number here")
        if st.button("Calculate"):
            st.success("Required solution calculated")
            st.text(f"The square root of {num1} is {m.sqrt(num1)}.")
            rating = st.slider("Please give us a rating out of 10:", min_value=0, max_value=10, step=1)
            st.text(f"Rating given by the user: {rating}")
    elif oper == "Cube root":
        num1 = st.number_input("Enter the number here")
        if st.button("Calculate"):
            st.success("Required solution calculated")
            st.text(f"The cube root of {num1} is {m.cbrt(num1)}.")
            rating = st.slider("Please give us a rating out of 10:", min_value=0, max_value=10, step=1)
            st.text(f"Rating given by the user: {rating}")
    elif oper == "Factorial":
        num1 = int(st.number_input("Enter the number here"))
        if st.button("Calculate"):
            st.success("Required solution calculated")
            st.text(f"The factorial of {num1} is {m.factorial(num1)}.")
            rating = st.slider("Please give us a rating out of 10:", min_value=0, max_value=10, step=1)
            st.text(f"Rating given by the user: {rating}")

def trigonometric():
    st.title("Basic and Advanced Calculator")
    st.subheader("This is a calculator supporting  Arithematical, Algebraic and Trigononetric operations")    
    oper = st.selectbox("Enter your operand here:", ["Operand", "Sine", "Cosine", "Tangent", "Cosecant", "Secant", "Cotangent"])
    if oper == "Sine":
        num1 = st.number_input("Enter the reference angle i.e., theta here")
        if st.button("Calculate"):
            st.success("Required solution calculated")
            degree = m.radians(num1)
            st.text(f"sin({num1}°) = {m.sin(degree)}°")
            rating = st.slider("Please give us a rating out of 10:", min_value=0, max_value=10, step=1)
            st.text(f"Rating given by the user: {rating}")
    elif oper == "Cosine":
        num1 = st.number_input("Enter the reference angle i.e., theta here")
        if st.button("Calculate"):
            st.success("Required solution calculated")
            degree = m.radians(num1)
            st.text(f"cos({num1}°) = {m.cos(degree)}°")
            rating = st.slider("Please give us a rating out of 10:", min_value=0, max_value=10, step=1)
            st.text(f"Rating given by the user: {rating}")
    elif oper == "Tangent":
        num1 = st.number_input("Enter the reference angle i.e., theta here")
        if st.button("Calculate"):
            st.success("Required solution calculated")
            degree = m.radians(num1)
            st.text(f"tan({num1}°) = {m.tan(degree)}°")
            rating = st.slider("Please give us a rating out of 10:", min_value=0, max_value=10, step=1)
            st.text(f"Rating given by the user: {rating}")
    elif oper == "Cosecant":
        num1 = st.number_input("Enter the reference angle i.e., theta here")
        if st.button("Calculate"):
            st.success("Required solution calculated")
            degree = m.radians(num1)
            st.text(f"cosec({num1}°) = {1/m.sin(degree)}°")
            rating = st.slider("Please give us a rating out of 10:", min_value=0, max_value=10, step=1)
            st.text(f"Rating given by the user: {rating}")
    elif oper == "Secant":
        num1 = st.number_input("Enter the reference angle i.e., theta here")
        if st.button("Calculate"):
            st.success("Required solution calculated")
            degree = m.radians(num1)
            st.text(f"sec({num1}°) = {1/m.cos(degree)}°")
            rating = st.slider("Please give us a rating out of 10:", min_value=0, max_value=10, step=1)
            st.text(f"Rating given by the user: {rating}")
    elif oper == "Cotangent":
        num1 = st.number_input("Enter the reference angle i.e., theta here")
        if st.button("Calculate"):
            st.success("Required solution calculated")
            degree = m.radians(num1)
            st.text(f"cot({num1}°) = {1/m.tan(num1)}°")
            rating = st.slider("Please give us a rating out of 10:", min_value=0, max_value=10, step=1)
            st.text(f"Rating given by the user: {rating}")

pages = [
    st.Page(arithematic, title="Arithematical Operations", icon="➕"),
    st.Page(algebraic, title="Algebraic Operations", icon="🔍"),
    st.Page(trigonometric, title="Trigonometric Operations", icon="📐")
]

pg = st.navigation(pages)
pg.run()