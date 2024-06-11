from validate_docbr import CPF #importa a classe cpf

cpf = CPF()

print(cpf.generate(True)) #with rimel on
print(cpf.generate(False)) #without rimel on


# Validar CPF
print(cpf.validate("515.555.878.60"))# True
cpf.validate("012.345.678-91")  # False

