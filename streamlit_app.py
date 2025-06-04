import streamlit as st

"""
1. Hola mundo interactivo
"""
st.title("🎈 Hello World!")
nombre = st.text_input("¿Cómo te llamas?")

if 'msg' not in st.session_state:
    st.write("")

if nombre:
    st.session_state.msg = f"Hello, {nombre}!"
    st.write(st.session_state.msg)


"""
2. Contador de clicks
"""
st.title("🎈 Clicks counter")
if 'counter' not in st.session_state:
    st.session_state.counter = 0

if st.button("Increase counter"):
    st.session_state.counter += 1
st.write(st.session_state.counter)


"""
3. Selector de color
"""
st.title("🎈 Color selector")
color = st.color_picker("Choose a colour", "#ff00ff")
st.write(f"Has seleccionado el color {color}")

