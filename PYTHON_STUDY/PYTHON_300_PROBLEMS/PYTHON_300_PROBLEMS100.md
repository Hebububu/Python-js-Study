# 파이썬 300제 시작.
- 따로 파일을 만들지는 않고, 문제를 풀고 풀이를 보고 진행하자. 
- 어려운 문제의 경우 파일을 만들어서 실제로 실행시켜볼 것. 


# 파이썬 시작하기 문제

## 1번 print 기초
```py
print("Hello World")
```

## 2번 print 기초
```py
print("Mary's cosmetics")
```

- 작은따음표가 들어가 있음으로 큰따음표로 처리.

## 3번 print 기초

```py
print('신씨가 소리질렀다. "도둑이야".')
```

## 4번 문제 print 기초
```py
print("C:\\Windows")
```

- 백슬래시의 경우 두번 적어야 제대로 문자열로 출력된다. 

## 5번 문제
```py
print("안녕하세요.\n만나서\t\t반갑습니다.")
```

- 백슬래시n (\n)은 줄바꿈, 백슬래시t (\t)의 경우 탭이 된다. 

## 6번 문제 print 여러 데이터 출력

```py
print("오늘은", "일요일")
```

- 여러 값을 출력할때는 쉼표로 구분하여 출력한다. 

## 7번 문제 print 기초

```py
print("naver","kakao","sk","samsung", sep=";")
```

- sep= 라는 옵션을 사용해서 쉼표 사이사이에 넣을 걸 지정할 수 있다. 

## 8번 문제 print 기초

```py
print("naver","kakao","sk","samsung", sep="/")
```

- 똑같이 sep= 옵션을 사용한다. 

## 9번 문제 print 줄바꿈
```py
print("first", end=""); print("second")
```

- 줄바꿈 없이 출력하는 것. end의 기본값이 \n으로 되어있는걸 공란으로 바꾸면 된다. 

## 10번 문제 연산 결과 출력
```py
print(5/3)
```

- 5/3의 결과를 출력하기

# 파이썬 변수

## 11번 문제 변수 사용하기

```py
삼성전자 = 50000
총평가금액 = 삼성전자 * 10
print(총평가금액)
```

- 변수애 값을 바인딩해보기기

## 12번 문제 변수 사용하기

```py
시가총액 = 298000000000000
현재가 = 50000
PER = 15.79
print("시가총액 :", int(시가총액))
print("현재가 :", int(현재가))
print("PER: ", float(PER))
```

- 변수의 type을 정의하는 부분

## 13번 문제 문자열 출력

```py
s = "hello"
t = "python"

print(f"{s}! {t}")
```

## 14번 문제 파이썬을 이용한 값 계산

```py
print(2 + 2 * 3)
```

- 8의 값이 나온다

## 15번 문제 type 함수

```py
a = 128
print(type(a))
<class 'int'>

a = "132" #의 타입 값은?
> str 이다. 
```

- 따옴표로 감싸진 숫자는 문자열. 

## 16번 문제 문자열을 정수로 변환

```py
num_str = "720"
num_int = int(num_str)
print(num_int+1, type(num_int))
```

- int() 에 넣어서 바꿀 수 있다. 

## 17번 문제 정수를 문자열 100으로 변환

```py
num = 100
num_str = str(num)
print(num_str, type(num_str))
```

- str()에 넣어서 바꿀 수 있다. 

## 18번 문제 문자열을 정수로 변환

```py
string = 15.79
float_string = float(string)
print(float_string, type(float_string))
```

- float()에 넣어서 바꿀 수 있다. 

## 19번 문제 문자열을 정수로 변환

```py
year = "2020"
year_int = int(year)
print(year_int)
print(year_int-1)
print(year_int-2)
```

- int 로 변환 후 연산자로 계산 

## 20번 문제 파이썬 계산

```py
monthly_price = 48584
total_month = 36
total_price = monthly_price * total_month
print(total_price)
```

