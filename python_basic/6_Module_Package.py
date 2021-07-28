# 지금까지 파이썬 프로그램을 실행해 볼 때 인터프리터를 사용해서 실행을 시켜다.  
# 이 경우 인터프리터를 종료하면 작성한 내용이 모두 사라진다.  
# 작성된 프로그램을 보존하기 위해서 프로그램의 내용을 텍스트 파일에 적어 보존 할 수 있는 방법이 모듈이다.  
# 이런 모듈들이 많아지면 모듈들을 잘 분류해서 모아둔 패키지를 만들어서 사용한다.  
# 파이썬 내에서 이미 만들어서 제공되는 유용한 패키지들이 많이 있지만, 자신이 만들어서 쓰는 경우도 많다.  

# 패키지

# 상대 경로
# .. : 부모 디렉토리
# . : 현재 디렉토리



# 1. 모든 class를 import
# - 불필요한 class까지 가져와 리소스를 낭비할 수 있기 때문에 권장하는 방법은 아님
# from pkg.fibonacci import *

# 2. 지정한 class만 import
from pkg.fibonacci import Fibonacci
Fibonacci.fib(300)
print(Fibonacci.fib2(300))
print()

# 3. 지정한 class를 지정한 이름으로 import
from pkg.fibonacci import Fibonacci as fb
fb.fib(300)
print(fb.fib2(300))
print()

# 4. function
import pkg.calculation as cal
print(cal.add(10, 100))
print(cal.mul(10, 100))
print()

# 5. 지정한 function만 import
from pkg.calculation import div as d
print(int(d(100,5)))
print()