import requests
import os, sys
from bs4 import BeautifulSoup


data = []


def get_page_number(url):
	resp = requests.get(url)
	html = BeautifulSoup(resp.content, 'html.parser')

	score_total = html.find('div', {'class': 'score_total'})
	lis = score_total.findAll('em')

	return int(lis[1].getText().replace(",",""))


def get_review_data(url):

	global data

	resp = requests.get(url)
	html = BeautifulSoup(resp.content, 'html.parser')
	# print(html)

	score_result = html.find('div', {'class': 'score_result'})
	lis = score_result.findAll('li')

	for l in lis:
		scoreText = l.find('em').getText()
		score = int(scoreText)
		review = l.find('p').getText().strip()

		pair = [score, review]
		data.append(pair)


def save_data(path):

	global data

	f = open(os.path.expanduser(path), 'w')

	for i in data:
		f.write(str(i[0])+ "\t"+i[1]+"\n")

	f.close()

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


def main():

	global data

	# raw_url = "https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=154255&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page="

	# reply_number = get_page_number(raw_url+"1")

	# for i in range(1, int(reply_number/10) + 2):
	# 	get_review_data(raw_url+str(i))
	# 	print(i)

	# save_data("./crawled_result.txt")
	load_data("./crawled_result.txt")


if __name__ =="__main__": 
	main()