#-------------------------------------------------------#
#Exemplo de classe com properties e validações
#-------------------------------------------------------#
class Titulo():
    def __init__(self, nossonumero=None, valor=None, pagadornome=None):
        self._nossonumero = nossonumero
        self._valor = valor
        self._pagadornome = pagadornome
        self._erro = ""  # Atributo para armazenar mensagens de erro
    
    # Property para nosso numero
    @property
    def nossonumero(self):
        return self._nossonumero
    
    @nossonumero.setter
    def nossonumero(self, novo_numero):
        self._erro = ""  # Limpa erro anterior
        if not isinstance(novo_numero, str):
            self._erro = "Nosso número deve ser uma string"
            return
        if not novo_numero.strip():
            self._erro = "Nosso número não pode estar vazio"
            return
        self._nossonumero = novo_numero.strip()
    
    # Property para nome com getter e setter
    @property
    def pagadornome(self):
        return self._pagadornome
    
    @pagadornome.setter
    def pagadornome(self, novo_nome):
        self._erro = ""  # Limpa erro anterior
        if not isinstance(novo_nome, str):
            self._erro = "Nome deve ser uma string"
            return
        if not novo_nome.strip():
            self._erro = "Nome não pode estar vazio"
            return
        self._pagadornome = novo_nome.strip()
    
    # Property para valor com validação
    @property
    def valor(self):
        return self._valor
    
    @valor.setter
    def valor(self, nova_valor):
        self._erro = ""  # Limpa erro anterior
        if nova_valor < 0:
            self._erro = "Valor deve ser maior que zero"
            return
        self._valor = nova_valor
    
     
    # Property para acessar mensagem de erro
    @property
    def erro(self):
        return self._erro
    
    # Property que formata dados
    @property
    def info_completa(self):
        return f"Nosso Numero: {self._nossonumero},Pagador: {self._pagadornome},Valor R$ {self._valor}"
