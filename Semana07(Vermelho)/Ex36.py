
num_total_oliveiras = int(input('Digite o número total de oliveiras para serem plantadas: '))
num_fileiras_disponiveis = int(input('Digite o número de fileiras disponíveis no campo: '))

qnts_oliveiras = num_total_oliveiras / num_fileiras_disponiveis
sobra_oliveiras = num_total_oliveiras % num_fileiras_disponiveis

print(f"Ficará {qnts_oliveiras:.0f} em cada fileira.")
print(f'Ficou sobrando {sobra_oliveiras} oliveiras.')
