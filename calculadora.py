#Dicionario de operações
calculos = {
    '+' : lambda x,y : x + y,
    '-' : lambda x,y : x - y,
    '*' : lambda x,y : x * y,
    '/' : lambda x,y : x / y,
}
#Pergunta para saber se o usuário quer continar a fazer cálculos
def finalizar():
    encerra = input('Deseja continuar? S/N\n') 
    if encerra.lower() == 's':
        return 0
    elif encerra.lower() == 'n':
        return 1
    else:
        print('Valor Invalido')
        return finalizar()
        
#Solicita numero inteiro e faz teste para verificar se o input é int
def valida_numero():
    try:
        numero = int(input('Digite um numero\n'))
        return numero
    except ValueError:
        print('Não é um número')
        return valida_numero()
    
#Solicita operação e testa para ver se é uma operação valida
def valida_operacao():
    operacao = input('Qual sera a operação? (* / + -)\n')
    if operacao not in ['+','-','*','/']:
        print('Operação invalida')
        return valida_operacao()
    else:
        return operacao
        
def main():
    continuar=0
    while continuar == 0 :
        numero1 = valida_numero()
        operacao = valida_operacao()
        numero2 = valida_numero()
        while True:
            if operacao == '/' and numero2 == 0:
                print('Não se pode dividor por 0, digite outro para completar a operação\n')
                numero2 = valida_numero()
            else:
                break

        resultado = calculos[operacao](numero1,numero2)
        print(f'{numero1} {operacao} {numero2} = {resultado}')

        continuar = finalizar()

main()