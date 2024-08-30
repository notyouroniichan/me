import streamlit as st

aboutme = st.Page("other/aboutMe.py",title="About Me", icon=":material/face:")
experience = st.Page("other/WorkEx.py",title="Work Experience", icon=":material/work:")
education = st.Page("other/education.py",title="Education", icon=":material/school:")
projects = st.Page("other/Projects.py",title="Projects", icon=":material/stacks:")
acheivements = st.Page("other/acheivements.py",title="Acheivements", icon=":material/trophy:")
contactme = st.Page("other/contact.py",title="Contact Me", icon=":material/connect_without_contact:")

pg = st.navigation([aboutme,experience,education,projects,acheivements,contactme])
pg.run()