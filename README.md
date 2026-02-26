# 📄 🚀 PDF 문서 AI 요약 서비스 (PDF Summary App)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://pdf-summary-app-pa9iqvg3d4gsnecjbrvw5t.streamlit.app/)

> 🔗 **서비스 링크:** https://pdf-summary-app-pa9iqvg3d4gsnecjbrvw5t.streamlit.app/

사용자가 PDF 문서를 업로드하면, AI가 문서의 내용을 분석하여 **핵심 내용을 3~5문장의 자연스러운 한국어 문장으로 자동 요약**해 주는 웹 서비스입니다.

## 🌟 주요 기능
* **간편한 PDF 업로드:** Streamlit UI를 통해 손쉽게 PDF 파일을 드래그 앤 드롭으로 업로드할 수 있습니다.
* **빠르고 정확한 AI 요약:** LangChain과 OpenAI의 `gpt-4o-mini` 모델을 활용하여 방대한 문서의 핵심을 빠르게 추출합니다.
* **사용자 맞춤형 보안 (BYOK):** 공용 API 키를 하드코딩하지 않고, 개별 사용자가 직접 본인의 OpenAI API 키를 사이드바에 입력하여 안전하게 사용할 수 있습니다.

## 🛠️ 기술 스택
* **Web Framework:** [Streamlit](https://streamlit.io/)
* **LLM & AI Orchestration:** [LangChain](https://www.langchain.com/), [OpenAI API](https://openai.com/) (`gpt-4o-mini`)
* **문서 전처리:** PyPDF2, langchain-text-splitters (CharacterTextSplitter)
* **임베딩 및 벡터 스토어 (필요시 확장 가능):** sentence-transformers, FAISS 

## 💻 로컬에서 실행하는 방법

### 1. 저장소 클론
```bash
git clone https://github.com/wqhekjbwdsaq123/pdf-summary-app.git
cd pdf-summary-app
```

### 2. 패키지 설치
Python 환경이 구성되어 있는지 확인한 후, 다음 명령어로 필요한 라이브러리를 설치합니다.
```bash
pip install -r requirements.txt
```

### 3. 애플리케이션 실행
```bash
streamlit run app.py
```
실행 후 브라우저에서 `http://localhost:8501`로 접속하여 이용할 수 있습니다.

## ☁️ 배포 (Streamlit Community Cloud)
이 프로젝트는 Streamlit Community Cloud에 최적화되어 있습니다.
GitHub 레포지토리를 Streamlit Share에 연결하고 `app.py`를 메인 파일로 지정하면, 추가 설정 없이 누구나 본인의 API 키를 입력하여 사용할 수 있습니다.
