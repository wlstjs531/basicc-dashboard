import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

# 왼쪽 바 맨 위에 읽기 자료 탑재 탭 추가
with st.sidebar:
    st.markdown("### 📚 읽기 자료 탑재")
    uploaded_sidebar_file = st.file_uploader("읽기 자료(이미지) 업로드", type=["png", "jpg", "jpeg"], key="sidebar_reading_img")
    if uploaded_sidebar_file is not None:
        st.image(uploaded_sidebar_file, caption="업로드한 읽기 자료", use_column_width=True)
    st.divider()

st.sidebar.title("개념기반탐구 연계 MYP디자인 수업")
chapter = st.sidebar.radio(
    "단계별로 학습",
    (
        "1단계 핵심개념 이해하기",
        "2단계 개념 탐구하기",
        "3단계 핵심개념 삶에 디자인하기"
    )
)

tab_main1, tab_main2, tab_main3 = st.tabs([
    "1단계 핵심개념 이해하기",
    "2단계 개념 탐구하기",
    "3단계 핵심개념 삶에 디자인하기"
])

with tab_main1:
    st.title("1단계 핵심개념 이해하기")
    tab0, tab1, tab2, tab3 = st.tabs(["읽기 자료", "어휘력 확인", "문해력 확인", "구글시트로 내보내기 안내"])

    with tab0:
        st.header("읽기 자료")
        if "reading_title" not in st.session_state:
            st.session_state.reading_title = ""
        reading_title = st.text_input("개념기반탐구학습 주제를 입력하세요.", value=st.session_state.reading_title, key="reading_title_input")
        if st.button("제목 저장", key="save_reading_title"):
            st.session_state.reading_title = reading_title
            st.success("제목이 저장되었습니다.")
        st.markdown(f"**주제:** {st.session_state.reading_title}")

        uploaded_img = st.file_uploader("읽기 자료(그림 파일)를 업로드하세요.", type=["png", "jpg", "jpeg"], key="reading_img")
        if uploaded_img is not None:
            st.image(uploaded_img, caption="업로드한 읽기 자료", use_column_width=True)

    with tab1:
        st.header("어휘력 확인")
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
        st.write("입력 결과:")
        st.table(pd.DataFrame({
            "단어": words,
            "내가 짐작한 뜻": [row[0] for row in st.session_state.vocab_inputs_1],
            "사전에서 찾은 뜻": [row[1] for row in st.session_state.vocab_inputs_1]
        }))
        st.subheader("단어 활용 문장 만들기")
        selected_word = st.selectbox("아래 단어 중 하나를 골라 문장을 작성해보세요.", words, key="selected_word_1")
        example_sentences = {
            "근로자": "예시>근로자: 최저임금 인상은 근로자들의 생활 수준을 높이는데 중요한 역할을 한다.",
            "기후위기": "예시>기후위기: 기후위기는 전 세계적으로 심각한 문제로 대두되고 있다.",
            "온실가스": "예시>온실가스: 온실가스 배출을 줄이기 위한 노력이 필요하다."
        }
        st.info(example_sentences[selected_word])
        user_sentence = st.text_area(f"{selected_word}를 활용한 문장을 작성하세요.", key="sentence_input_1")

    with tab2:
        st.header("문해력 확인")
        st.subheader("내용과 일치하는 것에 O, 일치하지 않은 것에 X표 하세요.")
        q1 = st.radio("∎ 플라스틱은 분해가 쉬워 자연에서 빠르게 사라진다.", ("O", "X"), horizontal=True, key="q1_1")
        q2 = st.radio("∎ 플라스틱은 석유를 원료로 하며, 생산과정에서 많은 이산화탄소가 발생한다.", ("O", "X"), horizontal=True, key="q2_1")
        st.subheader("글의 내용에 맞게 알맞은 표현을 골라 하세요.")
        a1 = st.radio("∎플라스틱이 햇빛에 노출되면 ( )을/를 배출하여 기후변화에 영향을 준다.",
                    ["수분", "온기", "온실가스", "산소"], horizontal=True, key="a1_1")
        a2 = st.radio("∎플라스틱 쓰레기 문제는 단순한 쓰레기 문제가 아니라 ( )와 연결된다.",
                    ["지진 발생", "기후위기", "경제 위기", "교통 문제"], horizontal=True, key="a2_1")
        st.subheader("빈칸에 알맞은 단어를 글에서 찾아 쓰세요.")
        blank1 = st.text_input("∎ 플라스틱 쓰레기가 햇볕에 노출되면 미세하게 분해되면서 ( ), 에틸렌 등의 온실가스를 내뿜는다.", key="blank1_1")
        blank2 = st.text_input("∎ 플라스틱 소비는 단순한 ‘쓰레기 문제’가 아니라, ( )와 직결된 환경 문제이다.", key="blank2_1")
        st.subheader("내용 요약 표")
        summary_title = st.text_input("내용 요약(제목)", key="summary_title_1")
        col1, col2 = st.columns(2)
        with col1:
            main_word = st.text_input("중심단어 찾기", key="main_word_1")
        with col2:
            summary = st.text_area("내용 요약하기", key="summary_1")

    with tab3:
        st.header("구글시트로 내보내기 안내")
        st.markdown("""
1. 위의 학생별 작성 내용을 모두 입력한 후,  
2. 아래 버튼을 클릭하면 CSV 파일로 다운로드할 수 있습니다.  
3. 다운로드한 CSV 파일을 구글시트에서 불러오면 학생별 결과를 관리할 수 있습니다.
        """)
        if st.button("학생 입력 내용 CSV로 다운로드", key="download_btn_1"):
            csv_df = pd.DataFrame({
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

with tab_main2:
    st.title("2단계 개념 탐구하기")
    tab1, tab2, tab3, tab4 = st.tabs(["개념과 사실 구분하기", "탐구질문 만들기", "작문력 확인", "구글시트로 내보내기 안내"])

    with tab1:
        st.header("개념과 사실 구분하기")
        st.markdown("""
- **관계 (Relationship)**: 어떤 것과 어떤 것이 서로 영향을 주고받는 것  
- **시스템 (System)**: 여러 부분이 서로 연결되어 함께 움직이는 구조  
- **지속 가능성 (Sustainability)**: 지금도 쓰고, 미래에도 쓸 수 있도록 자원을 아끼고 지키는 방법  
        """)
        st.markdown("""
- **관계 (Relationship)**: 플라스틱을 많이 쓰면 → 바다에 버려짐 → 바다 생물에게 해로움 → 결국 사람 건강에도 나쁨  
- **시스템 (System)**: 학교는 교장 선생님, 선생님, 학생, 규칙, 교실… 다 연결돼서 움직이죠? 이게 바로 학교 시스템이에요.  
- **플라스틱 시스템**: 플라스틱 생산 → 소비 → 쓰레기 → 바다 → 기후 → 사람까지→ 이 전체 흐름이 하나의 환경 시스템이에요.  
- **지속 가능성 (Sustainability)**: 오늘 플라스틱 컵 하나 덜 쓰면→ 쓰레기 줄고, 환경도 덜 망가져요.→ 이렇게 하면 나도 좋고, 미래 사람들도 좋죠!  
        """)
        fact1 = st.radio("∎ 플라스틱은 석유를 원료로 만들어진다.", ["사실", "개념"], horizontal=True, key="fact1_2")
        fact2 = st.radio("∎ 플라스틱 소비와 기후변화는 서로 연결되어 있다.", ["사실", "개념"], horizontal=True, key="fact2_2")
        st.write("힌트: 관계 / 시스템 / 지속 가능성")
        concept_blank = st.text_input("∎ 플라스틱이 바다에 버려지면 해양 생태계가 영향을 받는다.\n→ 이것은 __________ 개념과 관련이 있다.", key="concept_blank_2")
        my_concept = st.selectbox("개념 선택", ["관계", "시스템", "지속 가능성"], key="my_concept_2")
        st.info("예시>플라스틱 문제는 쓰레기 문제가 아니라 기후와 연결된 하나의 시스템이다.")
        my_sentence = st.text_area("내 문장", key="my_sentence_2")

    with tab2:
        st.header("탐구질문 만들기")
        factual_q1 = st.text_input("사실적 질문 1", key="factual_q1_2")
        factual_a1 = st.text_input("답 1", key="factual_a1_2")
        factual_q2 = st.text_input("사실적 질문 2", key="factual_q2_2")
        factual_a2 = st.text_input("답 2", key="factual_a2_2")
        conceptual_q1 = st.text_input("개념적 질문 1", key="conceptual_q1_2")
        conceptual_a1 = st.text_area("자신의 생각 1", key="conceptual_a1_2")
        conceptual_q2 = st.text_input("개념적 질문 2", key="conceptual_q2_2")
        conceptual_a2 = st.text_area("자신의 생각 2", key="conceptual_a2_2")
        debate_q1 = st.text_input("논쟁적 질문 1", key="debate_q1_2")
        debate_a1 = st.text_area("자신의 생각 1", key="debate_a1_2")
        debate_q2 = st.text_input("논쟁적 질문 2", key="debate_q2_2")
        debate_a2 = st.text_area("자신의 생각 2", key="debate_a2_2")

    with tab3:
        st.header("작문력 확인")
        selected_debate = st.selectbox("논쟁적 질문 선택", [st.session_state.get("debate_q1_2", ""), st.session_state.get("debate_q2_2", "")], key="selected_debate_2")
        my_opinion = st.text_area("나의 생각", key="my_opinion_2")
        counter_opinion = st.text_area("반론", key="counter_opinion_2")
        table_data = [
            ["질문", selected_debate],
            ["나의 생각", my_opinion],
            ["반론", counter_opinion]
        ]
        st.table(pd.DataFrame(table_data, columns=["구분", "내용"]))

        st.subheader("논리적 말하기 (PREP기법) 표로 정리")
        prep_topic = st.text_input("주제", key="prep_topic_2")
        prep_claim = st.text_area("주장 펼치기 (나는~)", key="prep_claim_2")
        prep_reason = st.text_area("근거 제시하기 (그 이유는~)", key="prep_reason_2")
        prep_example = st.text_area("사례 말하기 (예를 들어~)", key="prep_example_2")
        prep_conclusion = st.text_area("결론 요약하기", key="prep_conclusion_2")
        prep_table = [
            ["주제", prep_topic],
            ["주장 펼치기", prep_claim],
            ["근거 제시하기", prep_reason],
            ["사례 말하기", prep_example],
            ["결론 요약하기", prep_conclusion]
        ]
        st.table(pd.DataFrame(prep_table, columns=["구분", "내용"]))

    with tab4:
        st.header("구글시트로 내보내기 안내")
        st.markdown("""
1. 위의 학생별 작성 내용을 모두 입력한 후,  
2. 아래 버튼을 클릭하면 CSV 파일로 다운로드할 수 있습니다.  
3. 다운로드한 CSV 파일을 구글시트에서 불러오면 학생별 결과를 관리할 수 있습니다.
        """)
        if st.button("학생 입력 내용 CSV로 다운로드", key="download_btn_2"):
            csv_df = pd.DataFrame({
                "개념과 사실1": [fact1],
                "개념과 사실2": [fact2],
                "개념적용문장": [concept_blank],
                "나만의개념": [my_concept],
                "나만의문장": [my_sentence],
                "사실적질문1": [factual_q1],
                "사실답1": [factual_a1],
                "사실적질문2": [factual_q2],
                "사실답2": [factual_a2],
                "개념적질문1": [conceptual_q1],
                "개념답1": [conceptual_a1],
                "개념적질문2": [conceptual_q2],
                "개념답2": [conceptual_a2],
                "논쟁적질문1": [debate_q1],
                "논쟁답1": [debate_a1],
                "논쟁적질문2": [debate_q2],
                "논쟁답2": [debate_a2],
                "논쟁선택": [selected_debate],
                "나의생각": [my_opinion],
                "반론": [counter_opinion],
                "PREP_주제": [prep_topic],
                "PREP_주장": [prep_claim],
                "PREP_근거": [prep_reason],
                "PREP_사례": [prep_example],
                "PREP_결론": [prep_conclusion]
            })
            csv = csv_df.to_csv(index=False).encode('utf-8-sig')
            st.download_button(
                label="CSV 다운로드",
                data=csv,
                file_name="concept_exploration_result.csv",
                mime="text/csv"
            )

with tab_main3:
    st.title("3단계 핵심개념 삶에 디자인하기")
    tab1, tab2 = st.tabs(["학생별 작성 내용", "구글시트로 내보내기 안내"])

    with tab1:
        st.header("문제 분석하기")
        st.markdown("""
**핵심 문제 제시**  
우리는 편리함을 위해 많은 플라스틱을 사용하지만, 이것이 기후변화에 악영향을 미치고 있습니다.  
어떻게 하면 플라스틱 소비를 줄이면서도 실생활에서 사용할 수 있는 지속가능한 대안을 디자인할 수 있을까요?

**디자인 산출물**  
개인 맞춤형 에코 키트 디자인

**에코 키트 디자인 (GRASPS)**  
- **Goal (목표)**: 일회용 플라스틱 사용을 줄이기 위해, 사용자 친화적이고 지속 가능한 에코 키트를 디자인  
- **Role (역할)**: 당신은 친환경 제품을 기획하는 지속가능 디자인 스타트업의 디자이너  
- **Audience (대상)**: 환경 문제에 관심은 있지만 일회용품을 자주 사용하는 중학생 또는 일반 소비자  
- **Situation (상황)**: 많은 사람들이 편리함 때문에 일회용품을 계속 사용하고 있어요. 이들의 행동을 변화시킬 수 있는 에코 키트를 디자인해야 합니다. 디자인은 실용적이면서도 개성 있고 친환경적이어야 합니다.  
- **Product (결과물)**: 에코 키트 디자인 포트폴리오를 완성  
        """)
        cause = st.text_area("사람들은 왜 일회용 플라스틱을 계속 사용할까? 플라스틱 생산과 소비가 기후변화에 어떤 방식으로 영향을 줄까?", key="cause_3")
        user_survey = st.text_area("우리 학교에서 친구들은 플라스틱을 어떻게 사용하고 있나?", key="user_survey_3")
        solution_survey = st.text_area("어떤 친환경 제품이 사용자에게 인기가 있고, 디자인은 어떠한가?", key="solution_survey_3")

        st.header("아이디어 개발")
        st.subheader("1) 에코 키트 구성 아이디어")
        st.write("내가 만들고 싶은 에코 키트의 구성품을 아래 표에 작성해보세요. (3~5가지)")
        kit_items = []
        for i in range(1, 6):
            col1, col2, col3 = st.columns([1, 2, 2])
            with col1:
                item = st.text_input(f"구성품 이름 {i}", key=f"kit_item_{i}")
            with col2:
                usage = st.text_input(f"용도 {i}", key=f"kit_usage_{i}")
            with col3:
                reason = st.text_input(f"왜 필요한가요? {i}", key=f"kit_reason_{i}")
            if item or usage or reason:
                kit_items.append([item, usage, reason])
        if kit_items:
            st.table(pd.DataFrame(kit_items, columns=["구성품 이름", "용도", "왜 필요한가요?"]))

        st.subheader("2) 스케치하기")
        sketch_tab1, sketch_tab2 = st.tabs(["전체 키트 외형/파우치 디자인", "세부 구성품 확대 스케치"])
        with sketch_tab1:
            st.write("전체 키트 외형 또는 파우치 디자인 (색상, 재질, 휴대 방식 등도 함께 고려)")
            kit_sketch = st.file_uploader("전체 키트/파우치 스케치 이미지 업로드", type=["png", "jpg", "jpeg"], key="kit_sketch_3")
            if kit_sketch is not None:
                st.image(kit_sketch, caption="전체 키트/파우치 스케치", use_column_width=True)
        with sketch_tab2:
            st.write("세부 구성품 중 하나의 디자인 아이디어를 스케치해보세요. (예: 텀블러 손잡이, 빨대 청소도구, 포장방식 등)")
            detail_sketch = st.file_uploader("세부 구성품 스케치 이미지 업로드", type=["png", "jpg", "jpeg"], key="detail_sketch_3")
            if detail_sketch is not None:
                st.image(detail_sketch, caption="세부 구성품 스케치", use_column_width=True)

        st.subheader("3) 나의 디자인이 특별한 이유")
        special_reason = st.text_area(
            "내가 디자인한 에코 키트는 (               ) 때문에\n다른 키트와 달리 사용자에게 더 편리하고 환경에 도움이 됩니다",
            key="special_reason_3"
        )

    with tab2:
        st.header("구글시트로 내보내기 안내")
        st.markdown("""
1. 위의 학생별 작성 내용을 모두 입력한 후,  
2. 아래 버튼을 클릭하면 CSV 파일로 다운로드할 수 있습니다.  
3. 다운로드한 CSV 파일을 구글시트에서 불러오면 학생별 결과를 관리할 수 있습니다.
        """)
        if st.button("학생 입력 내용 CSV로 다운로드", key="download_btn_3"):
            kit_items_str = "; ".join(
                [f"{item[0]}|{item[1]}|{item[2]}" for item in kit_items if any(item)]
            )
            csv_df = pd.DataFrame({
                "문제원인": [st.session_state.get("cause_3", "")],
                "사용자조사": [st.session_state.get("user_survey_3", "")],
                "기존해결책조사": [st.session_state.get("solution_survey_3", "")],
                "에코키트구성": [kit_items_str],
                "특별한이유": [st.session_state.get("special_reason_3", "")]
            })
            csv = csv_df.to_csv(index=False).encode('utf-8-sig')
            st.download_button(
                label="CSV 다운로드",
                data=csv,
                file_name="life_design_result.csv",
                mime="text/csv"
            )