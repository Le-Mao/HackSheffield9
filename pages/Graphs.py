import streamlit as st 
#import connectionTest
import main

st.set_page_config(
    page_title="Graphs",
    page_icon=":bar_chart:",
    layout="wide",
)

st.title("Graphs")
st.markdown("These are our graphs for displaying animal populations and food avilability.")
col1, col2 = st.columns(2)
# df1, df2, df3 = connectionTest.create_graphs()
df1 = main.main()
#with col1:
st.markdown("This Graph shows the equilibrium reached in the following food chain:")
st.markdown("1. Moose eats Plant")
st.markdown("2. Wolf eats Moose")
st.markdown("3. Humans eat everything")
st.line_chart(df1)
    #st.line_chart(df2)

#with col2: 
    #st.title("Other Graphs")
    #st.line_chart(df3)


