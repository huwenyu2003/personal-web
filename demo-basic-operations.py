import streamlit as st
st.title("Hello, 欢迎光临我的世界！")
st.header("You need to comprehend my character")
st.subheader("display my character")
st.text("温柔美丽大方得体善良热心")

st.markdown('this is an image: ![Alt Text](https://tse1-mm.cn.bing.net/th/id/OIP-C.Rmu2HNfPTot9nN9kWt0dbgHaNK?w=106&h=180&c=7&r=0&o=5&dpr=1.5&pid=1.7)')
if st.checkbox("Yes/No"):
    st.text("That must be right")


status = st.radio("select button:" ,
                  ('trust',
                   'doubt'))
if status == 'trust':
    st.success("恭喜你，你非常了解我！")
else:
    st.success("怎么回事，怎么一点不相信我！")

character = st.multiselect("character:",
               ['温柔',
                '美丽',
                '大方得体',
                '善良热心'])
st.write("You selected: ", character)

if st.button("reward"):
    st.text("微信发我红包")

answer = st.text_input("这是你自愿的吗:")
if st.button("answer"):
    st.write("of course, ", answer)

level = st.slider("Select your willness level", 1, 5)
st.write("You selected: ", level)

from fastai.vision.all import *
upload_img = st.file_uploader("Upload an image",
                               type=['jpg',
                                      'png'])

if upload_img is not None:
    img = PILImage.create(upload_img)
    st.image(img.to_thumb(256,256), 
             caption="Uploaded Image")

    
