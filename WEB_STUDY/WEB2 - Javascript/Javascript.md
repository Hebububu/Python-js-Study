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

- 조건에 따라서 다른 기능을 실행하거나, 반복되서 실행되는 프로그램도 만들고 싶어짐.
- 복잡하게 된 순서를 깔끔하게 정리정돈 하는 기능도 만들고 싶어짐. 

## Javascrpt의 조건문

- 토글로 구현해볼까? (문제점을 찾고, 해결하자)

### Boolean 데이터 타입
- 다른 언어와 마찬가지로 True, False로 구분된다.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title></title>
    </head>
    <body>
        <h1>Comparison operators & Boolean</h1>
        <h2>===</h2>
        <h3>1===1</h3>
        <script>
            document.write(1===1); // 비교 연산자, 동등함을 비교.
        </script>

        <h3>1===2</h3>
        <script>
            document.write(1===2);
        </script>

        <h3>1&lt;2</h3>
        <script>
            document.write(1<2); // 비교 연산자, 크고 작음을 비교함.
        </script>

        <h3>1&lt;1</h3>
        <script>
            document.write(1<1);
        </script>
    </body>
</html>
```

- Boolean 타입에 대해 간단히 예시를 통해 알아보았다. 

## 조건문의 기본 형식

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        <h1>Conditional statements</h1>
        <h2>Program</h2>
        <script>
            document.write("1<br>");
            document.write("2<br>");
            document.write("3<br>");
            document.write("4<br>");
            document.write("5<br>");
        </script>
        <h2>if-true</h2>
        <script>
            if(true){ // Boolean의 값이 true
                document.write("1<br>");
            }
            else {
                document.write("2<br>");
            }
            document.write("3<br>");
            document.write("4<br>");
            document.write("5<br>");
        </script>

        <h2>if-false</h2>
        <script>
            if(false){ // Boolean의 값이 False
                document.write("1<br>");
            }
            else {
                document.write("2<br>");
            }
            document.write("3<br>");
            document.write("4<br>");
            document.write("5<br>");
        </script>
    </body>
</html>
```

- 조건문의 기본 형식에 대해서 알아보았다.

```html
<script>
  if('Boolean 값'){
    'javascript 내용'
  }
  else{
    'javascript 내용'
  }
</script>
```

- 이러한 형식으로 사용되며, 'Boolean 값'이 True 인 경우 if가 실행되고, False인 경우, else를 실행하게끔 되어있다. 

```html
  <input id="night_day" type="button" value="Night" onClick="
  if (document.querySelector('#night_day').value === 'Night'){
    document.querySelector('body').style.backgroundColor= 'black';
    document.querySelector('body').style.color = 'white';
    document.querySelector('#night_day').value = 'Day'
  } else {
    document.querySelector('body').style.backgroundColor= 'white';
    document.querySelector('body').style.color= 'black';
    document.querySelector('#night_day').value = 'Night'
  }
  ">
```

1. input 의 id값이 night_day 인 요소를 querySelector로 찾기. 
2. 그 value가 Night인 경우 나이트 모드를 활성화하고, value를 Day로 대체하기.

- Day일때는 else 문이 작동하여 반대로 데이모드가 작동된다.
- 신기하고 재밌다!

## 리팩토링이란?

- 좀 더 개선한다. 로 이해하면 좋을 것 같은 용어 
- 비효율적인 코드, 반복적인 코드를 아주 효율적으로 만들고, 가독성을 높이면서 유지보수 하기 편하게 하는 것!

```html
  <input type="button" value ="Night" onClick="
  if (this.value === 'Night'){
    document.querySelector('body').style.backgroundColor= 'black';
    document.querySelector('body').style.color = 'white';
    this.value = 'Day'
  } else {
    document.querySelector('body').style.backgroundColor= 'white';
    document.querySelector('body').style.color= 'black';
    this.value = 'Night'
  }
  ">
```

- 자기 자신, 스스로를 가르키고 있는 쿼리셀렉터를 지우고 'this'로 대체함으로써 가독성이 좋아지고, 재사용성 또한 좋아졌다.

```html
  <input type="button" value ="Night" onClick="
  var target = document.querySelector('body')
  if (this.value === 'Night'){
    target.style.backgroundColor= 'black';
    target.style.color = 'white';
    this.value = 'Day'
  } else {
    target.style.backgroundColor= 'white';
    target.style.color= 'black';
    this.value = 'Night'
  }
  ">
```

