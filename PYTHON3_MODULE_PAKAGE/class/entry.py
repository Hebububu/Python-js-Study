# ./arithmetic_module.py

#import PYTHON3_MODULE_PAKAGE.class.number_pakage.aristhmetic_module as aristhmetic_module
#print(aristhmetic_module.sum(1,2))

#import statsitcs_module
#print (statsitcs_module.sum(1,2))

#from statsitcs_module import sum # 함수 이름을 그대로 가져오기
#print(sum(1,2))

#from PYTHON3_MODULE_PAKAGE.class.number_pakage.statsitcs_module import sum as SSUM # 함수 이름을 직접 짓기
#print(SSUM(1,2))

import number_package.aristhmetic_module
print(number_package.aristhmetic_module.sum(1,2))

from number_package.aristhmetic_module import sum 
print(sum(1,2))

from number_package.aristhmetic_module import sum as SSUM
print(SSUM(1,2))