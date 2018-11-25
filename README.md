# Movie Review Cluster Test

- 네이버 영화 댓글 크롤링하여 활용
- Konlpy를 사용한 한글 형태소 분석. 현재는 명사만 활용 중
- Word2Vec 를 사용하여 워드 임베딩. 위키피디아 덤프 파일 이용


# 방법..?

- 워드 벡터 similarity 단순 평균 : 주어진 키워드와의 유사성
키워드 선정이 중요함. 키워드가 해당 주제를 전부 대표하지 못함. 
관련 있는 내용을 얘기 해도 단어수가 많으면 similarity 가 떨어짐:
- K means clustering
- RNN