- var target = document.querySelector('body') 변수를 선언함으로써, 반복된 코드를 줄이고 가독성이 더 좋아졌다!


## 반복문을 위한 배열

```html
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
        <title></title>
    </head>
    <body>
        <h1>Array</h1>
        <h2>Syntax</h2>
        <script>
            var names = ["Hebu", "Heaven"];
        </script>

        <h2>get</h2>
        <script>
            document.write(names[0]);
            document.write(names[1]);
        </script>

        <h2>add</h2>
        <script>
            names.push('Heavekk')
        </script>

        <h2>count</h2>
        <script>
            document.write(names.length);
        </script>
        
    </body>
</html>
```

- 데이터들을 담기 위한 수납 상자라고 생각하자.
- 변수에 담고 변수명[0] 등을 이용해서 사용할 수 있다.
- .push를 통해 배열에 새로운 값을 추가할 수 있다.
- .length를 통해 배열의 길이를 찾을 수 있다. 

## 반복문 while 기초

```html
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
    </head>
    <body>
        <h1>Loop</h1>
        <ul>
            <script>
                document.write('<li>1</li>');
                var i = 0;
                while(i < 3){
                    document.write('<li>2</li>');
                    document.write('<li>3</li>');
                    i = i + 1;
                }
                document.write('<li>4</li>');
            </script>
        </ul>
    </body>
</html>
```

- while 반복문
- i라는 변수를 0으로 선언, while(i < 3) 일때, 리스트 2,3 을 반복 작성
- 완료될때 i의 값에 +1 을 더함 
- 최종적으로 i가 3이 되면 반복문이 종료됨. 

## 배열과 반복문
- 배열은 예쁘게 데이터를 차곡차곡 담는 것
- 반복문은 그 데이터를 차곡차곡 꺼내서 사용하는 것

```html
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
    </head>
    <body>
        <h1>Loop & Array</h1>
        <script>
            var coworkers= ['Hebu', 'Heaven', 'HeaveKK', 'Hebububu']
        </script>
        <h2>Co workers</h2>
        <ul>
            <script>
                var i = 0;
                while(i < coworkers.length){
                    document.write('<li>'+coworkers[i]+'</li>');
                    i = i + 1;
                }
            </script>
        </ul>
    </body>
</html>
```

- while(i < coworkers.length)에 집중..
- 변수 i 는 인덱스 순서와 같기 때문에 사용하기 편하구나.

## 배열과 반복문의 활용

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
  <input type="button" value ="Night" onClick="

  var target = document.querySelector('body')

  if (this.value === 'Night'){
    target.style.backgroundColor= 'black';
    target.style.color = 'white';
    this.value = 'Day'

    var alist = document.querySelectorAll('a');
    var i = 0;

    while (i < alist.length){
    alist[i].style.color = 'powderblue';
    i = i + 1
}


  } else {
    target.style.backgroundColor= 'white';
    target.style.color= 'black';
    this.value = 'Night'

    var alist = document.querySelectorAll('a');
    var i = 0;

    while (i < alist.length){
    alist[i].style.color = 'blue';
    i = i + 1
    }
  }

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

- 집중할만한 부분

```html
<input type="button" value ="Night" onClick="

  var target = document.querySelector('body')

  if (this.value === 'Night'){
    target.style.backgroundColor= 'black';
    target.style.color = 'white';
    this.value = 'Day'

    var alist = document.querySelectorAll('a');
    var i = 0;

    while (i < alist.length){
    alist[i].style.color = 'powderblue';
    i = i + 1
}


  } else {
    target.style.backgroundColor= 'white';
    target.style.color= 'black';
    this.value = 'Night'

    var alist = document.querySelectorAll('a');
    var i = 0;

    while (i < alist.length){
    alist[i].style.color = 'blue';
    i = i + 1
    }
  }

  ">
```

- if else 문 사이에 while 문을 넣었다.
- 변수 alist를 선언하고 a 태그를 전부 선택했다. (querySelectorAll)
- 변수 i가 alist의 길이보다 작을때까지, alist[i]의 값을 blue나 powderblue로 변경하는 코드를 작성했다. 
- 활용에 대해서 직접적으로 배운 계기가 된 것 같다. 

## 함수 (Funtion)

```js
function nightDayHandler(self){
  var target = document.querySelector('body')

  if (self.value === 'Night'){
    target.style.backgroundColor= 'black';
    target.style.color = 'white';
    self.value = 'Day'
  
    var alist = document.querySelectorAll('a');
    var i = 0;
  
    while (i < alist.length){
    alist[i].style.color = 'powderblue';
    i = i + 1
    }
  } 

  else {
  target.style.backgroundColor= 'white';
  target.style.color= 'black';
  self.value = 'Night'

  var alist = document.querySelectorAll('a');
  var i = 0;

  while (i < alist.length){
  alist[i].style.color = 'blue';
  i = i + 1
    }
  }
}
```

