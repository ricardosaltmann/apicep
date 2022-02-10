import requests
from cep import BuscaEndereco

cep = "06705050"
objeto_cep = BuscaEndereco(cep)

bairro, uf, logradouro = objeto_cep.acessa_via_cep()
print(bairro,logradouro,uf)