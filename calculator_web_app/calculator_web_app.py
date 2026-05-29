import streamlit as st
import math as m

st.title("Arithematical and Scientific Calculator")
st.subheader("This is a calculator supporting both arithematical and scientific operations")

operator = st.selectbox("Your operator here:", ["Select an operator", "Addition", "Subtraction", "Multiplication", "Division", "Exponents", "Square root", "Cube root", "Factorial", "Sine", "Cosine", "Tangent", "Secant", "Cosecant", "Cotangent"])
if operator == "Addition":
    num1 = st.number_input("Enter your first number: ")
    num2 = st.number_input("Enter your second number: ")
    st.success("Your calculation is being done...")
    st.write(f"The answer is {num1 + num2}.")
    ans = st.radio("Wanna give us a rating?", ["Select an option below:", "Yes", "No"])
    if ans == "Yes":
        rating = st.slider("Slide this bar to give us a rating out of 10:", min_value=0, max_value=10, step=1)
        st.write(f"Thanks for giving us a rating of {rating}")
        st.write("Thanks for using our calculator.\nWe are actively updating this app and now we are working on bringing more functions and opertions to you. Till then, stay tuned!")
    elif ans == "Select an option below:":
        st.error("Plese select an option above!")
    else:
        st.write("Thanks for using our calculator.\nWe are actively updating this app and now we are working on bringing more functions and opertions to you. Till then, stay tuned!")
elif operator == "Subtraction":
    num1 = st.number_input("Enter your first number: ")
    num2 = st.number_input("Enter your second number: ")
    st.success("Your calculation is being done...")
    st.write(f"The answer is {num1 - num2}.")
    ans = st.radio("Wanna give us a rating?", ["Select an option below:", "Yes", "No"])
    if ans == "Yes":
        rating = st.slider("Slide this bar to give us a rating out of 10:", min_value=0, max_value=10, step=1)
        st.write(f"Thanks for giving us a rating of {rating}")
        st.write("Thanks for using our calculator.\nWe are actively updating this app and now we are working on bringing more functions and opertions to you. Till then, stay tuned!")
    elif ans == "Select an option below:":
        st.error("Plese select an option above!")
    else:
        st.write("Thanks for using our calculator.\nWe are actively updating this app and now we are working on bringing more functions and opertions to you. Till then, stay tuned!")
elif operator == "Multiplication":
    num1 = st.number_input("Enter your first number: ")
    num2 = st.number_input("Enter your second number: ")
    st.success("Your calculation is being done...")
    st.write(f"The answer is {num1 * num2}.")
    ans = st.radio("Wanna give us a rating?", ["Select an option below:", "Yes", "No"])
    if ans == "Yes":
        rating = st.slider("Slide this bar to give us a rating out of 10:", min_value=0, max_value=10, step=1)
        st.write(f"Thanks for giving us a rating of {rating}")
        st.write("Thanks for using our calculator.\nWe are actively updating this app and now we are working on bringing more functions and opertions to you. Till then, stay tuned!")
    elif ans == "Select an option below:":
        st.error("Plese select an option above!")
    else:
        st.write("Thanks for using our calculator.\nWe are actively updating this app and now we are working on bringing more functions and opertions to you. Till then, stay tuned!")
elif operator == "Division":
    num1 = st.number_input("Enter your first number: ")
    num2 = st.number_input("Enter your second number: ")
    if num2 == 0:
        st.error("Division by 0 is not possible.")
    else:
        st.success("Your calculation is being done...")
        st.write(f"The answer is {num1 / num2}.")
        st.write(f"The answer in absolute integer is {num1 // num2}.")
    ans = st.radio("Wanna give us a rating?", ["Select an option below:", "Yes", "No"])
    if ans == "Yes":
        rating = st.slider("Slide this bar to give us a rating out of 10:", min_value=0, max_value=10, step=1)
        st.write(f"Thanks for giving us a rating of {rating}")
        st.write("Thanks for using our calculator.\nWe are actively updating this app and now we are working on bringing more functions and opertions to you. Till then, stay tuned!")
    elif ans == "Select an option below:":
        st.error("Plese select an option above!")
    else:
        st.write("Thanks for using our calculator.\nWe are actively updating this app and now we are working on bringing more functions and opertions to you. Till then, stay tuned!")
