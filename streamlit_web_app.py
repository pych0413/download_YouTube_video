from main import *
import streamlit as st

st.title('Online YouTube downloader')
'This is the free tool for you to download the YouTube video or mp3'

yt_url = st.text_input("YouTube link")
res_option = st.selectbox('How would you like to be download?', ('1080p', '720p', '480p'))


#check the yt url whether valid
def check_yt_url(yt_url):
    try:
        yt = YouTube(yt_url, on_progress_callback=onProgress )
        return True
    except:
        return False


if st.button("Download"):
    if check_yt_url(yt_url)==False:
        st.error("The url link is invalid, plz ckeck and enter again.")
    else:
        st.write('you selected:', res_option)
        if res_option == '1080p':
            os.system("python main.py {} -fhd".format(yt_url))
        elif res_option == '720p':
            os.system("python main.py {} -hd".format(yt_url))
        else:
            os.system("python main.py {} -sd".format(yt_url))
        st.write('Done')


        #os.system("python main.py {}".format(yt_url))
    




