idade = int(raw_input())

ano = idade/365
dias = idade % 365
mes = dias/30
dias = dias % 30

print "%d ano(s)" %(ano)
print "%d mes(es)" %(mes)
print "%d dia(s)" %(dias)