elif operator == "Exponents":
    num1 = st.number_input("Enter the number which should be raised: ")
    num2 = st.number_input(f"Enter the number by which {num1} should be raised by: ")
    st.success("Your calculation is being done...")
    st.write(f"The answer is {m.pow(num1, num2)}.")
    ans = st.radio("Wanna give us a rating?", ["Select an option below:", "Yes", "No"])
    if ans == "Yes":
        rating = st.slider("Slide this bar to give us a rating out of 10:", min_value=0, max_value=10, step=1)
        st.write(f"Thanks for giving us a rating of {rating}")
        st.write("Thanks for using our calculator.\nWe are actively updating this app and now we are working on bringing more functions and opertions to you. Till then, stay tuned!")
    elif ans == "Select an option below:":
        st.error("Plese select an option above!")
    else:
        st.write("Thanks for using our calculator.\nWe are actively updating this app and now we are working on bringing more functions and opertions to you. Till then, stay tuned!")
elif operator == "Square root":
    num1 = st.number_input("Enter the number: ")
    st.success("Your calculation is being done...")
    st.write(f"The answer is {m.sqrt(num1)}.")
    ans = st.radio("Wanna give us a rating?", ["Select an option below:", "Yes", "No"])
    if ans == "Yes":
        rating = st.slider("Slide this bar to give us a rating out of 10:", min_value=0, max_value=10, step=1)
        st.write(f"Thanks for giving us a rating of {rating}")
        st.write("Thanks for using our calculator.\nWe are actively updating this app and now we are working on bringing more functions and opertions to you. Till then, stay tuned!")
    elif ans == "Select an option below:":
        st.error("Plese select an option above!")
    else:
        st.write("Thanks for using our calculator.\nWe are actively updating this app and now we are working on bringing more functions and opertions to you. Till then, stay tuned!")
elif operator == "Cube root":
    num1 = st.number_input("Enter the number: ")
    st.success("Your calculation is being done...")
    st.write(f"The answer is {m.cbrt(num1)}.") 
    ans = st.radio("Wanna give us a rating?", ["Select an option below:", "Yes", "No"])
    if ans == "Yes":
        rating = st.slider("Slide this bar to give us a rating out of 10:", min_value=0, max_value=10, step=1)
        st.write(f"Thanks for giving us a rating of {rating}")
        st.write("Thanks for using our calculator.\nWe are actively updating this app and now we are working on bringing more functions and opertions to you. Till then, stay tuned!")
    elif ans == "Select an option below:":
        st.error("Plese select an option above!")
    else:
        st.write("Thanks for using our calculator.\nWe are actively updating this app and now we are working on bringing more functions and opertions to you. Till then, stay tuned!") 
elif operator == "Factorial":
    num1 = int(st.number_input("Enter the number: "))
    st.success("Your calculation is being done...")
    st.write(f"The answer is {m.factorial(num1)}.")  
    ans = st.radio("Wanna give us a rating?", ["Select an option below:", "Yes", "No"])
    if ans == "Yes":
        rating = st.slider("Slide this bar to give us a rating out of 10:", min_value=0, max_value=10, step=1)
        st.write(f"Thanks for giving us a rating of {rating}")
        st.write("Thanks for using our calculator.\nWe are actively updating this app and now we are working on bringing more functions and opertions to you. Till then, stay tuned!")
    elif ans == "Select an option below:":
        st.error("Plese select an option above!")
    else:
        st.write("Thanks for using our calculator.\nWe are actively updating this app and now we are working on bringing more functions and opertions to you. Till then, stay tuned!")   
elif operator == "Sine":
    num1 = st.number_input("Enter the angle in degrees: ")
    st.success("Your calculation is being done...")
    st.write(f"The sine of {num1}° is {m.sin(m.radians(num1))}.") 
    ans = st.radio("Wanna give us a rating?", ["Select an option below:", "Yes", "No"])
    if ans == "Yes":
        rating = st.slider("Slide this bar to give us a rating out of 10:", min_value=0, max_value=10, step=1)
        st.write(f"Thanks for giving us a rating of {rating}")
        st.write("Thanks for using our calculator.\nWe are actively updating this app and now we are working on bringing more functions and opertions to you. Till then, stay tuned!")
    elif ans == "Select an option below:":
        st.error("Plese select an option above!")
    else:
        st.write("Thanks for using our calculator.\nWe are actively updating this app and now we are working on bringing more functions and opertions to you. Till then, stay tuned!")
