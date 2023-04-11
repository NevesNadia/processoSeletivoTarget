
import json
  
f = open('dados.json')
  
data = json.load(f)
  
somaMensal = 0

for i in data:
    somaMensal += float(i['valor'])


print(somaMensal)



# for i in data:
#    print(i)

f.close()