# 파이썬 문자열

## 21번 문제 문자열 인덱싱

```py
letters = 'python'
print(letters[0],letters[2])
```

- 변수명[0] 등으로 인덱싱을 할 수 있다. 0부터 시작하는 것을 기억하자. 

## 22번 문제 문자열 슬라이싱

```py
license_plate = "24가 2210"
print(license_plate[4:8])
```

- 변수명[0:0] 등으로 슬라이싱을 할 수 있다. 0부터 시작하는 것을 기억하자.

## 23번 문제 문자열 인덱싱

```py
string = "홀짝홀짝홀짝"
print(string[::2])
```

- 처음 보는 기능이라 이해가 잘 안됐음. 
- 슬라이싱은 **start:stop:step** 순서로 진행된다고 함.
- start는 시작 인덱스 (생략하면 0부터 시작함)
- stop은 끝 인덱스 (생략하면 끝까지 진행함)
- step은 몇칸씩 건너뛰면서 가져올지 (여기서는 2)

- 따라서 값은 처음부터 끝까지 가져오되, 두칸씩 건너뛰면서 가져오기 떄문에
> 홀홀홀
- 이라는 결과값이 나오게 된다.

## 24번 문제 문자열 인덱싱

```py
string = "PYTHON"
print(string[::-1])
```

- 이 역시도 답안을 보고 알았다. 
- 슬라이싱에 음수값을 넣으면 역순으로 가져오게 됨. -1 값을 넣었기 때문에 맨 뒤에서부터 가져온다. 

## 25번 문제 문자열 치환

```py
phone_number = "010-1234-5678"
phone_number1 = phone_number.replace("-"," ")
print(phone_number1)
```

- 답안을 보고 알았다.
- 그냥 인덱싱으로 010 부분이랑 1234 부분이랑 5678을 잘라서 하려고 했음 (바보..)
- replace() 함수를 사용해서 하이폰을 공백으로 교체하면 편하게 할 수 있다. 

## 26번 문제 문자열 다루기

```py
phone_number = "010-1234-5678"
phone_number1 = phone_number.replace("-","")
print(phone_number1)
```

- 같은 원리로 replace() 함수를 사용하면 된다.

## 27번 문제 문자열 다루기 (kr 부분 추출하기기)

```py
url = "http://sharebook.kr"
print(url[17:19])
```

- 내가 푼 답변

```py
url = "http://sharebook.kr"
url_split = url.split('.')
print(url_split[-1])
```

- 실제 답안에서는 split() 함수를 사용했다.
- 왜 -1을 사용하는지 잘 모르겠어서 GPT에게 물어봤다.

```md
왜 -1을 사용하는지?
split() 함수는 문자열을 나누면 리스트로 반환되는데, 각 부분이 점(.)을 기준으로 나눠지므로 마지막 부분은 'kr'가 됩니다.
[-1]은 이 리스트에서 가장 마지막 원소를 가져오는 방법입니다. 그래서 kr이 출력됩니다.
```

- 마지막 원소를 가져올때 -1 을 사용하는는걸 알았다. 

## 28번 문자열은 immutable

```py
lang = 'python'
lang[0] = "P"
print(lang)
```

- 문자열은 수정할 수 없기 때문에 (assignment 메서드를 지원하지 않는다.) 결과값은 그냥 python이 나오게 된다.. 

## 29번 replace 메서드

```py
string = 'abcdfe2a354a32a'
edited_string = string.replace('a', 'A')
print(edited_string)
```

- replace() 메서드를 사용하는 간단한 변경 문제였다.

## 30번 replace 메서드

```py
string = 'abcd'
string.replace('b','B')
print(string)
> abcd
```

- 문자열은 변경 불가능한 데이터 타입이다.

```py
string = 'abcd'
new_string = string.replace('b','B')
print(new_string)
> aBcd
```

