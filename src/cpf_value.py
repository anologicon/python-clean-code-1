class Cpf:

    def __init__(self, cpf):
        self.cpf = cpf
        if not self.validate() :
            self.throw_error()

    def validate(self) -> bool:
        if not self.cpf:
            return False
        if (len(self.cpf) < 11) or (len(self.cpf) > 14):
            return False
        return True
    
    def throw_error(self):
        raise Exception("Cpf Invalido")

        