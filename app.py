from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="S Technologies", page_icon=":eyes:", layout="wide")

               
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

lottie_coding = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_o6spyjnc.json")
img_contact_form = Image.open("images/Predict Receivables.png")
img_predict_receivable = Image.open("images/Predict Receivables.png")
img_previous_balance_age = Image.open("images/Previous Balances Aging.png")
img_browse_ledger=Image.open("images/Browse Ledgers.png")


with st.container():
    st.subheader("Hi, I am Sundar :wave:")
    st.title("A TDL Programmer in Chennai")
    st.write("I am passionate about finding ways to use Tally to be more efficient and effective in business Settings.")
    st.write("[Learn more>] (https://www.youtube.com/@sundar8601/videos)")


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write('##')
        st.write(
            """
            On my youtube channel I am displaying Advanced Tally TDL working videos for the people who
            are looking for a way to leverage the power of Tally in their day to day work, or
            struggling  with repetitive tasks in Tally and are looking for a way to use Tally automation
            and want to know the capability of TDLs and thinking - "there has to better way".

            If this sounds interesting to you, consider subscribing and turning on the notifications, so you don't miss any content.
            """
        )

        st.write("[Youtube Channel >] (https://www.youtube.com/@sundar8601/videos)")
    
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

with st.container():

    st.write('---')
    st.header("Tally TDL Videos")
    #st.write("##")
    image_column, text_column = st.columns((1,2))

    with image_column:
        st.image(img_previous_balance_age)

    with text_column:
        st.subheader("Previous Balance Ageing")
        st.write(
            """
            Monitoring Receivables is the key role of Finance Department.
            If it is increases we have to find the customers who are holding company money for long period, 
            if it is decreasing who are all reduces their balances which they may started doing business with
            some other competitors.  

            This report will shows the previous aging which help us to take decision accordingly.
            """
        )
        st.markdown("[Watch Video ...] (https://www.youtube.com/watch?v=quddq0bLqTw)")


with st.container():

    image_column, text_column = st.columns((1,2))

    with image_column:
        st.image(img_predict_receivable)

    with text_column:
        st.subheader("Predict Receivable")
        st.write(
            """
            We can not expect all our customers honor their dues in time.  Few of them may do so.
            Many of them may take extra few days.  Tally uses a method of PERFORMANCE in days.

            For example, if you give 30 days credit for a customer X, but this X used to pay always after 32 or 35 or even he
            may take 40 days.  Tally always calculated his performance as an average days he takes to pay due.

            Based on this performance, we can approximately drive how much fund we are going to receive from our
            customers for upto next 6 weeks.
            """
        )
        st.markdown("[Watch Video ...] (https://www.youtube.com/watch?v=Dqlzyx2Nd2M)")

with st.container():

    image_column, text_column = st.columns((1,2))

    with image_column:
        st.image(img_browse_ledger)

    with text_column:
        st.subheader("Browse Ledgers")
        st.write(
            """
            Ledger view made simple.  
            Always we wanted to compare ledger vouchers. 
            In this TDL you can view ledger vouchers with bill wise breakup and 
            contact details all along in single screen.
            """
        )

        st.markdown("Watch Video ...] (https://youtu.be/nDs0l8Y7bxo)")


with st.container():
    st.write("---")
    st.header("Get in touch with me")
    st.write("##")
    contact_form = """
    <form action="https://formsubmit.co/tallystechnologies@gmail.com" method="POST">
     <input type = "hidden" name = "_captcha" value="false">
     <input type="text" name="name" placeholder = "Your Name" required>
     <input type="email" name="email" placeholder = "Email" required>
     <textarea name="message" placeholder = "Your message here" required></textarea>
     <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)

    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)

    with right_column:
        st.empty()