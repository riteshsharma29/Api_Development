import streamlit as st
import json

st.title("Dynamic REST api response builder")

# passing integer input
num_of_param = st.sidebar.number_input('Provide Number of Parameters Required for the REST response', min_value=2)

# reading number of param required
params = list(range(num_of_param))
k_param = params
v_param = params

# empty dictionary
d = {}
for i in range(0,len(params)):
    # place 3 columns per row for i
    c1, c2, c3 = st.columns(3)
    with c1:
        k = st.text_input("Parameter Key " + str(params[i]))
    with c3:
        dt = st.selectbox("datatype of Value " + str(v_param[i]),["int","float","string","bool"])
    # based on datatype append key value
    with c2:
        if dt == "int":
            # passing integer input
            v = st.number_input('Parameter Value ' + str(i), min_value=0)
            d[k] = v
        elif dt == "float":
            # passing float input
            v = st.number_input('Parameter Value ' + str(i), step = 1., format = "%.2f")
            d[k] = v
        elif dt == "bool":
            # passing boolean input
            v = st.selectbox("Parameter Value",["True","False"])
            if v == "True":
                d[k] = True
            elif v == "False":
                d[k] = False
        elif dt == "string":
            v = st.text_input("Parameter Value " + str(i))
            d[k] = v


st.sidebar.text_area("JSON Output", json.dumps([d],indent=4), height=200)