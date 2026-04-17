
plantacao_A = 80000
plantacao_B = 200000
qnts_anos = 0

while plantacao_A <= plantacao_B:
    
    plantacao_A *= 1.03
    plantacao_B *= 1.015

    qnts_anos += 1

print(f"Demorou {qnts_anos} anos para a plantação A ultrapassar ou se igualar a plantação B")
