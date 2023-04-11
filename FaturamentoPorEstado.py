

sp = float(67836.43)
rj = float(36678.66)
mg = float(29229.88)
es = float(27165.48)
outros = float(19849.53)

total = float(sp + rj + mg + es + outros)


porcentagemSp = ((sp/total)*100)
porcentagemRj = ((rj/total)*100)
porcentagemMg = ((mg/total)*100)
porcentagemEs = ((es/total)*100)
porcentagemOutros = ((outros/total)*100)

print(f'A porcentagem do faturamento do estado de São Paulo é de', round(porcentagemSp,2), '%')
print(f'A porcentagem do faturamento do estado do Rio de Janeiro é de', round(porcentagemRj,2), '%')
print(f'A porcentagem do faturamento do estado de Minas Gerais é de', round(porcentagemMg,2), '%')
print(f'A porcentagem do faturamento do estado do Espírito Santo é de', round(porcentagemEs,2), '%')
print(f'A porcentagem do faturamento dos outros estados é de', round(porcentagemOutros,2),'%')