elif operator == "Cosine":
    num1 = st.number_input("Enter the angle in degrees: ")
    st.success("Your calculation is being done...")
    st.write(f"The cosine of {num1}° is {m.cos(m.radians(num1))}.")
    ans = st.radio("Wanna give us a rating?", ["Select an option below:", "Yes", "No"])
    if ans == "Yes":
        rating = st.slider("Slide this bar to give us a rating out of 10:", min_value=0, max_value=10, step=1)
        st.write(f"Thanks for giving us a rating of {rating}")
        st.write("Thanks for using our calculator.\nWe are actively updating this app and now we are working on bringing more functions and opertions to you. Till then, stay tuned!")
    elif ans == "Select an option below:":
        st.error("Plese select an option above!")
    else:
        st.write("Thanks for using our calculator.\nWe are actively updating this app and now we are working on bringing more functions and opertions to you. Till then, stay tuned!")
elif operator == "Tangent":
    num1 = st.number_input("Enter the angle in degrees: ")
    st.success("Your calculation is being done...")
    st.write(f"The tangent of {num1}° is {m.tan(m.radians(num1))}.")
    ans = st.radio("Wanna give us a rating?", ["Select an option below:", "Yes", "No"])
    if ans == "Yes":
        rating = st.slider("Slide this bar to give us a rating out of 10:", min_value=0, max_value=10, step=1)
        st.write(f"Thanks for giving us a rating of {rating}")
        st.write("Thanks for using our calculator.\nWe are actively updating this app and now we are working on bringing more functions and opertions to you. Till then, stay tuned!")
    elif ans == "Select an option below:":
        st.error("Plese select an option above!")
    else:
        st.write("Thanks for using our calculator.\nWe are actively updating this app and now we are working on bringing more functions and opertions to you. Till then, stay tuned!")
elif operator == "Cosecant":
    num1 = st.number_input("Enter the angle in degrees: ", min_value=1)
    st.success("Your calculation is being done...")
    st.write(f"The cosecant of {num1}° is {1 / m.sin(m.radians(num1))}.") 
    ans = st.radio("Wanna give us a rating?", ["Select an option below:", "Yes", "No"])
    if ans == "Yes":
        rating = st.slider("Slide this bar to give us a rating out of 10:", min_value=0, max_value=10, step=1)
        st.write(f"Thanks for giving us a rating of {rating}")
        st.write("Thanks for using our calculator.\nWe are actively updating this app and now we are working on bringing more functions and opertions to you. Till then, stay tuned!")
    elif ans == "Select an option below:":
        st.error("Plese select an option above!")
    else:
        st.write("Thanks for using our calculator.\nWe are actively updating this app and now we are working on bringing more functions and opertions to you. Till then, stay tuned!")
elif operator == "Secant":
    num1 = st.number_input("Enter the angle in degrees: ", min_value=1)
    st.success("Your calculation is being done...")
    st.write(f"The secant of {num1}° is {1 / m.cos(m.radians(num1))}.")
    ans = st.radio("Wanna give us a rating?", ["Select an option below:", "Yes", "No"])
    if ans == "Yes":
        rating = st.slider("Slide this bar to give us a rating out of 10:", min_value=0, max_value=10, step=1)
        st.write(f"Thanks for giving us a rating of {rating}")
        st.write("Thanks for using our calculator.\nWe are actively updating this app and now we are working on bringing more functions and opertions to you. Till then, stay tuned!")
    elif ans == "Select an option below:":
        st.error("Plese select an option above!")
    else:
        st.write("Thanks for using our calculator.\nWe are actively updating this app and now we are working on bringing more functions and opertions to you. Till then, stay tuned!")
elif operator == "Cotangent":
    num1 = st.number_input("Enter the angle in degrees: ", min_value=1)
    st.success("Your calculation is being done...")
    st.write(f"The cotangent of {num1}° is {1 / m.tan(m.radians(num1))}.")
    ans = st.radio("Wanna give us a rating?", ["Select an option below:", "Yes", "No"])
    if ans == "Yes":
        rating = st.slider("Slide this bar to give us a rating out of 10:", min_value=0, max_value=10, step=1)
        st.write(f"Thanks for giving us a rating of {rating}")
        st.write("Thanks for using our calculator.\nWe are actively updating this app and now we are working on bringing more functions and opertions to you. Till then, stay tuned!")
    elif ans == "Select an option below:":
        st.error("Plese select an option above!")
    else:
        st.write("Thanks for using our calculator.\nWe are actively updating this app and now we are working on bringing more functions and opertions to you. Till then, stay tuned!")