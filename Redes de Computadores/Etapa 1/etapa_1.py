#!/usr/bin/python3
# -*- encoding: utf-8 -*-
import socket
import csv

#recebe um nome em uma string e procura no registro
#o nome deve estar no formado <nome>_<sobrenome>
def encontra_registro(request):
    with open('dados.csv', 'r') as d:
        registros = csv.reader(d)
        resultado = [] #["erro",'-400',"Nao esta no db"]
        for linha in registros:
            nome = linha[0]
            if(request.lower() in nome.lower()):
                resultado.append(linha)
				
        d.close()
    
    return resultado

''' Pagina HTML
    Arquivo com a pagina inicial do projeto
    recebe o nome da pessoa ao qual os dados 
    deseja-se consultar
'''
def homePage():
    arquivo = open('homePage.txt','r')
    hp = arquivo.read()
    arquivo.close()
    return hp
	
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', 8000))
s.listen(1)

while True:
    cli, addr = s.accept()
    
    while True:
        req = b''
        while not (b'\r\n\r\n' in req or b'\n\n' in req):
            pedaco = cli.recv(1500)
            if pedaco == b'':
                break
            req += pedaco
        if req == b'':
            break
        print(req.decode('utf-8'))
        print('requisição tem %d bytes' % len(req))
        metodo, caminho, lixo = req.split(b' ', 2)
        
        # Solicitado dados
        if caminho.decode('utf-8').find('?name')>0 :
            nome_bytes = caminho.replace(b'/?name=', b'').replace(b'+', b' ')
            
            #transforma bytes em string
            nome_str = nome_bytes.decode(("utf-8"))
            
            #procura o registro
            registro = encontra_registro(nome_str)
            
            if len(registro) == 0:
                resposta = b'<div align=center><h2 class="page-title">404: Name not found</h2></div>'
                cli.send(b'HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\nContent-Length: %d\r\n\r\n' %len(resposta))
                cli.send(resposta)
            
            else:
                resposta = b'<p><b>Dados dos usuarios encontrados:</b></p>'
                for reg in registro:
                    #transforma os dados do registro encontrado para bytes
                    nome_reg = str.encode(reg[0])
                    idade_reg = str.encode(reg[1])
                    curso_reg = str.encode(reg[2])

                    # Mostra todos os registros
                    resposta = resposta + b'<p>Nome: %s</p><p>Idade: %s</p><p>Curso: %s</p><br>' % (nome_reg,idade_reg,curso_reg)
                    
                    
                cli.send(b'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: %d\r\n\r\n' % len(resposta))
                cli.send(resposta)

        # Nenhum da do foi solicitado - Home Page
        else:
            page = bytes(homePage(),'utf-8')
            cli.send(b'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: %d\r\n\r\n' % len(page))
            cli.send(page) 

    cli.close()
    print('<conexao fechada>')
