import streamlit as st
import pandas as pd
import os 
from io import BytesIO

st.set_page_config(page_title="💿Data sweaper" , layout="wide")
st.title("💿Data sweaper")
st.write("transform your files between CSV and excel formats with built-in data cleaning and visuallization!")


uploaded_files = st.file_uploader(
    "Upload your files (CSV, Excel, PDF, TXT, JPG, PNG):",
    type=["csv", "xlsx", "xls", "pdf", "txt", "jpg", "png"],
    accept_multiple_files=True
)

if uploaded_files: 
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()

        if file_ext == ".csv":
            df = pd.read_csv(file)
            st.write("Genius you can do it ")
        elif file_ext in [".xlsx", ".xls"]:
          df = pd.read_excel(file)
        else:
            st.error (f"unsupported file type: {file_ext}")
            continue

        st.write(f"**File Name:** {file.name}")
        st.write(f"**File Size:** {file.size / 1024:.2f} KB")


        st.write("preview the head of the dataframe")
        st.dataframe(df.head())

        st.subheader("data cleaning options")
        if st.checkbox(f"clean data for {file.name}"):
            col1 , col2 = st.columns(2) 

            with  col1:
                if st.button (f"remove the duplicates {file.name}"):
                    df.drop_duplicates(inplace=True)
                    st.write("Duplicates removed!")

            with  col2:
                if st.button (f"fill missing values for {file.name}"):
                    numeric_cols = df.select_dtypes(include=['number']).columns
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                    st.write("Missing values have been filled👍")

                st.subheader("Select coloums to convert")
                columns = st.multiselect(f"choose columns for {file.name}" , df.columns , default=df.columns)
                df = df[columns]

                st.subheader("📊 Data visulization")
                if st.checkbox(f"Show visulization {file.name}"):
                    st.bar_chart(df.select_dtypes(include='number').iloc[:,:2])

                st.subheader("🔄 Conversion options")
                conversion_type = st.radio(f"Convert {file.name} to:" ["CSV" , "excel"] , key=file.name)

                if st.button(f"Convert {file.name}"):
                    Buffer = BytesIO()
                    if conversion_type == "CSV":
                        df.to_csv(Buffer , index=False)
                        file_name = file.name.replace(file_ext , ".csv")
                        mime_type= "text/csv"
                    elif conversion_type == "excel":
                        df.to_excel(Buffer , index=False)
                        file_name = file.name.replace(file_ext , ".xlsx")
                        mime_type= "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                        Buffer.seek(0)


                        st.download_button(
                            label=f"📩Download {file.name} as {conversion_type}", 
                            data=Buffer,
                            file_name = file_name,
                            mime= mime_type
                        )

                        st.success("🎉🎊 All files processed")




