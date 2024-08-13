import streamlit as st

st.title(":red[상호] :blue[작용]을 위한 앱")

st.write("쪼랩 원데이클래스 연습 페이지")


col1, col2 = st.columns(2)
with col1:
    st.image("https://cdn.midjourney.com/0f6e6a65-8ecc-4077-afab-29b4983f46bf/0_3.png", width=300)
with col2:
    st.link_button("네이버 영상 바로가기","http://www.naver.com")
    answer = st.text_input('이 케릭터의 이름은 무엇인가요?')
    if answer == "나은":
        st.success('맞았습니다!!!')
    else :
        st.warning('다시 생각해보세요.')

st.latex('2x^2-1')

picture = st.camera_input("Take a picture")
if picture:
    st.image(picture)

tab1, tab2, tab3, tab4 = st.tabs(['봄','여름','가을','겨울'])
tab1.success('봄이에요')
tab2.error('여름이에요')
tab3.info('가을이에요')
tab4.warning('겨울이에요')