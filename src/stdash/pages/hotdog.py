import streamlit as st
import requests 

st.title('핫도그 사진 판별기')
st.subheader('업로드한 이미지로 핫도그 판별')
url = 'http://127.0.0.1:8000/uploadfile/'
uploaded_file = st.file_uploader("이미지 파일을 올려주세요",type=['png','jpg','jpeg'])

if uploaded_file is not None:
    print(type(uploaded_file))
    print(uploaded_file.name)
    print(uploaded_file.size)
    print(uploaded_file.type)

    file_name = uploaded_file.name
    file_type = uploaded_file.type
    file_ext = file_type.split('/')[-1]
    img = uploaded_file.read()

    # 로컬 fastapi 응답 확인
    files = {"file" : (file_name,img, f"image/{file_ext}")}

    response = requests.post(url, files=files)
    result = response.json()
    print(result)
    hotdog = "https://encrypted-tbn3.gstatic.com/shopping?q=tbn:ANd9GcQweb_7o7OrtlTP75oX2Q_keaoVYgAhMsYVp1sCafoNEdtSSaHps3n7NtNZwT_ufZGPyH7_9MFcao_r8QWr3Fdz17RitvZXLTU4dNsxr73m6V1scsH3_ZZHRw&usqp=CAE"
    dog = "https://hearingsense.com.au/wp-content/uploads/2022/01/8-Fun-Facts-About-Your-Dog-s-Ears-1024x512.webp"
    # 핫도그 유무에 따라 이미지 출력
    if result['label'] == "hot dog":
        imgurl=hotdog
        st.write("핫도그에요")
        st.image(imgurl)
    else :
        imgurl=dog
        st.write("핫한 도그에요")
        st.image(imgurl)

