import streamlit as st

st.title("Exploring Streamlit")

st.header("Header of Streamlit")
st.subheader("Sub - Header of Streamlit")

st.text("This is an Example Text")

st.success("Success")
st.warning("Warning")
st.info("information")
st.error("Error")

if st.checkbox("Select/Unselect"):
    st.text("User selected the checkbox")
else:
    st.text("user has not selected the checkbox")

state = st.radio("What is your Favorite Color ? ",
("Red","Green","Blue"))

if state == "Green":
    st.success("Thats the color of grass")

Occupation = st.selectbox("What do you do ?",
["Student","Vlogger","Engineer"])

st.text(f"selected option is {Occupation}")

if st.button("Example button"):
    st.error("you clicked it")

st.sidebar.header("Heading of Sidebar")
st.sidebar.text("Creater by ANUSHA")