- 만약 바꾸고 싶다면 이런 방식을 사용해야 할 것. 

## 31번 문자열 합치기

```py
a = "3"
b = "4"
print(a + b)

> 34
```

- 문자열은 더하면 문자열 값 그대로 더해짐으로 결과값은 34가 나온다.

## 32번 문자열 곱하기

```py
print("Hi" * 3)

> HiHiHi
```

- 문자열은 곱하면 문자열 값 그대로 곱해짐으로 결과값이 저렇게 나온다.

## 33번 문자열 곱하기

```py
print("-" * 80)
```

- 문자열을 80번 곱하면 되는 간단한 문제.

## 34번 문자열 곱하기

```py
t1 = 'python'
t2 = 'java'
t3 = t1 + ' ' + t2 + ' '

print(t3*4)
```

- 문자열을 서로 더해서 곱하면 되는 간단한 문제 

## 35번 문자열 출력

```py
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13

my_str = "이름: %s 나이: %d"
print(my_str % (name1, age1))
print(my_str % (name2, age2))
```

- % 포맷팅은 실제론 처음 써봤다. 구글에 검색해서 알아봤음
- %s 문자열, %d 정수, %f 실수 

```py
print("이름: %s 나이 %d" % (name1, age1))
```

- 이렇게도 쓸 수 있다. 

## 36번 문자열 출력

```py
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13

print("이름: {} 나이: {}".format(name1, age1))
print("이름: {} 나이: {}".format(name2, age2))
```

- format() 메서드를 이용한 방식. 
- 이도 처음 써봐서 구글에 검색했다.

## 37번 문자열 출력

```py
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13

print(f"이름: {name1} 나이: {age1}")
print(f"이름: {name2} 나이: {age2}")
```

- f-string을 이용한 방식. 
- 이전에 사용해 본 적 있는 방식이라 익숙하다. 간단한 문제. 

## 38번 컴마 제거하기

```py
상장주식수 = "5,969,782,550"
non_comma = 상장주식수.replace(',','')
type_change = int(non_comma)
print(type_change, type(type_change))
```

- 컴마를 제거하는 부분까지는 이해했는데.. 결과값의 숫자가 붙어서 나온다
- 숫자를 따로 분리하는 부분까지는 설명이 안 되어 있다. 문제의 의도인가?

## 39번 문자열 슬라이싱

```py
분기 = "2020/03(E) (IFRS연결)"
print(분기.split('(')[0])
```

- 나는 split() 메소드를 사용해서 풀었다. 
- 정답은 print(분기[:7])을 사용하고 있었다. 

## 40번 strip 메서드

```py
data = "      삼성전자      "
cleared_data = data.strip()
print(cleared_data)
```

- strip() 메서드도 처음 써 본다. 
- 원하는 문자열과 공백을 전부 제거하는 메소드. 
- 다른 활용방법도 있다. 

## 41번 upper 메서드

```py
ticker = "btc_krw"
print(ticker.upper())
```

- upper() 메소드를 이용해 문자열을 대문자로 만들기.

## 42번 lower 메서드

```py
ticker = "BTC_KRW"
print(ticker.lower())
```

- lower() 메소드를 이용해 문자열을 소문자로 만들기.

## 43번 capitalize 메소드

```py
string = "hello"
print(string.capitalize())
```

- capitalize() 메소드. 첫 글자를 대문자로 바꾸는 함수이다. 

## 44번 endswith 메소드

```py
file_name = "보고서.xlsx"
print(file_name.endswith('xlsx'))
```

- endswith() 메소드. 무엇으로 끝나는지를 Boolean으로 알려준다. 

## 45번 endswith 메소드

```py
file_name = "보고서.xlsx"
print(file_name.endswith(('xlsx','xls')))
```

- xlsx이나 xls로 끝나는지 확인하라길래 무슨 소린가 했는데 그냥 2개 넣으면 되는거였다.
- 타입 에러가 났었는데, 두개 넣고 괄호를 안넣었다. ㅋㅋ

