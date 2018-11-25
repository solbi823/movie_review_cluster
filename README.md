# Movie Review Cluster Test

- 네이버 영화 댓글 크롤링하여 활용
- Konlpy를 사용한 한글 형태소 분석. 현재는 명사만 활용 중
- Word2Vec 를 사용하여 워드 임베딩. 여러가지 training data로 실험중
위키피디아, 나무위키 덤프 텍스트는 댓글에서 실제 사용하는 언어를 대표하지 못하는 듯하다.


# 방법..?

- 워드 벡터 similarity 단순 평균 : 주어진 키워드와의 유사성
키워드 선정이 중요함. 키워드가 해당 주제를 전부 대표하지 못함. 
- K means clustering
- RNN