- function에 담은 기능을 사용하기.

## js 함수의 이론적 정리

- 함수를 정의하고 꺼내서 쓸 수 있다. 

```js
function functionname(){
    ...
}

functionname()
```

```html
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
    </head>
    <body style="background-color: black; color: white;">
        <h1>Function</h1>
        <h2>Basic</h2>
        <ul>
            <script>
                function two(){
                    document.write('<li>2-1</li>')
                    document.write('<li>2-2</li>')
                }
                document.write('<li>1</li>')
                two()
                document.write('<li>3</li>')
            </script>
        </ul>
        <h2>Parameter & Argument</h2>
        <h2>Return</h2>
    </body>
</html>
```

- 실제로 적용해 본 사례 

## 함수 파라미터, 아규먼트

- 함수는 입력과 출력으로 이루어져 있다.
- Parameter (매개변수)
- Argument (인자)

```html
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
    </head>
    <body style="background-color: black; color: white;">
        <h1>Function</h1>
        <h2>Basic</h2>
        <ul>
            <script>
                function two(){
                    document.write('<li>2-1</li>')
                    document.write('<li>2-2</li>')
                }
                document.write('<li>1</li>')
                two()
                document.write('<li>3</li>')
            </script>
        </ul>
        <h2>Parameter & Argument</h2>
        <script>
            function oneplusone(){
                document.write(1+1+'<br>')
            }
            oneplusone();

            function sum(a,b){
                document.write(a + b +'<br>')
            }
            sum(2,3); // 5
            sum(3,4) // 7
        </script>
        <h2>Return</h2>
    </body>
</html>
```

- 예제로 알아보았다.

```js
function sum(a, b) { // 매개변수를 전달
  document.write(a + b)
}

sum(3,4) // 인자를 전달

> 7 
```

- 결과값이 잘 나오는걸 볼 수 있다. 

## return

```js
function sum2(a,b){
    return a + b
}
document.write(sum2(2,3)+'<br>')
document.write('<div style="color:red">' + sum2(2,3)+'</div>'+'<br>')
```

- 함수에 왜 가급적 한개의 기능만 넣는게 좋은지 깨달았다. 
- 다양한 맥락에서 사용할 수 있는 자유도가 생긴다. 

## 함수의 활용


```html
<input type="button" value ="Night" onClick= "nightDayHandler(this)"> // this는 본인(태그)을 지칭하는 Argument
```

```js
function nightDayHandler(self){
        var target = document.querySelector('body')

        if (self.value === 'Night'){
          target.style.backgroundColor= 'black';
          target.style.color = 'white';
          self.value = 'Day'
        
          var alist = document.querySelectorAll('a');
          var i = 0;
        
          while (i < alist.length){
          alist[i].style.color = 'powderblue';
          i = i + 1
          }
        } 

        else {
        target.style.backgroundColor= 'white';
        target.style.color= 'black';
        self.value = 'Night'
      
        var alist = document.querySelectorAll('a');
        var i = 0;
      
        while (i < alist.length){
        alist[i].style.color = 'blue';
        i = i + 1
          }
        }
      }
```

- 매개변수로 인자 this를 제공하고 함수에서는 self 로 받아서 제대로 작동하게끔 수정함. 

## 객체 (Object)

- 객체에 포함된 함수는 메소드(method) 라고 부른다.
- Object.method() 식으로 사용이 가능하다. 

- 중괄호로 객체를 만들 수 있다. 

```js
var object = {
  "object1": "object2"
}
```

```html
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
    </head>
    <body>
        <h1>Object</h1>
        <h2>Create</h2>
        <script>
            var coworkers = {
                "nickname": "Hebu",
                "heart": "Heaven"
            }
            document.write("nickname : " + coworkers.nickname + "<br>")
            document.write("heart : " + coworkers.heart + "<br>")
            coworkers["artist"] = "HeaveKK"
            document.write("artist: " + coworkers["artist"])
        </script>
    </body>
</html>
```

- 예시로 간단한 객체를 만들어서 사용해보았다.
- 추가하는 객체 중 띄어쓰기가 있어 문법적으로 오류가 있는 경우, 대괄호를 써서 해결할 수 있다.