## 46번 startswith 메소드

```py
file_name = "2020_보고서.xlsx"
print(file_name.startswith("2020"))
```

- startswith() 메소드

## 47번 split 메소드

```py
a = "hello world"
split_a = a.split(" ")
print(split_a)
```

- split() 메소드

## 48번 split 메소드

```py
ticker = "btc_krw"
split_ticker = ticker.split("_")
print(split_ticker)
```

- split() 메소드

## 49번 split 메소드

```py
date = "2020-05-01"
split_date = date.split("-")
print(split_date)
```

## 50번 rstrip 메소드

```py
data = "035043       "
strip_data = data.rstrip()
print(strip_data)
```

- rstrip() 메소드. 스트립이랑 거의 같다. 오른쪽이란거 빼고. 

# 파이썬 리스트

## 51번 리스트 생성

```py
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
print(movie_rank)
```

- 기본적인 파이썬 리스트 만드는 방법. 

## 52번 리스트에 원소 추가

```py
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
movie_rank.append("배트맨")
print(movie_rank)
```

- append() 메소드를 이용하여 리스트에 원소를 추가할 수 있다. 

## 53번 

```py
movie_rank = ["닥터 스트레인지", "스플릿", "럭키", "배트맨"]
movie_rank.insert(1, "슈퍼맨")
print(movie_rank)
```

- insert() 메소드를 사용하면 특정 위치에 값을 끼워넣을 수 있다.
- insert(인덱스, 원소)

## 54번 

```py
movie_rank = ["닥터 스트레인지", "슈퍼맨", "스플릿", "럭키", "배트맨"]
movie_rank.remove("럭키")
print(movie_rank)
```

- 답에선 del 키워드를 사용했는데, 난 그냥 remove() 메소드를 사용했다. 

## 55번 

```py
movie_rank = ["닥터 스트레인지", "슈퍼맨", "스플릿", "럭키", "배트맨"]
movie_rank.remove("스플릿")
movie_rank.remove("배트맨")
print(movie_rank)
```

- 두번 지우면 됨. 

## 56번 

```py
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python","Go","C#"]

combined_lang = lang1 + lang2
print(combined_lang)
```

- 리스트끼리 더하기.

## 57번

```py
nums = [1, 2, 3, 4, 5, 6, 7]
print(f"max: {max(nums)}")
print(f"min: {min(nums)}")
```

- max()와 min() 메서드로 최솟값과 최댓값을 출력하기. 

## 58번

```py
nums = [1, 2, 3, 4, 5]
total = 0

for num in nums:
    total += num

print(total)
```

- 나는 for 문을 쓰긴 했다. 정답에서는 그냥 sum()을 썼다

```py
nums = [1, 2, 3, 4, 5]
print(sum(nums))
```

## 59번

```py
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print(len(cook))
```

## 60번

```py
nums = [1, 2, 3, 4, 5]
import statistics 
print(statistics.mean(nums))
```

- statistics 모듈을 임포트해서 mean() 메소드로 풀었다. 
- 정답에서는 sum() / len() 으로 풀더라. 

```py
nums = [1, 2, 3, 4, 5]
avg = sum(nums) / len(nums)
print(avg)
```

## 61번

```py
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])
```

- 슬라이싱을 통한 가격 리스트 값 구하기

## 62번

```py
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])
```

- 슬라이싱을 통한 홀수만 출력하기


## 63번 

```py
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[1::2])
```

- 슬라이싱을 통한 짝수만 출력하기

## 64번 

```py
nums = [1, 2, 3, 4, 5]
print(nums[::-1])
```

- 슬라이싱을 통한 역순 출력하기

## 65번

```py
interest = ["삼성전자", "LG전자", "Naver"]
print(interest[0],interest[2])
```

