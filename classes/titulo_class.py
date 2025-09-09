#-------------------------------------------------------#
#Exemplo de classe com properties e validações
#-------------------------------------------------------#
class Titulo():
    def __init__(self, nossonumero=None, valor=None, pagadornome=None):
        self._nossonumero = nossonumero
        self._valor = valor
        self._pagadornome = pagadornome
    
    # Property para nosso numero
    @property
    def nossonumero(self):
        return self._nossonumero
    
    @nossonumero.setter
    def nossonumero(self, novo_numero):
        if not isinstance(novo_numero, str):
            raise TypeError("Nosso número deve ser uma string")
        if not novo_numero.strip():
            raise ValueError("Nosso número não pode estar vazio")
        self._nossonumero = novo_numero.strip()
    
    # Property para nome com getter e setter
    @property
    def pagadornome(self):
        return self._pagadornome
    
    @pagadornome.setter
    def pagadornome(self, novo_nome):
        if not isinstance(novo_nome, str):
            raise TypeError("Nome deve ser uma string")
        if not novo_nome.strip():
            raise ValueError("Nome não pode estar vazio")
        self._pagadornome = novo_nome.strip()
    
    # Property para valor com validação
    @property
    def valor(self):
        return self._valor
    
    @valor.setter
    def valor(self, nova_valor):
        if nova_valor < 0:
            raise ValueError("Valor deve ser maior que zero")
        self._valor = nova_valor
    
     
    # Property que formata dados
    @property
    def info_completa(self):
        return f"Nosso Numero: {self._nossonumero},Pagador: {self._pagadornome},Valor R$ {self._valor}"
