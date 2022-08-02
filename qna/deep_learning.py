from nltk.tokenize import TreebankWordTokenizer
import numpy as np
from numpy import dot
from numpy.linalg import norm


# 정의할 수 있는 모든 태그 리스트 정의
tag_things = [
    "파이썬", "Python", "PYTHON", "python", 
    "장고", "django", "Django", "DJANGO", 
    "HTML", "html", "Html", 
    "css", "Css", "CSS", 
    "Javascript", "Js", "JS", "JAVASCRIPT", "javascript", "자바스크립트", "자스", 
    "DjangoRestFramework", "DRF", "DJANGORESTFRAMEWORK", 
    "머신러닝", "딥러닝", "machine learning", "ml", "deep learning", "DEEP LEARNING", 
    "DOCKER", "Docker", "docker", "도커"
    ]

# 인자를 받아서 토큰화 해주는 함수
def tokenize_hashtag(hashtag):
    hashtag = TreebankWordTokenizer().tokenize(hashtag)
    while "#" in hashtag:
      hashtag.remove("#")
    return hashtag

# 토큰에 해당하는 리스트 인덱스에 카운트를 넣는 리스트 메이킹 함수
def make_hashtag_array(tokenlist):
  np_hashtag = [0]*len(tag_things)
  for tag in tag_things:
    for target_tag in tokenlist:
      if target_tag == tag:
        tag_index = tag_things.index(tag)
        np_hashtag[tag_index] += 1
  return np_hashtag

# numpy를 활용한 코사인 유사도 함수
def cos_sim(A, B):
  return dot(A, B)/(norm(A)*norm(B))

def cos_similarity(np_target, np_exclude):
    simil_list = []
    for index, np_ex in enumerate(np_exclude):
        result = cos_sim(np_target, np_ex)
        print(f'타겟과 익스클루드{index+1}번째의 유사도 :',result)
        simil_list.append(
            {
                "id" : index+1,
                "similarity": result
                }
        )
        for i in simil_list:
            print(i)
            sort_simil_list = sorted(simil_list , key= lambda x: x['similarity'], reverse=True)[:5]
            for i in sort_simil_list:
                print(i)

# =========================================================================


# 전체 통제 함수
def return_five_recommends(target_hashtag, all_data_hashtag):
    
    # 토크나이저
    target_hashtag = tokenize_hashtag(target_hashtag)
    target_hashtag = make_hashtag_array(target_hashtag)
    target_hashtag = np.array(target_hashtag)
    
    for ex_dict in all_data_hashtag:
        ex_dict['hashtag'] = tokenize_hashtag(ex_dict['hashtag'])
        ex_dict['hashtag'] = make_hashtag_array(ex_dict['hashtag'])
        ex_dict['hashtag'] = np.array(ex_dict['hashtag'])
        ex_dict['hashtag'] = cos_sim(target_hashtag, ex_dict['hashtag'])
    
    sort_result_list = sorted(all_data_hashtag , key= lambda x: x['hashtag'], reverse=True)[:5]
    sort_result_list = [sort_dict['id'] for sort_dict in sort_result_list]
    return sort_result_list
    

  

