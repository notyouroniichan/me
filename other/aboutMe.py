import streamlit as st
from PIL import Image
import io
import base64
from st_social_media_links import SocialMediaIcons

social_media_links = [
    "https://www.linkedin.com/in/tushar-vinayak/",
    "https://github.com/notyouroniichan",
    "https://www.instagram.com/tusharvinayak_/",
    "https://www.hackerrank.com/profile/tusharvinayak6",
]

# Load the image
image = Image.open("images/profile.jpeg")

# Convert the image to bytes
buffer = io.BytesIO()
image.save(buffer, format="PNG")
buffer.seek(0)
img_str = base64.b64encode(buffer.read()).decode('utf-8')

# Display the image using HTML with CSS for a circular profile picture
st.markdown(
    f"""
    <style>
    .center {{
        display: block;
        margin-left: auto;
        margin-right: auto;
        text-align: center;
    }}
    .profile-pic {{
        border-radius: 15%;
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 250px;
        height: 250px;
    }}
    .text {{
        font-size: 20px;
        line-height: 2;
    }}
    </style>
    <img src="data:image/png;base64,{img_str}" class="profile-pic">
    <div class="center">
        <h1>Tushar&nbsp;&nbsp;Vinayak</h1>
        <div class = "text", style = "text-align: justify;">Results-driven software engineer with around 2 years of expertise in machine learning, adept at
            creating scalable solutions. Transitioning to Data Science, leveraging a solid foundation in
            algorithm development and model deployment. Proven ability to analyze complex datasets,
            extract meaningful insights, and drive data-driven decision-making. Eager to contribute technical
            acumen and innovative problem-solving skills to excel in a dynamic data science role.</div>
    </div>
    """,
    unsafe_allow_html=True,
)

social_media_icons = SocialMediaIcons(social_media_links)
st.divider()
social_media_icons.render(sidebar=False,justify_content='center')
