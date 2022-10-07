# Variáveis
verificadorDeTamanho = 0
soma = 0

# Verificar se os dígitos informados têm exatamente os 11 dígitos do CPF
while verificadorDeTamanho != 11:
    cpf = input('Digite um CPF válido(11 números): ')
    verificadorDeTamanho = len(cpf)

if len(set(cpf)) == 1:
    print('CPF INVÁLIDO!!!')
else:
    #Primeira verificação
    for p, r in enumerate(range(10, 1, -1)):
        soma += int(cpf[p]) * r
    #Quando o resto for 10 o dígito verificador equivale a 0
    resto = (10 * soma) % 11
    if resto == 10:
        resto = 0
    if not (resto % 11 == int(cpf[9])):
        print('CPF INVÁLIDO!!!')

    else:
        soma = 0
        for p, r in enumerate(range(11, 1, -1)):
            soma += (int(cpf[p]) * r)
        
        #Quando o resto for 10 o dígito verificador equivale a 0
        resto = (10 * soma) % 11
        if resto == 10:
            resto = 0
        if not (resto % 11 == int(cpf[10])):
            print('CPF INVÁLIDO!!!')
        else:
            print('CPF VÁLIDO!!!')
