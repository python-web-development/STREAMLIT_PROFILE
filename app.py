import streamlit as st
import pandas as pd
# import matplotlib.pyplot as plt

st.title("SAI VINEELA PEDDINTI")
st.write("PYTHON WEB DEVELOPER")
st.write("vineelapeddinti@gmail.com")
st.write("contact: 267 815 4168")

professional_summary1 = "• Dynamic and results-oriented Python Web Developer with 4 years of experience in designing, developing, and maintaining web applications."
professional_summary2 = "•	Proficient in leveraging modern frameworks such as Flask, Django, FastAPI and Streamlit to deliver robust, scalable, and high-performance solutions."

skills = ["Python", "APIs: FastAPI, FLASK, Graphql", "SQL & MongoDb"]

experience = [
    {"Company": "IT Rysources", "Position": "Python Web Developer", "Duration": "2022-Till date"},
    {"Company": "Infosys Technologies", "Position": "Python Developer", "Duration": "2018-2021"},
    {"Company": "Infosys Technologies", "Position": "SAP ABAP Developer", "Duration": "2014-2018"},
    {"Company": "Wipro Technologies", "Position": "SAP ABAP Developer", "Duration": "2010-2014"}
]

projects = [
    {"Name": "RBS Budget Optimizer Application", "Description": "Developed an application for The Royal Bank of Scotland (RBS) Banking team to provide customers with an optimized budget required to achieve their financial targets. The application features a budget optimization logic developed in Python using a gradient descent approach, enabling customers to efficiently manage their expenses and savings."},
    {"Name": "Flight Demand Prediction API", "Description": "A FastAPI application is developed to serve the model, allowing users to make predictions through a RESTful API. "},
    {"Name": "Dynamic Dashboard Data Visualization ", "Description": "This project aims to develop a dynamic dashboard for data visualization using a Flask-based REST API backend with security features, connected to an SQL database "},
    {"Name": "Vendor Management Application", "Description": "An application to categorize the vendors based on their services provided . Developed few screens to show in the mobile device for warehouse management activites "}

]

def main():
    st.title("My Professional Profile")

    # with st.tabs(["Professional Summary", "Skills", "Experience", "Projects"]):
    tabs = st.tabs(["Professional Summary", "Skills", "Experience", "Projects"])
    with tabs[0]:
        st.write(professional_summary1)
        st.write(professional_summary2)

    with tabs[1]:
        #     st.write(", ".join(skills))
        st.write(" , ".join(skills))

    with tabs[2]:
        # st.write("Experience Summary Tab")
        st.table(experience)
        for index, exp in enumerate(experience, start=1):
            st.write(f"{index}. Company: {exp['Company']}, Position: {exp['Position']}, Duration: {exp['Duration']}")

    with tabs[3]:
        for project in projects:
            st.subheader(project["Name"])
            st.write(project["Description"])

if __name__ == "__main__":
    main()