import pytest
from src.cpf_value import Cpf

import src

class TestCpfValidator:

    def test_should_be_true(self):
        cpf_test = "101.201.049-03"
        cpf_object = Cpf(cpf_test)
        assert cpf_test == cpf_object.cpf 

    def test_should_be_false(self):
        with pytest.raises(Exception, match='Cpf Invalido') as exception:
            cpf_test = "101.201.0000000000"
            Cpf(cpf_test)