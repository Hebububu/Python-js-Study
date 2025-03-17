# 1억줄의 코드

#def get_vat(price):
#    vat_rate = 0.1
#    print(price*vat_rate)
#
#get_vat(10000)
#get_vat(20000)

# 1억줄의 코드 

#def get_vat(price,vat_rate):
#    print(price*vat_rate)
#
#get_vat(20000,0.3)

#def get_vat(price, vat_rate = 0.1):
#    print (price*vat_rate)
#
#get_vat(20000)

def get_vat(price, vat_rate=0.1):
    return price*vat_rate

print(get_vat(10000))