import streamlit as st 
import numpy as np
import datetime as dt
import time
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Streamlit Demo",
    page_icon="OIP.jfif",
    layout="wide"
)
st.sidebar.title("Streamlit Topics")
page=st.sidebar.radio(
    "Go to Section",
    ['UI & Layout','Input Widgets','Data Display','Buttons and Files','Media & Status','Charts and Visualization'])
if page=='UI & Layout':
    st.title("UI Creation and Layout")
    st.header("Text Elements")
    st.subheader("SubHeader Example")
    st.text("This is text")
    st.write("It can show text, numbers, tables, etc..")
    st.markdown("**Markdown** supports _formatting_")   
code='''
def add(a,b):
    return a+b
print(add(3,7))'''
st.code(code,language='python')
st.divider()
st.header("Columns and Expander")
col1, col2=st.columns(2)
with col1:
    st.success("Column 1 content")
with col2:
    st.warning("Column 2 content")
with st.expander("Click to Expand"):
    st.write("Hidden content Shown here")
if page =='Input Widgets':
    st.title("Inputs Widgets and Interactivity")
    name=st.text_input("Enter name")
    feedback=st.text_area("Enter feedback")
    age=st.number_input('AGE',1,100,18)
    rating=st.slider("Rate sessions",1,10,5)
    course=st.selectbox("Select Course",['FSD-1','Python-1','PS','DE'])
    days=st.multiselect('Preferred Days',['Mon','Tue','Wed','Thurs','Fri','Sat','Sun'])
    mode=st.radio('Mode',['OFFLINE','ONLINE'])
    subscribe=st.checkbox('Subscribe')
    exam_date=st.date_input("Exam", dt.date.today())
    exam_time=st.time_input("Exam Time",dt.time(9,0))
    
    st.markdown('## Live Output')
    st.write(f'Name:{name}')
    st.write(f'Age:{age}')
    st.write(f'Course:{course}')
    st.write(f'Mode:{mode}')
    st.write(f'Subscribed:{subscribe}')
    st.write(f'Date:{exam_date}')
    st.write(f'Time:{exam_time}')
elif page =='Data Display':
    st.title("Displaying Data")
    data={
        'Student':['A','B','C'],
        'Price':[85,90,99],
        'Pass':[True,True,True]
    }
    df=pd.DataFrame(data)
    st.subheader('Dataframe')
    st.dataframe(df)
    st.subheader('Table')
    st.table(df)
    st.subheader('JSON')
    st.json(data)
elif page =='Buttons and Files':
    st.title("Buttons, File Upload and Download")
    upload_file=st.file_uploader('Upload CSV',type=['csv'])
    if upload_file:
        df=pd.read_csv(upload_file)
        st.dataframe(df)
    if st.button('Generate Sample Data'):
        df=pd.DataFrame({
            'Student':['A','B','C'],
            'Marks':[86,56,78]
        })
        st.table(df)
        csv=df.to_csv(index=False).encode('utf-8')
        st.download_button('Download CSV',
                           csv,
                           'marks.csv')
elif page=='Media & Status':
    st.title('Media and Status')
    st.success('Operation Successfull')
    st.info('This is some information')
    st.warning('This is a warning')
    st.error('This is an error')
    if st.button('Start Task:'):
        progress=st.progress(0)
        with st.spinner('Processing....'):
            for i in range(100):
                time.sleep(0.02)
                progress.progress(i+1)
        st.success('Task completed')
    st.subheader('Media Display')
    st.image('OIP.jfif',width='content')
    st.audio('sampleaudio.mp3')
    st.video('samplevideo.mp4')
elif page=='Charts and Visualization':
    st.title('Charts and Visualization')
    x=np.arange(1,101)
    y=np.random.randint(1,101,100)
    st.subheader('Matplotlib Line Chart')
    plt.plot(x,y,marker='*',c='black')
    plt.xlabel('X-label')
    plt.ylabel('Y-label')
    st.pyplot(plt)
    st.subheader('Matplotlib Scatter Plot')

    plt.figure()
    plt.scatter(x,y,cmap='gist_rainbow')
    plt.title('Random Scatter Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.colorbar()
    st.pyplot(plt)
    
    st.subheader('Streamlit Built-in Line Chart')
    data={
        'x':x,
        'y':y
    }
    df=pd.DataFrame(data)
    st.line_chart(df['y'])
    st.bar_chart(df['y'])
    st.area_chart(df['y'])
    