- 인덱싱으로 특정 데이터 출력하기

## 66번 join 매소소드

```py
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
result = " ".join(interest)
print(result)
```

- join 메서드. 매개변수로 들어온 리스트에 있는 요소 하나하나를 합쳐서 하나의 문자열로 바꾸어 반환하는 함수. 
- 구분자.join(매개변수) 식으로 사용이 가능하다. 

## 67번 join 메소드

```py
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("/".join(interest))
```

- 구분자를 바꿔서 사용해보기. 

## 68번 join 메소드

```py
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("\n".join(interest))
```

- \n 줄바꿈 

## 69번 문자열 split 메소드

```py
string = "삼성전자/LG전자/Naver"
interest = string.split("/")
print(interest)
```

- split() 메소드 사용해보기. 

## 70번 리스트 정렬

```py
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data)
```

- sort() 메소드 사용하기.

# 파이썬 튜플

## 71번 

```py
my_variable = ()
print(type(my_variable))
```

- 튜플을 정의하는 기호는 괄호. 

## 72번

```py
movie_rank = ("닥터 스트레인지", "스플릿", "럭키")
```

- 튜플 만들어보기 

## 73번 

```py
num = (1,)
```

- 하나의 데이터만 저장되는 경우, 쉼표로 튜플임을 알려주어야 함. 

## 74번

```py
>> t = (1, 2, 3)
>> t[0] = 'a'
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    t[0] = 'a'
TypeError: 'tuple' object does not support item assignment
```

- 오류가 일어나는 이유
- 튜플은 원소의 값을 변경할 수 없다. 

## 75번

```py
t = 1, 2, 3, 4
```

- 괄호 없이도 튜플은 동작한다. 

## 76번

```py
t = ('a', 'b', 'c')
t = ('A', 'b', 'c')
```

- 튜플은 값이 변경될 수 없음으로 변수를 새로 선언해야 한다. 

## 77번

```py
interest = ('삼성전자', 'LG전자', 'SK Hynix')
data = list(interest)
```

- 튜플을 리스트 자료형으로 변경하기. 

## 78번

```py
interest = ["삼성전자", "LG전자", "SK Hynix"]
data = tuple(interest)
```

- 리스트를 튜플 자료형으로 변경하기.

## 79번 튜플 언팩킹

```py
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)
```

- 튜플의 왼쪽에 각 튜플의 원소를 바인딩할 변수를 적어주면 각 변수가 튜플의 원소를 바인딩하게 된다.
- 이를 튜플 언팩킹이라고 한다. 하나씩 인덱싱 할 필요가 없어서 편하다. 

## 80번 range 함수

```py
numbers = tuple(range(2,100,2))
print(numbers)
```

- range() 함수도 마찬가지로 start, stop, step 을 인자로 받는다. 
- 2부터 시작해서 100에서 멈추고 2마다 건너뛴다. 로 짝수만 출력하게 했다. 

# 파이썬 딕셔너리 

## 81번 별 표현식

```py
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, b, c = tuple(scores)
print(a, b, c)
```

- 위에서 배웠던 튜플 언팩킹으로 왼쪽 8개의 값을 valid_score 리스트에 담았다. 

```py
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, _, _= scores
print(valid_score)
```

- 정답에선 이렇게 했던데, _ 변수가 궁금해서 알아봤다.
- _ 변수도 실제로 값을 저장하고 있지만, 관례적으로 이 값은 사용하지 않겠다는 뜻의 변수로 사용된다고 한다. 
- 굳이 튜플로 변환하지 않아도 됐었다.. ㅋㅋㅋ

## 82번 

```py
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
_, _, *valid_score = scores
print(valid_score)
```

- 오른쪽 8개 값을 언팩킹하기

## 83번

```py
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
_, *valid_score, _ = scores
print(valid_score)
```

- 마찬가지로 중간 값을 언팩킹하기 

## 84번

```py
temp = {}
```

