#---------------------------------------------------#
# Programa: exemplo01.py
# Autor: Daniel Morais Infocotidiano
# Data: 08/09/2025
#---------------------------------------------------#
from classes.titulo_class import *

titulo_atual = None
lista_titulos = []

#region incluir pessoa na classe
def incluir_titulo():
    global titulo_atual, lista_titulos
    while True:
        nome = input("Informe o nome: ")
        nossonumero = input("Informe o nosso numero: ")
        try:
            valor = float(input("Informe o valor: "))
        except ValueError as e:
            print(f"Erro: {e}")
            continue
        
        # Método novo: criar instância vazia e atribuir diretamente
        titulo_atual = Titulo()
        titulo_atual.nossonumero = nossonumero
        titulo_atual.valor = valor
        titulo_atual.pagadornome = nome
        lista_titulos.append(titulo_atual)
        print("Titulo Cadastrado -----------------")
        print(f"Pagador: {titulo_atual.pagadornome} NossoNumero: {titulo_atual.nossonumero} Valor: {titulo_atual.valor}")
        
        # Perguntar se quer adicionar outro
        continuar = input("Deseja adicionar outro titulo? (s/n): ").lower()
        if continuar not in ['s', 'sim', 'y', 'yes']:
            break
    
    print(f"Total de titulos cadastrados: {len(lista_titulos)}")
#endregion

#region retorna dados da classe
def retorna_dados():
    global titulo_atual
    if titulo_atual is None:
        print("Nenhum título foi cadastrado ainda!")
        return
    
    print("=== Dados do Título Atual ===")
    print(f"Pagador....: {titulo_atual.pagadornome}")
    print(f"NossoNumero: {titulo_atual.nossonumero}")
    print(f"Valor......: {titulo_atual.valor}")
    print("=== Concluido ===")
#endregion

#region alterar valor
def alterar_valor():
    global titulo_atual
    if titulo_atual is None:
        print("Nenhum titulo foi cadastrado ainda!")
        return
   
    try:
        nova_valor = float(input("Informe o novo valor: "))
        titulo_atual.valor = nova_valor
        print(f"Valor alterado para: {titulo_atual.valor}")
    except (ValueError, TypeError) as e:
        print(f"Erro: {e}")
#endregion

#region listar titulos
def listar_titulos():
    global lista_titulos
    if not lista_titulos:
        print("Nenhum titulo foi cadastrado ainda!")
        return
    
    print("-----<Listar Titulos>-----")
    
    # Cabeçalho alinhado
    print(f"{'NossoNumero':>10} {'Nome':<20} {'Valor':>15}")
    print("-" * 45)  # Linha separadora
    
    # Lista com valores alinhados
    for titulo in lista_titulos:
        print(f"{titulo.nossonumero:>10} {titulo.pagadornome:<20} {titulo.valor:>15.2f}")
    
    print("-----<Final de Lista!>-----")
#endregion

#region alterar nome
def alterar_nome():
    global titulo_atual
    if titulo_atual is None:
        print("Nenhum título foi cadastrado ainda!")
        return
    
    novo_nome = input("Informe o novo nome: ")
    try:
        titulo_atual.pagadornome = novo_nome
        print(f"Nome alterado para: {titulo_atual.pagadornome}")
    except (ValueError, TypeError) as e:
        print(f"Erro: {e}")
#endregion

#region gerar_ini
def gerar_ini(salvar_arquivo=False):
    if not lista_titulos:
        print("Nenhum título foi cadastrado ainda!")
        return ""
    
    ini_content = []
    
    for i, titulo in enumerate(lista_titulos, 1):
        ini_content.append(f"[Titulo{i}]")
        ini_content.append(f"Nome={titulo.pagadornome}")
        ini_content.append(f"NossoNumero={titulo.nossonumero}")
        ini_content.append(f"Valor={str(titulo.valor)}")
        ini_content.append("")
    
    ini_string = "\n".join(ini_content)
    return ini_string
#endregion

def menu():
    while True:
        print("\nMenu:")
        print("1. Incluir Título")
        print("2. Retorna Dados da Classe")
        print("3. Altera Valor do Título")
        print("4. Altera Nome do Pagador")
        print("5. Listar Títulos")
        print("6. Gerar INI")
        print("7. Finaliza")
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Por favor, digite um número válido.")
            continue

        match opcao:
            case 1:
                print("Você escolheu incluir título.")
                incluir_titulo()
            case 2:
                print("Você escolheu retornar dados.")
                retorna_dados()
            case 3:
                print("Você escolheu alterar valor.")
                alterar_valor()
            case 4:
                print("Você escolheu alterar nome.")
                alterar_nome()
            case 5:
                print("Você escolheu listar Títulos.")
                listar_titulos()
            case 6:
                print("Você escolheu gerar INI.")
                dados_ini = gerar_ini()
                print(dados_ini)
            case 7:
                print("Finalizando...")
                break
            case _:
                print("Opção inválida.")


if __name__ == "__main__":
    menu()