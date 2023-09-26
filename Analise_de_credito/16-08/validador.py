from validate_docbr import CPF, CNPJ

def validar_cpf(cpf: str) -> bool:
    cpf = CPF()
    return cpf.validate(cpf)

def validar_cnpj(cnpj: str) -> bool:
    cnpj = CNPJ()
    return cnpj.validate(cnpj)

