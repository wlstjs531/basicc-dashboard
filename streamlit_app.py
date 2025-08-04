import streamlit as st
import pandas as pd

st.sidebar.title("단계별 챕터")
chapter = st.sidebar.radio(
    "챕터를 선택하세요",
    ("1. 핵심개념 이해하기", "2. 개념 탐구하기", "3. 핵심 개념 삶에 디자인 하기")
)

if chapter == "1. 핵심개념 이해하기":
    st.title("1. 핵심개념 이해하기")

    tab1, tab2 = st.tabs(["학생별 작성 내용", "구글시트로 내보내기 안내"])

    with tab1:
        # 1. 읽기 자료
        st.header("1) 읽기 자료")
        topic = st.text_input("개념기반탐구학습 주제를 입력하세요.", key="topic_1")
        uploaded_img = st.file_uploader("읽기 자료(그림 파일)를 업로드하세요.", type=["png", "jpg", "jpeg"], key="img_1")
        if uploaded_img is not None:
            st.image(uploaded_img, caption="업로드한 읽기 자료", use_column_width=True)

        # 2. 어휘력 확인 문제
        st.header("2) 어휘력 확인 문제")
        st.subheader("2-1. 어휘력 확인하기")
        words = ["근로자", "기후위기", "온실가스"]
        if "vocab_inputs_1" not in st.session_state or len(st.session_state.vocab_inputs_1) != 3:
            st.session_state.vocab_inputs_1 = [["", ""] for _ in words]

        for i, word in enumerate(words):
            st.write(f"**{word}**")
            col1, col2 = st.columns(2)
            with col1:
                guess = st.text_input(f"내가 짐작한 뜻 - {word}", value=st.session_state.vocab_inputs_1[i][0], key=f"guess1_{i}")
            with col2:
                dict_mean = st.text_input(f"사전에서 찾은 뜻 - {word}", value=st.session_state.vocab_inputs_1[i][1], key=f"dict1_{i}")
            st.session_state.vocab_inputs_1[i] = [guess, dict_mean]

        result_df = pd.DataFrame({
            "단어": words,
            "내가 짐작한 뜻": [row[0] for row in st.session_state.vocab_inputs_1],
            "사전에서 찾은 뜻": [row[1] for row in st.session_state.vocab_inputs_1]
        })
        st.write("입력 결과:")
        st.table(result_df)

        st.subheader("2-2. 단어 활용 문장 만들기")
        selected_word = st.selectbox("아래 단어 중 하나를 골라 문장을 작성해보세요.", words, key="selected_word_1")
        example_sentences = {
            "근로자": "예시>근로자: 최저임금 인상은 근로자들의 생활 수준을 높이는데 중요한 역할을 한다.",
            "기후위기": "예시>기후위기: 기후위기는 전 세계적으로 심각한 문제로 대두되고 있다.",
            "온실가스": "예시>온실가스: 온실가스 배출을 줄이기 위한 노력이 필요하다."
        }
        st.info(example_sentences[selected_word])
        user_sentence = st.text_area(f"{selected_word}를 활용한 문장을 작성하세요.", key="sentence_input_1")

        # 3. 문해력 확인 문제
        st.header("3) 문해력 확인 문제")

        st.subheader("3-1. 내용과 일치하는 것에 O, 일치하지 않은 것에 X표 하세요.")
        q1 = st.radio("∎ 플라스틱은 분해가 쉬워 자연에서 빠르게 사라진다.", ("O", "X"), horizontal=True, key="q1_1")
        q2 = st.radio("∎ 플라스틱은 석유를 원료로 하며, 생산과정에서 많은 이산화탄소가 발생한다.", ("O", "X"), horizontal=True, key="q2_1")

        st.subheader("3-2. 글의 내용에 맞게 알맞은 표현을 골라 하세요.")
        a1 = st.radio("∎플라스틱이 햇빛에 노출되면 ( )을/를 배출하여 기후변화에 영향을 준다.",
                    ["수분", "온기", "온실가스", "산소"], horizontal=True, key="a1_1")
        a2 = st.radio("∎플라스틱 쓰레기 문제는 단순한 쓰레기 문제가 아니라 ( )와 연결된다.",
                    ["지진 발생", "기후위기", "경제 위기", "교통 문제"], horizontal=True, key="a2_1")

        st.subheader("3-3. 빈칸에 알맞은 단어를 글에서 찾아 쓰세요.")
        blank1 = st.text_input("∎ 플라스틱 쓰레기가 햇볕에 노출되면 미세하게 분해되면서 ( ), 에틸렌 등의 온실가스를 내뿜는다.", key="blank1_1")
        blank2 = st.text_input("∎ 플라스틱 소비는 단순한 ‘쓰레기 문제’가 아니라, ( )와 직결된 환경 문제이다.", key="blank2_1")

        st.subheader("3-4. 내용 요약 표")
        summary_title = st.text_input("내용 요약(제목)", key="summary_title_1")
        col1, col2 = st.columns(2)
        with col1:
            main_word = st.text_input("중심단어 찾기", key="main_word_1")
        with col2:
            summary = st.text_area("내용 요약하기", key="summary_1")

    with tab2:
        st.header("구글시트로 내보내기 안내")
        st.markdown("""
1. 위의 학생별 작성 내용을 모두 입력한 후,  
2. 아래 버튼을 클릭하면 CSV 파일로 다운로드할 수 있습니다.  
3. 다운로드한 CSV 파일을 구글시트에서 불러오면 학생별 결과를 관리할 수 있습니다.
        """)
        if st.button("학생 입력 내용 CSV로 다운로드", key="download_btn_1"):
            csv_df = pd.DataFrame({
                "주제": [st.session_state.get("topic_1", "")],
                "근로자_내뜻": [st.session_state.vocab_inputs_1[0][0]],
                "근로자_사전뜻": [st.session_state.vocab_inputs_1[0][1]],
                "기후위기_내뜻": [st.session_state.vocab_inputs_1[1][0]],
                "기후위기_사전뜻": [st.session_state.vocab_inputs_1[1][1]],
                "온실가스_내뜻": [st.session_state.vocab_inputs_1[2][0]],
                "온실가스_사전뜻": [st.session_state.vocab_inputs_1[2][1]],
                "문장작성_단어": [st.session_state.get("selected_word_1", "")],
                "문장작성": [st.session_state.get("sentence_input_1", "")],
                "일치OX1": [st.session_state.get("q1_1", "")],
                "일치OX2": [st.session_state.get("q2_1", "")],
                "표현선택1": [st.session_state.get("a1_1", "")],
                "표현선택2": [st.session_state.get("a2_1", "")],
                "빈칸1": [st.session_state.get("blank1_1", "")],
                "빈칸2": [st.session_state.get("blank2_1", "")],
                "요약제목": [st.session_state.get("summary_title_1", "")],
                "중심단어": [st.session_state.get("main_word_1", "")],
                "요약내용": [st.session_state.get("summary_1", "")]
            })
            csv = csv_df.to_csv(index=False).encode('utf-8-sig')
            st.download_button(
                label="CSV 다운로드",
                data=csv,
                file_name="core_concept_understanding_result.csv",
                mime="text/csv"
            )

elif chapter == "2. 개념 탐구하기":
    st.title("2. 개념 탐구하기")
    # ...이전 코드 유지...

elif chapter == "3. 핵심 개념 삶에 디자인 하기":
    st.title("3. 핵심 개념 삶에 디자인 하기")
    # ...이전 코드 유지...