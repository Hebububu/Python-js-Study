# 모듈과 패키지
서로 연관된 데이터를 그룹핑하고 이름을 붙인 것 - 리스트, 딕셔너리 
서로 연관된 코드를 그룹핑하고 이름을 붙인 것 - 함수

코딩이란, 정리 정돈이 반이다.
코드가 많아지면 어떻게 하면 좋을까?

서로 연관된 코드를 이어 붙인 다음, 파일에 이름을 붙이면 편하지 않을까?
이것을 '모듈' 이라고 한다. 

코드가 많아질수록 모듈도 많아질 것. 
서로 연관된 모듈을 담은 것을 '패키지' 라고 한다.


## 모듈을 만들고, 그 모듈을 불러와서 쓰는 방법

1. 임포트로 모듈 전체를 가져와서, 모듈명.사용할 함수명 으로 사용하기. 

```py
import modulename
print(modluename.functionname())
```

2. from을 사용하여 함수명을 직접 가져오기.

```py
from directoryname.modulename import functionname
print(functionname())
```

3. from을 사용하여 함수명을 직접 가져오되, 그 함수에 이름을 지어 따로 사용하기

```py
from directoryname.modulename import functionname as functionname1
print(functionname1())
```

## 배운 점 정리
- 코딩이란 정리 정돈이 반이다 (맞는 말인 것 같다.. 잘 정리되고 가독성이 좋은 코드를 적으려고 노력해야 한다.)
- 함수 -> 모듈 -> 패키지 라는 개념에 대해 이해했다. 
- 패키지를 불러오는 방식을 알고는 있었지만, 따로 이름을 지어 활용하는 법은 모르고 있었다. 

- 대충 배웠던 나의 경우 대부분 그냥 from 을 통해서 함수를 하나하나 불러와서 쓰고 있었지만, 임포트로 모듈 전체를 가져와서 모듈명. 함수명으로 사용할 수 있다는 걸 익혔다. 

```py
import modulename
print (modulename.functionname())
``` 

이 부분이 가장 많이 배운 부분인 것 같다. 