import streamlit as st 
st.title("2205a21035-ps11")
def Gen_Eff(V,CL,IL,K,Rse,Ra):
    CUL=(K*IL)**2*(Rse+Ra)
    Eff=((K*V*IL-CL-CUL)/(K*V*IL))*100
    return CUL,Eff



st.text("calculate the efficiency f DC series Generator various loads")

col1,col2=st.columns(2)
with col1:
    with st.container(border=True):
        V=st.number_input("V:in volts",value=1)
        IL=st.number_input("IL:in amps",value=1)
        Rse=st.number_input("Rse:in ohms",value=0.20)
        Ra=st.number_input("Ra:in ohms",value=0.10)
        CL=st.number_input("CL:in watts",value=1) 
        K=st.number_input("constant(K)",value=1) 
    compute=st.button("compute")


with col2:
    with st.container(border=True):
        if compute:
            CUL,Eff=Gen_Eff(V,CL,IL,K,Rse,Ra,)
            st.write(f"CUL={CUL:.2f}Watts")
            st.write(f"Eff={Eff:.2f}%")