- 빈 딕셔너리 만들기. 기본

## 85번

```py
icecream = {
  "메로나" : 1000,
  "폴라포" : 1200,
  "빵빠레" : 1800
}
```

- 딕셔너리 만들기

## 86번

```py
icecream = {
  "메로나" : 1000,
  "폴라포" : 1200,
  "빵빠레" : 1800
}
icecream['죠스바'] = 1200
icecream['월드콘'] = 1500

print(icecream)
```

- 딕셔너리에서는 append나 inser같은 메서드를 지원하지 않는다. 
- 따라서 딕셔너리에 데이터를 삽입하기 위해서는 명시적으로 key - value 쌍을 넣어서 데이터를 삽입하는 방법을 사용한다. 

## 87번

```py
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}

print(f"메로나 가격: {ice['메로나']}")
```

- 딕셔너리를 인덱싱할때는, 인덱스로 key를 이용하여 인덱싱한다. 

## 88번

```py
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}

ice['메로나'] = 1300

print(f"메로나 가격: {ice['메로나']}")
```

- 값 수정도 마찬가지로 인덱스로 key를 이용하면 된다. 

## 89번 

```py
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}

del ice['메로나']

print(ice)
```

- 딕셔너리의 key - value 쌍을 삭제할때는 del 명령어를 사용하면 된다. 

## 90번

```py
>> icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
>> icecream['누가바']
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    icecream['누가바']
KeyError: '누가바'
```

- 오류가 발생한 원인..?
- 누가바라는 Key가 존재하지 않기 때문.

## 91번 

```py
inventory = {
  "메로나" : [300, 20],
  "비비빅" : [400, 3],
  "죠스바" : [250, 100]
}
```

- 딕셔너리 안에 리스트를 넣을 수 있다. 

## 92번 딕셔너리 인덱싱 

```py
inventory = {
  "메로나" : [300, 20],
  "비비빅" : [400, 3],
  "죠스바" : [250, 100]
}

print(f"{inventory['메로나'][0]} 원")
```

## 93번 딕셔너리 인덱싱

```py
inventory = {
  "메로나" : [300, 20],
  "비비빅" : [400, 3],
  "죠스바" : [250, 100]
}

print(f"{inventory['메로나'][1]} 개")
```

## 94번 딕셔너리 추가

```py
inventory = {
  "메로나" : [300, 20],
  "비비빅" : [400, 3],
  "죠스바" : [250, 100]
}
inventory['월드콘'] = [500,7]
print(inventory)
```

- 뭐 똑같다. key - value 로 넣되 value가 리스트 타입으로 바뀌었을 뿐.

## 95번 딕셔너리 keys() 메소드

```py
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
ice = list(icecream.keys())
print(ice)
```

- 좀 헤맸다. list() 로 감싸면 되는걸 굳이 빈 리스트를 만들어서 append 하려고 함 ㅋㅋㅋ

## 96번 딕셔너리 values() 메소드

```py
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
ice = list(icecream.values())
print(ice)
```

## 97번 딕셔너리 values() 메소드

```py
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
ice = list(icecream.values())
print(sum(ice))
```

## 98번 딕셔너리 update 메서드

```py
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수':2700, '아맛나':1000}
icecream.update(new_product)
print(icecream)
```

## 99번 zip과 dict

```py
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
result = dict(zip(keys, vals))
print(result)
```

- zip() 은 여러 개의 순서가 있는 자료형을 쌍으로 묶어주는 함수. 1대 1로 대응되는 튜플 쌍을 만들어준다.
- dict() 는 딕셔너리를 만들어주는 함수다. 튜플 쌍이 들어 있으면 자동으로 key - value 구조로 바꿔줌. 

- zip 으로 만든 튜플 쌍을 dict로 딕셔너리로 만드는 것. 

## 100번 zip과 dict

```py
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(date,close_price))
print(close_table)
```
