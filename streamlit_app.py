import streamlit as tf
import pandas as pd
import streamlit as st

# 웹 페이지 제목
st.title("💯 과목별 성적 산출 프로그램")

# 과목 데이터 정의
subjects = ["국어", "영어", "수학", "과학"]
scores = {}

st.subheader("📝 과목별 점수 입력")

# 각 과목의 점수를 입력받는 위젯 생성
for subject in subjects:
    scores[subject] = st.number_input(
        f"{subject} 점수 입력:", min_value=0, max_value=100, value=80
    )

# 성적 산출 버튼
if st.button("성적 산출하기", type="primary"):
    results = []

    # 기존 핵심 로직 그대로 유지하며 반복문 수행
    for subject in subjects:
        score = scores[subject]

        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        else:
            grade = "C"

        # 결과를 리스트에 담기
        results.append({"과목": subject, "점수": score, "등급": grade})

    # 결과를 데이터프레임으로 변환 후 웹 화면에 출력
    df_results = pd.DataFrame(results)

    st.success("🎉 성적 산출이 완료되었습니다!")
    st.dataframe(df_results, use_container_width=True, hide_index=True)