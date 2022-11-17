# 허수의 아름다움

An imaginary number is a real number multiplied by the imaginary unit i, which is defined by its property i² = −1. 
```
i² = −1. 
```

우리가 어렸을 때 부터 배운 수의 체계로는 그 수를 제곱하면 양수가 나오는 것은 당연한 결과일 것이다.

## 허수의 특징

- 복소수의 연산
- 방정식의 해
- 복소평면
- 뷰티풀(내가 지은 특징이다. ㅋㅋ)

### 복소수의 연산

```python
a = 3 + 4j
b = 1 + 7j

print(a + b) # 4 + 11j
print(a - b) # 2 - 3j
print(a * b) # -25 + 25j
print(a / b) # 0.62 - 0.34j
```
초등학교 떄부터 배우던 사칙연산 개념을 사용할 수 있다.
실수 부분은 그 부분끼리, 허수 부분은 그 부분끼리 사칙연산을 해주면 된다.

### 방정식의 해

```python
a = int(input('이차항의 계수를 입력하세요. '))
b = int(input('일차항의 계수를 입력하세요. '))
c = int(input('상수항의 계수를 입력하세요. '))
d = b**2 - 4*a*c

if d < 0:
    real = round(-b / (2*a))
    imag = round((abs(d) ** 0.5) / (2*a))
    if real:
        if imag == 1: print(f'{real} + i, {real} - i')
        else: print(f'{real} + {imag}i, {real} - {imag}i')
    else:
        if imag == 1: print('i, -i')
        else: print(f'{imag}i, -{imag}i')
elif d == 0:
    print(round((-b + d ** 0.5) / (2*a)))
else:
    print(round((-b + d ** 0.5) / (2*a)), end=', ')
    print(round((-b - d ** 0.5) / (2*a)))
```

모든 고차 함수의 해를 구하는 데 허수가 안 쓰일 수 없다.(1차는 빼고 ㅎ)
