import random

a = ['小貓','小狗','小豬','小雞']
#print(random.sample(a,1)[0])

b = ['玩','丟','踢','打','吃','喝']
#print(random.sample(b,1)[0])

c = ['玩具','球','泥巴','食物','筆','汽油']
for i in range(10):
    print(random.sample(a,1)[0]+random.sample(b,1)[0]+random.sample(c,1)[0])
    