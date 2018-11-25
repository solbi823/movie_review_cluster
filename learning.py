# !/usr/bin/env python
# -*- coding: utf-8 -*-

# import torch
# import torch.nn as nn
# from torch.autograd import Variable
# import torch.optim as optim
# import torch.nn.functional as F
# import torchtext

from konlpy.tag import Mecab
import gensim
import os,sys
import numpy as np

data =[]
mecab = Mecab()

analyzedData =[]


def load_data(path):

	global data 

	f = open(os.path.expanduser(path), 'r')

	while True:

		line = f.readline()
		if not line or line=='\n':
			break 
		line_splited = line.split('\t')
		tmp =[int(line_splited[0]),line_splited[1].strip('\n') ]
		data.append(tmp)

	f.close()

def calculate_mean_similarity(model, nouns, words):

	summation = 0
	num = 0
	for n in nouns:
		if n in model.wv.vocab:

			for w in words:
				summation += model.similarity(n, w)
				num +=1

	if num == 0:
		return 0

	return summation / num

def calculate_mean_similarity2(model, nouns, words):

	dim = model["영화"].size

	vec_sum = np.zeros(dim)
	num =0
	for n in nouns:
		if n in model.wv.vocab:
			vec_sum+= model[n]
			num +=1

	sectence_vec = vec_sum / num

	vec_sum = np.zeros(dim)
	num =0
	for w in words:
		if w in model.wv.vocab:
			vec_sum+= model[w]
			num +=1 

	category_vec = vec_sum / num

	return model.similarity(sectence_vec, category_vec)



def main():

	global data


	f = open(os.path.expanduser("new_file.txt"), 'r')

	while True:

		line = f.readline()
		if not line or line=='\n':
			break 
		tmp =mecab.nouns(line)
		analyzedData.append(tmp)

	f.close()


	train_data = analyzedData

	model = gensim.models.Word2Vec(analyzedData, size =100, window = 5, min_count=5, workers = 4, sg =1)
	model.init_sims(replace = True)
	model.save('./train_model')


	# 위키피디아 덤프파일로 모델 구성
	# model = gensim.models.KeyedVectors.load_word2vec_format("./wiki_dmpv_1000_no_taginfo_word2vec_format.bin", binary=True)

	# 크롤링한 테스트 파일 모델구성
	# model = gensim.models.Word2Vec.load('./model')

	# 과제로 받은 영화리뷰 20만개를 페이스북 fast text 를 이용하여 모델 구성(형태소 분석이 부족함)
	# model = KeyedVectors.load_word2vec_format('./movie_model.vec')

	# 요건 과제로 받은 영화리뷰 20만개를 konlpy 형태소 분석후 word2vec 로 모델 구성
	model = gensim.models.Word2Vec.load('./train_model')

	# # 단어 리스트 작성
	# vocab = model.wv.index2word
	# # 전체 단어벡터 추출
	# wordvectors = []
	# for v in vocab:
	# 	wordvectors.append(model.wv[v])
	# wordvectors = np.vstack(wordvectors)

	# print(model.most_similar(positive=["감독", "연출"], topn=20))
	# print(model.most_similar(positive=["스토리", "줄거리", "내용"], topn=20))
	# print(model.most_similar(positive=["음악"], topn=20))
	# print(model.most_similar(positive=["영상미", "색감"], topn=20))
	# print(model.most_similar(positive=["연기력","배우","연기"], topn=20))


	classified_review=[[], [], [], [], []]

	f = open(os.path.expanduser("crawled_result.txt"), 'r')

	while True:

		line = f.readline()
		if not line or line=='\n':
			break 
		line = line.rstrip('\n')
		splited_line = line.split('\t')
		nouns=mecab.nouns(splited_line[1])

		if len(nouns) == 0:
			continue

		value_list = []

		value_list.append( calculate_mean_similarity(model, nouns, ["감독","연출"]))
		value_list.append( calculate_mean_similarity(model, nouns, ["스토리", "내용", "줄거리"]))
		value_list.append( calculate_mean_similarity(model, nouns, ["음악", "노래"]))
		value_list.append( calculate_mean_similarity(model, nouns, ["색감", "영상"]))
		value_list.append( calculate_mean_similarity(model, nouns, ["연기", "배우", "연기력"]))

		for i in range(0, 5):
			if value_list[i] > 0.93:
				classified_review[i].append(splited_line[1])

	f.close()

	i =0
	for c in classified_review:
		print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
		i +=1
		for d in c:
			print(str(i)+"\t" +d)





if __name__ =="__main__": 
	main()


