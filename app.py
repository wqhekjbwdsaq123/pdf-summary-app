import streamlit as st
import os
from PyPDF2 import PdfReader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Streamlit 페이지 설정
st.set_page_config(page_title="PDF 요약 서비스", page_icon="📄")
st.title("📄 🚀 PDF 문서 AI 요약 서비스")
st.write("PDF 파일을 업로드하시면 AI가 내용을 분석하여 3~5문장으로 핵심을 요약해 드립니다.")

# 사이드바에서 API 키 입력받기
with st.sidebar:
    st.header("설정")
    api_key = st.text_input("OpenAI API 키를 입력하세요", type="password")
    st.markdown("[OpenAI API 키 발급받기](https://platform.openai.com/api-keys)")

# PDF 파일 업로드 구역
uploaded_file = st.file_uploader("PDF 파일을 여기에 드래그하거나 클릭해서 업로드하세요.", type="pdf")

if uploaded_file is not None:
    # API 키 확인
    if not api_key:
        st.warning("⚠️ 요약을 시작하려면 왼쪽 사이드바에 OpenAI API 키를 입력해주세요.")
    else:
        with st.spinner('해당 문서를 읽고 분석하는 중입니다. 잠시만 기다려주세요...'):
            try:
                # 1. PDF 텍스트 추출
                pdf_reader = PdfReader(uploaded_file)
                text = ""
                for page in pdf_reader.pages:
                    text += page.extract_text()
                
                # 2. 텍스트 추출 검증 및 전처리
                if not text.strip():
                    st.error("문서에서 텍스트를 추출할 수 없습니다. 스캔본(이미지) PDF일 수 있습니다.")
                else:
                    # 4. LLM 요약 요청 (ChatOpenAI)
                    # gpt-4o-mini 등 빠르고 범용적인 모델 사용, 사이드바에서 입력받은 API 키 전달
                    llm = ChatOpenAI(temperature=0, model_name="gpt-4o-mini", api_key=api_key)
                    
                    # 새로운 프롬프트 및 체인 구조 (LCEL)
                    prompt = PromptTemplate.from_template(
                        "다음 텍스트의 핵심 내용을 분석하여 한국어로 3문장에서 5문장 내외의 자연스러운 요약문으로 작성해 줘:\n\n{text}"
                    )
                    chain = prompt | llm | StrOutputParser()
                    
                    # 텍스트 전체 길이를 압축 요약
                    # 텍스트가 너무 길면 모델 제한에 걸릴 수도 있지만, 
                    # GPT-4o-mini는 128k 토큰까지 지원하므로 대부분의 PDF 전문을 바로 처리 가능합니다.
                    summary_text = chain.invoke({"text": text})
                    
                    # 결과 출력
                    st.success("✅ 요약이 완료되었습니다!")
                    st.subheader("📝 문서 핵심 요약")
                    st.write(summary_text)

            except Exception as e:
                st.error(f"오류가 발생했습니다: {e}")
