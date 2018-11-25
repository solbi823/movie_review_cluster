# Movie Review Cluster Test

- 네이버 영화 댓글 크롤링하여 활용
- Konlpy를 사용한 한글 형태소 분석. 현재는 명사만 활용 중
- Word2Vec 를 사용하여 워드 임베딩. 위키피디아 덤프 파일 이용


# 방법..?

- 테스트 문장의 명사 word vector와 category keyword 간의 similarity 단순 평균

키워드 선정이 중요함. 키워드가 해당 주제를 전부 대표하지 못함. 

관련 있는 내용을 얘기 해도 단어수가 많으면 similarity 가 떨어지는 문제가 있다. 

결과 -> result_with_similarity_mean.text

- 워드 벡터와 카테고리 키워드 가운데 가장 큰 similarity

단순 search 와 비슷한 결과..
-> result_with_most_similar.text

- K means clustering
- RNN

