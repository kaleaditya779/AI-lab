import streamlit as st

def suggest_cars(budget, car_type):
    # Sample car suggestions based on budget and car type
    if budget == "Less than $20,000" and car_type == "Sedan":
        return ["Toyota Corolla", "Honda Civic", "Nissan Sentra"]
    elif budget == "Less than $20,000" and car_type == "SUV":
        return ["Honda CR-V", "Toyota RAV4", "Subaru Forester"]
    elif budget == "More than $20,000" and car_type == "Sedan":
        return ["Toyota Camry", "Honda Accord", "Nissan Altima"]
    elif budget == "More than $20,000" and car_type == "SUV":
        return ["Toyota Highlander", "Honda Pilot", "Subaru Outback"]
    else:
        return []

def main():
    st.title("Car Suggestion Chatbot")

    # Questions
    budget = st.selectbox("What is your budget?", options=["Less than $20,000", "More than $20,000"])
    car_type = st.selectbox("What type of car are you interested in?", options=["Sedan", "SUV"])

    # Button to trigger car suggestions
    if st.button("Show Car Suggestions"):
        if budget and car_type:
            car_suggestions = suggest_cars(budget, car_type)
            if car_suggestions:
                st.success("Here are some car suggestions based on your preferences:")
                for car in car_suggestions:
                    st.write(car)
            else:
                st.warning("No car suggestions found for your preferences.")

if __name__ == "__main__":
    main()
