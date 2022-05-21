class CpfException(Exception):
    
    def __init__(self):
        super().__init__("Cpf Invalido")