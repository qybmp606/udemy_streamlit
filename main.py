import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i +1)
    time.sleep(0.1)

'Done!!'

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')

# text = st.text_input('あなたが趣味を教えてください',)
# condition = st.slider('あなたの今の調子は？', 0, 100, 50)

# 'あなたの好きな趣味:' , text ,'です'
# 'コンディション' , condition

# if st.checkbox('Show Image'):
#     img = Image.open('company.jpg')
#     st.image(img, caption='Kouhei Imanishi', use_column_width=True)

expander1 = st.expander('問合せ1')
expander1.write('問合せ1の回答')
expander2 = st.expander('問合せ2')
expander2.write('問合せ2の回答')
expander3 = st.expander('問合せ3')
expander3.write('問合せ3の回答')