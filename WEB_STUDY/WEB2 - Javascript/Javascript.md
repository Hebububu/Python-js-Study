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

## 데이터타입 (자료형)

- 숫자형 integer 
- 문자형 string 

- 숫자형은 숫자 그대로, 문자형도 마찬가지로 '',  ""로 묶어서 표현한다. 

```js
"Hello world".toUpperCase // 대문자로 바꾸기
"Hello world".length // 길이가 얼마나 되는지?
"Hello world".indexOf('o') // 몇번째에 어떤 숫자가 있는지
```

- 문자열 기능은 다양하게 있다. 찾아보며 사용해보자.
- 지금 문법은 완벽하게 이해하지 않아도 된다, 우선은 이런 기능이 있고, 문법은 찬찬히 익숙해지면 된다. 

## 변수와 대입 연산자

- 변수, 바뀔 수 있는 어떤 값..

- 대입연산자 '=' 좌항의 값에 우항의 값을 대입한다. 

```js
var name = 'hebu';
alert("어쩌구저쩌구머시기저시기" + name + "어쩌구저쩌구머시기저시기.." + name)
```

- 바뀔 수 있는 값에 변수를 사용하면 유용하다.
- 변수를 사용할 때는 가급적 var을 사용하는게 좋다. (variable)


## 제어할 태그 선택하기 

```html
<!doctype html>
<html>
<head>
  <title>WEB1 - JavaScript</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.html">WEB</a></h1>
  <input type="button" value ="Night" onclick="
  document.querySelector('body').style.backgroundColor = 'black';
  document.querySelector('body').style.color = 'white';
  ">
  <input type="button" value ="Day" onclick="
  document.querySelector('body').style.backgroundColor = 'white';
  document.querySelector('body').style.color = 'black';
  ">
  <ol>
    <li><a href="1.html">HTML</a></li>
    <li><a href="2.html">CSS</a></li>
    <li><a href="3.html">JavaScript</a></li>
  </ol>
  <h2>JavaScript</h2>
  <p>
    JavaScript (/ˈdʒɑːvəˌskrɪpt/[6]), often abbreviated as JS, is a high-level, dynamic, weakly typed, prototype-based, multi-paradigm, and interpreted programming language. Alongside HTML and CSS, JavaScript is one of the three core technologies of World Wide Web content production. It is used to make webpages interactive and provide online programs, including video games. The majority of websites employ it, and all modern web browsers support it without the need for plug-ins by means of a built-in JavaScript engine. Each of the many JavaScript engines represent a different implementation of JavaScript, all based on the ECMAScript specification, with some engines not supporting the spec fully, and with many engines supporting additional features beyond ECMA.
  </p>
</body>
</html>
```

- document.querySelector('태그명') 을 통해서 body 태그를 선택했다.
- .style 을 통해서 css 변환을 지정했다.
- .backgroundColor = 'black'을 통해서 검은색으로 바꾸었다. 

- onclick -> body 태그 선택 -> css 스타일을 변경 -> 나이트모드 / 다크모드 변환 

## 자바스크립트는 무엇일까? 돌아보자. 
- javascript는 컴퓨터 언어이면서 동시에 프로그래밍 언어라고 불리운다.
- 프로그램이라는 말의 중심에는 순서라는 말이 중점적으로 강조되어 있다. 
- 그 순서를 만드는 사람을 프로그래머 라고 함.

- 필요에 따라 순서에 따라 여러 기능을 조작하게 하는 것 
- 시간에 순서에 따라 순차적으로 실행되어야 하는 것을 컴퓨터 프로그래밍 언어의 문법에 맞게 언어로 작성한 것. 
