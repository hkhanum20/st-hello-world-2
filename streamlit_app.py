import streamlit as st
st.set_page_config(page_title="Hira Khanum's PMM Portfolio", page_icon=":tada:", layout= "wide")
st.subheader("Hi, I am Hira :wave:")
st.title("Product Marketing Manager")
st.write("I am a data-driven, “full-stack” Product Marketer in enterprise software. And I am on a mission to move the world forward using technology to make opportunities for growth more accessible.")
st.write("[Learn More>](https://docs.google.com/presentation/d/1zN2YIOizD9GGoVD_6g4OZdNiEoJbCqgO4ultu9yeWNE/edit?usp=sharing)")

st.write("---")
left_column, right_column=st.columns(2)
with left_column:
    st.header("Who I am:")
    st.write("##")
    st.write(
        """
- Ensuring that market realities and only the most important attributes for customer and market adoption influence GTM, I AM AN AMBASSADOR OF INSIGHTS.
- Directing the vision of the go to market plan, I AM A STRATEGIST.
- Shaping the way the world sees our product and enabling others to tell its story, I AM A STORYTELLER.
- Connecting insight and action to drive product adoption by shaping market perception through strategic marketing activities, I CREATE LASTING VALUE.
"""
        )

st.write("---")
st.header("My Projects")


st.write("---")
st.header(":mailbox: Get in Touch!")
st.write("##")

contact_form = """
<form action="https://formsubmit.co/hk3033@columbia.edu" method="POST">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email"placeholder="Your email" required>
     <textarea name="message" placeholder="Your Message here" required></textarea>
     <button type="submit">Send</button>
</form>
"""
left_column, right_column= st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()
    
