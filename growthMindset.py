import streamlit as st
st.set_page_config(page_title="Growth Mindset", page_icon="🗿")
stst.header("welcome to the Growth Mindset page!")
st.write("This is a page dedicated to the growth mindset. Here, you can learn about the concept of growth mindset and how it can help you in your personal and professional life.")

st.header("today Growth Mindset")
st.write("Today, we will explore the concept of growth mindset and how it can help you achieve your goals. We will also discuss some practical tips on how to develop a growth mindset and overcome challenges.")

st.header("whats your chanllenge today")
user_input = st.text_input("Please enter your challenge for today:")
if user_input: 
    st.write(f"Your challenge for today is: {user_input}")
    st.write("Remember, challenges are opportunities for growth. Embrace them and learn from them!")
    else:
        st.write("Please enter a challenge to proceed.")

    st.header("celebrate your success")
    achievement = st.text_input("Please enter your achievement for today:")
    if achievement:
        st.write(f"Your achievement for today is: {achievement}")
        st.write("Congratulations! Celebrate your success and keep pushing forward.")
        else:
            st.write("Please enter an achievement to proceed.")

           st.write("Thank you for visiting the Growth Mindset page! Remember, a growth mindset is all about embracing challenges, learning from failures, and celebrating successes. Keep growing and thriving!")
           st.write("motivation is the key to success")
              st.write("created by ABDUL SUBHAN")