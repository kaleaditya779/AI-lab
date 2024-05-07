import streamlit as st

bot_name = "MedicalBot"

knowledge_base = {
    "What is your name?": [
        f"My name is {bot_name}! I'm here to help you with your medical queries."
    ],

    "Hello": [
        f"Hello! I'm {bot_name}. How can I assist you today?"
    ],

    "What are the symptoms of the common cold?": [
        "The symptoms of the common cold include coughing, sneezing, sore throat, runny or stuffy nose, and sometimes fever."
    ],

    "What are the symptoms of influenza?": [
        "Influenza symptoms include fever, chills, muscle aches, cough, congestion, runny nose, headaches, and fatigue."
    ],

    "What are the symptoms of asthma?": [
        "Asthma symptoms include shortness of breath, wheezing, chest tightness, and coughing."
    ],

    "What are the symptoms of pneumonia?": [
        "Pneumonia symptoms include cough, fever, chills, shortness of breath, chest pain, fatigue, and sometimes vomiting or diarrhea."
    ],

    "What are the symptoms of a heart attack?": [
        "Heart attack symptoms include chest pain or discomfort, upper body pain or discomfort in the arms, back, neck, jaw, or upper stomach, shortness of breath, cold sweats, nausea, and lightheadedness."
    ],

    "What are the symptoms of a stroke?": [
        "Stroke symptoms include sudden numbness or weakness in the face, arm, or leg, especially on one side of the body, sudden confusion, trouble speaking or understanding speech, sudden trouble seeing in one or both eyes, sudden trouble walking, dizziness, loss of balance or coordination, and sudden severe headache with no known cause."
    ],

    "What are the symptoms of diabetes?": [
        "Diabetes symptoms include increased thirst, frequent urination, extreme hunger, unexplained weight loss, fatigue, blurred vision, slow-healing sores, and frequent infections."
    ],

    "What are the symptoms of allergies?": [
        "Allergy symptoms include sneezing, runny or stuffy nose, itchy or watery eyes, itching of the throat, mouth, nose, or skin, coughing, and wheezing."
    ],

    "What are the symptoms of food poisoning?": [
        "Food poisoning symptoms include nausea, vomiting, diarrhea, abdominal pain or cramps, fever, and headache."
    ],

    "What are the symptoms of a urinary tract infection (UTI)?": [
        "UTI symptoms include a strong, persistent urge to urinate, burning sensation when urinating, passing frequent, small amounts of urine, cloudy or strong-smelling urine, and pelvic pain in women."
    ],

    "What are the symptoms of depression?": [
        "Depression symptoms include feeling sad, empty, or hopeless, loss of interest or pleasure in activities once enjoyed, changes in appetite or weight, sleep disturbances, fatigue, feelings of worthlessness or guilt, difficulty concentrating, and thoughts of death or suicide."
    ],

    "What is the difference between a virus and bacteria?": [
        "Viruses are smaller than bacteria and can only replicate inside the living cells of other organisms. Bacteria are single-celled microorganisms that can live independently and reproduce on their own."
    ],

    "What are the benefits of a healthy diet?": [
        "A healthy diet provides essential nutrients that support overall health and well-being, including vitamins, minerals, protein, healthy fats, and carbohydrates. It can help prevent chronic diseases, maintain a healthy weight, support immune function, and promote energy and vitality."
    ]
}

st.header("Disease symptoms chatbot")

def respond(input_text):
    if input_text in knowledge_base:
        values = knowledge_base[input_text]
        for value in values:
            st.write(value)
        st.write("")
        st.button("Clear Input", on_click=lambda: st.text_input(
            "Enter your query here:", value=""))
    else:
        st.write("Question is not present in the knowledge base!")
        answer = st.text_input(
            "Enter the appropriate answer for the question below:")
        if st.button("Add Answer"):
            knowledge_base[input_text] = [answer]
            st.write("Answer added successfully!")

# Main function to handle user interaction
def main():
    input_text = st.text_input("Enter your query here:")
    col1, col2 = st.columns([1, 0.1])
    with col1:
        if st.button("Ask"):
            respond(input_text)
    with col2:
        if st.button("Quit"):
            st.write("Thank you for using the Chatbot")

if __name__ == "__main__":
    main()
