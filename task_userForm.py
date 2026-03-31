import streamlit as st

with st.form("user_input_form") :
    st.subheader("사용자 입력 폼")

    name = st.text_input("이름")
    
    age = st.number_input("나이", min_value = 1, value = 1, step = 1)

    agreement = st.checkbox("약관에 동의합니다")

    submitted = st.form_submit_button("제출")

if submitted :
    st.write(f"이름 : {name}, 나이 : {age}")

    if agreement :
        st.success("약관에 동의했습니다.")