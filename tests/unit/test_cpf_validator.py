import pytest
from src.domain.entity.cpf_value import Cpf
from src.exceptions.cpf_exception import CpfException

class TestCpfValidator:

    def test_should_be_true(self):
        cpf_test = "101.201.049-03"
        cpf_object = Cpf(cpf_test)
        assert cpf_test == cpf_object.cpf 

    def test_should_be_false(self):
        with pytest.raises(CpfException, match='Cpf Invalido') as exception:
            cpf_test = "101.201.0000000000"
            Cpf(cpf_test)