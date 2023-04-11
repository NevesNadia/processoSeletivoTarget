
import json
  
f = open('dados.json')
  
data = json.load(f)
  
somaMensal = 0
numeroDeDiasUteis = 0

for i in data:
    somaMensal += float(i['valor'])
    
    if float(i['valor']) != 0:
        numeroDeDiasUteis = numeroDeDiasUteis + 1

mediaFaturamento = somaMensal/numeroDeDiasUteis

diasMaiorQueMedia = 0

for i in data:
    if float(i['valor']) > mediaFaturamento:
        diasMaiorQueMedia = diasMaiorQueMedia +1



print('O menor valor de faturamento ocorrido em um dia é de R$', min(round(float(i['valor']),2) for i in data if i['valor'] > 0))
print('O maior valor de faturamento ocorrido em um dia é de R$', max(round(float(i['valor']),2) for i in data))
print('O faturamento diário foi superior à média mensal em', diasMaiorQueMedia, 'dias.')


f.close()