# Javascript
- 사용자와 상호작용하고 싶어 하는 욕망에서 등장

## 이번 수업의 최종적인 목표 
- 문법을 배워나가는 수업이 아님,
- 기능을 구현하는 과정에서 문법을 익혀나가는 수업
- 야간모드, 주간모드를 버튼을 통해서 바꾸는 기능을 만들어 볼 것.

- onClick = 속성의 값으로는 Javascript가 들어감.
- styte = 속성의 값으로는 반드시 CSS가 들어감.

- Javascript는 사용자와 상호작용하기 위한 언어이다
- 웹브라우저는 한번 출력되면 스스로를 바꿀 수 없다.
- 그걸 바꾸기 위해서 Javascript를 사용한다.

## Script 태그
- 웹 페이지에 글씨를 출력할 때, document.write를 쓴다. 
- 웹 페이지에 Javascript의 문법임을 알릴 때, Script 태그를 쓴다.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title></title>
    </head>
    <body>
        <h1>Javascript</h1>
        <script>
            document.write(1+1);
        </script>
        <h1>html</h1>
        1+1
    </body>
</html>
```

- 간단한 예시 
- html은 1+1은 영원히 1+1이지만, Javascript는 2 라는 결과를 동적으로 만들어서 출력한다. 

## 이벤트 


```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title></title>
    </head>
    <body>
        <input type="button" value="hi" onclick="alert('hi')">
        <input type="text" onchange="alert('changed')">
        <input type="text" onkeydown="alert('key down')"
    </body>
</html>
```

- 어떠한 이벤트가 일어났을때, Js가 실행되게 하는 것이 onClick, onChange, onKeydown 속성이다. 
- 웹브라우저는 어떠한 이벤트들을 정의해두고 있다. 
- 그것을 이용해서 사용자와 상호작용할 수 있는 웹페이지를 만들 수 있다. 

## 콘솔
- 콘솔로도 이미 작성되어있는 웹페이지를 제어할 수 있다. 
- 나의 현실의 문제를 가볍게 가볍게 해결할 수 있는 방법을 찾아보자. 
- 콘솔을 통해서 Js를 실행하면 Js가 실행된다는걸 기억하자. 

## 데이터타입

