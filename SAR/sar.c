
//INTEGRANTES:
//Guilherme Nishi Kanashiro (RA: 628298)
//Tiago Bachiega de Almeida (RA: 628247)


#include <iostream>
#include <string>
#include <fstream> //relacionado a arquivo
#include <stdio.h>
#include <dirent.h> //Relacionado a diretorio
#include <vector>
#include <string.h>
#include <sstream> //Relacionado a string
#include <stdlib.h>
#include <windows.h> //Permitem usar comandos que afetam
#include <windef.h>  // o Sistema Operacional

//COMO TESTAR O PROGRAMA: O programa funciona exatamente te acordo com as instrucoes.
// O nome do arquivo onde o diretorio é  salvo é conteudo.sar
//Quando o arquivo é extraido, o resultado fica na pasta 'extracao', dentro do local onde esta
// o .exe e o arquivo.sar

//ORGANIZACAO DE ARQUIVO: Tamanho do Campo + Keyword com tipo + (se for binario) Conteudo
// Ex : 15DIR=C:/Trabalho11FIL=abc.txt12TXT=trabalho

using namespace std;
 
void menu(vector<string> &conteudo); //Menu do programa
void gravaArquivo(string input, string output, string dirF); //Grava um elemento do tipo arquivo no zip
vector<string> conteudoDoDir(string dirN); //Lista o que tem no diretório
void gravaDir(string input, string output); // Grava um elemento do tipo diretório no zip
vector<string> listSubdir(string dirN); //Lista os subdiretórios
void extrair(string arquivo); //Recria o diretorio
int encontraTamanho(string conteudo, int &inicioSubstr); //Encontra o tamanho do campo
void criaArquivoComp(vector<string> conteudo, string dir); //Cria o arquivo sar
void listaElementos(string arquivo); //Lista o arquivo sar
vector<string> caminhoUtil(vector<string> conteudo, string dirFonte); //Essa funcao retorna somente o caminho relevante para a extracao
																		// Como e na mesma pasta, ele remove o C:/Users...

int main(){
	int instrucao; 
	
	vector<string> conteudo;
	
	menu(conteudo); //chama o menu
	
	return 0;
}

void menu(vector<string> &conteudo){
	
	string opcao = "";
	string diretorioFonte;
	string arquivoComp; //arquivo onde esta a compressao
	
	while(opcao != "sair"){
		
		cout << "Digite a opcao desejada. Para ter ajuda, digite 'ajuda'. \n";
		
		cin >> opcao;
		
		if(opcao == "ajuda"){
			
			cout << "Para salvar um diretorio, digite -c [caminho do diretorio] \n";
			cout << "Para extrair o diretorio, digite -e [nome do arquivo onde esta salvo]\n";
			cout << "Para listar o conteudo do arquivo, digite -l [nome do arquivo]\n";
			cout << "Para encerrar o programa, digite 'sair'\n";
			cout << "RETURN CODES : 0 -> bem sucedido / 1 -> caminho invalido para dir / 2 -> arquivo nao e .sar valido\n\n";
			
		}
		if(opcao.find("-c")!=-1){  //Opcao cria arquivo
			
			cin >>diretorioFonte;  //Le diretorio Fonte
			
			if (GetFileAttributes(diretorioFonte.c_str()) != FILE_ATTRIBUTE_DIRECTORY){ //RETURN CODE de erro
				cout << "1\n";
			}
			else{
				
				conteudo = listSubdir(diretorioFonte.c_str()); //lista o conteudo do diretorio
				
				conteudo = caminhoUtil(conteudo, diretorioFonte); //Salva o caminho util
				
				criaArquivoComp(conteudo, diretorioFonte); //Cria o arquivo
				
				cout << "0\n"; //Operacao bem sucedida
			}
		}
		
		if(opcao.find("-e")!=-1){ //Extrai na pasta destino
			
			cin >> arquivoComp; // le o arquivo (caminho dele e seu nome)
			
			if(arquivoComp.find(".sar")==-1){ //RETURN CODE de erro
				cout << "2\n";
			}
			else{
				
				extrair(arquivoComp.c_str()); //Extrai
					
				cout << "0\n"; //Operacao bem sucedida
			}
		}
		
		if(opcao.find("-l")!=-1){ //Lista arquivo sar 
			cin >> arquivoComp; // le arquivo sar
			
			if(arquivoComp.find(".sar")==-1){ //RETURN CODE de erro
				cout << "2\n";
			}
			else{
			
				listaElementos(arquivoComp); //Lista arquivo sar			
				cout << "0\n"; //Operacao bem sucedida
			}
		}
	}
	
}

void listaElementos(string arquivoComp){ //Lista o arquivo sar
	
	ifstream fonte(arquivoComp.c_str(), ios::binary); 
    string conteudo = "";
    int tamanho=0;
	char ch;
	string campo;
	string elemento; 
	
    while(fonte.get(ch)) { //Le o nome de cada conteudo
    	conteudo += ch;
    	
	}
	
	for(int i = 0; i < conteudo.size(); i+=tamanho){ 
		
		tamanho = encontraTamanho( conteudo, i); //Tamanho do campo
		campo = conteudo.substr(i, tamanho); //salva o campo
	
		if(campo.compare(0, 4, "DIR=")==0){ //Se possuir indicador DIR= 
			elemento = campo.substr(4, campo.size()-1); //Salva o caminho sem o indicador DIR= e o de tamanho de campo
			cout << elemento +"\n";  //Lista
		}
		if(campo.compare(0, 4, "FIL=")==0){ //Se possuir indicador FIL= 
			elemento = campo.substr(4,  campo.size()-1); //Salva o campo sem o indicador FIL= e o de tamanho de campo
			cout <<  elemento +"\n"; //Lista
		}
	}
}

void criaArquivoComp(vector<string> conteudo, string dir){ //Cria arquivo sar
	
		for(int i = 0; i < conteudo.size(); i++) {
			if(GetFileAttributes((dir + "/" + conteudo[i]).c_str()) != FILE_ATTRIBUTE_DIRECTORY) gravaArquivo(conteudo[i], "conteudo.sar", dir);
			//Se nao for dir, grava como binario
			else  gravaDir(conteudo[i], "conteudo.sar");	 //Se for dir, grava como diretorio
		}
}

void gravaDir(string input, string output){
	
    ofstream destino(output.c_str(),ios_base::app);  //Abre destino no modo append(inserir no final sem apagar)
    int tamanhoDoCampo = input.size()+4; //+4 =>DIR=    // DIR= é um identificador de diretorio no arquivo (organizacao). Deve ser pulado
    
    //CONVERTE TAMANHO PRA STRING
	std::stringstream ss; 
	ss << tamanhoDoCampo;
	std::string tamanhoString = ss.str();
    
    for(int i = 0; i < input.size(); i++){ //Padroniza as barras
    	if(input[i]==92){
    		input[i] = '/';
		}	
	}
	
    //SALVA O DESTINO COM PREFIXO DIR=
    destino << tamanhoString + "DIR="+ input;
    destino.close();
}

void gravaArquivo(string input, string output, string dirF){
	
	ifstream fonte((dirF + "/" + input).c_str(), ios::binary); //Abre arquivo de fonte (txt, ppt, pdf, etc) em modo binario
    ofstream destino(output.c_str(),ios_base::app | ofstream::binary); //Abre destino como append e binario
    string conteudo = ""; 
    int i;
	char ch;
	
	
	//CONVERTE TAMANHO PARA STRING
	int tamanhoDoCampo = input.size()+4;  //+4 =>FIL=    // FIL= é um identificador de arquivo (organizacao). Deve ser pulado
    std::stringstream ss; 
	ss << tamanhoDoCampo;
	std::string tamanhoString = ss.str();
	
	//LE CADA CARACTER DO ARQUIVO TXT	
    while(fonte.get(ch)) {
    	conteudo += ch;
	}
	
    i--;
    conteudo.erase(conteudo.end()-1);

    fonte.close();
    
	//CONVERTE TAMANHO PARA STRING
	int tamanhoDoConteudo = conteudo.size()+4; //+4 =>TXT=    // TXT= é um identificador de conteudo do arquivo (organizacao). Deve ser pulado
    std::stringstream ss2; 
	ss2 << tamanhoDoConteudo;
	std::string tamanhoContString = ss2.str();
    
    for(int i = 0; i < input.size(); i++){
    	if(input[i]==92){
    		input[i] = '/';
		}	
	}
    
  	//GRAVA O ARQUIVO COM PREFIXO FIL= E CONTEUDO TXT=  
    destino << tamanhoString + "FIL="+input << tamanhoContString + "TXT=" << conteudo;
    destino.close();
    
}

//LISTA TUDO O QUE EXISTE DENTRO DO DIRETÓRIO ATUAL
vector<string> conteudoDoDir(string dirN){
	
	const char * dirNome = dirN.c_str(); //Nome do diretorio
	DIR *dir; //Variavel relacionada a esta biblioteca. Funciona de maneira semalhante a arquivo
	struct dirent *leitura; //para onde vai o que foi lido 
	vector<string> conteudo; //Conteudo do diretorio
	string nome; //Nome do diretorios
	
	if ((dir = opendir (dirNome)) != NULL) { //Abre o diretorio
		
  		while ((leitura = readdir (dir)) != NULL) { //Le o conteudo do diretorio
  			nome = string(leitura->d_name);	
  			if(nome != "." && nome!= "..")
  				conteudo.push_back(nome); //Adiciona em conteudo cada arquivo/diretorio
  		}
  	
  		closedir (dir);
  	
	} 
	
	return conteudo;
}

//Percorre os subdiretorios
vector<string> listSubdir(string dirN){
	
	vector<string> conteudo = conteudoDoDir(dirN);
	vector<string> tempConteudo = conteudo;
	vector<string> conteudoFinal;
	int max = conteudo.size();
	DWORD atributo;
	
	for(int i = 0; i < max; i++){
		conteudoFinal.push_back(dirN + "/" +conteudo[i]);  //Adiciona o conteudo do diretorio atual na lista final
	}
	
	for(int i = 0; i < max; i++) {
		
		if(atributo = GetFileAttributes((dirN + "/" + conteudo[i]).c_str()) == FILE_ATTRIBUTE_DIRECTORY) {
			
			tempConteudo = listSubdir(dirN + "/" + conteudo[i]); //Chama subdiretorios recursivamente
			
			conteudoFinal.insert(conteudoFinal.end(), tempConteudo.begin(), tempConteudo.end()); //Insere o que foi encontrado nos subdiretorios
				
		}
	}
	
	return conteudoFinal;
}

//Recria o diretorio salvo em out.sar
void extrair(string arquivo){
	
	ifstream fonte(arquivo.c_str(), ios::binary); 
    string conteudo = "";
    int tamanho=0;
	char ch;
	string campo;
	string caminhoNovoArquivo; 
	string caminhoFinal;
	string textoDoArquivo;
	
    while(fonte.get(ch)) { //Le o nome de cada conteudo
    	conteudo += ch;
    	
	}
	
	CreateDirectory("./extracao", NULL); //Cria a pasta de extracao  
	
	for(int i = 0; i < conteudo.size(); i+=tamanho){ 
		
		tamanho = encontraTamanho( conteudo, i); //calcula tamanho do campo 
		campo = conteudo.substr(i, tamanho); //le campo
	
		if(campo.compare(0, 4, "DIR=")==0){ //Se possuir indicador DIR= 
		
			caminhoNovoArquivo = campo.substr(4, campo.size()-1);
			caminhoFinal = "./extracao/" + caminhoNovoArquivo;
			
			CreateDirectory(caminhoFinal.c_str(), NULL); //Cria pasta
			}
		if(campo.compare(0, 4, "FIL=")==0){ //Se possuir indicador FIL=
			caminhoNovoArquivo = campo.substr(4,  campo.size()-1);
			caminhoFinal = "./extracao/" + caminhoNovoArquivo;
		}
		if(campo.compare(0, 4, "TXT=")==0){ //Pega o conteudo de FIL= pelo TXT=
			textoDoArquivo = campo.substr(4, campo.size()-1); //Salva o conteudo binario sem indicadores
			ofstream novoArquivo(("./extracao/" + caminhoNovoArquivo).c_str(), ofstream::binary); //Cria um novo arquivo binario
			novoArquivo << textoDoArquivo; //Grava no novo arquivo
			novoArquivo.close();
		} 
		
	}
	
}

int encontraTamanho(string conteudo, int &inicioSubstr){
	
	string conteudoNum;
	int tamanho;
	
	
	while(isdigit(conteudo[inicioSubstr])){ //Enquanto os primeiros caracteres nao forem digito, ou seja, para antes do indicador de tipo de conteudo 
											//(DIR, FIL, TXT)
		conteudoNum += conteudo[inicioSubstr]; //Salva o tamanho do campo
		inicioSubstr++; 
	}
	
	istringstream buffer(conteudoNum);
	buffer >> tamanho;
	
	return tamanho ; //Retorna o tamanho do campo e posiciona o i da funcao anterior no lugar certo (primeiro char do indicador DIR, FIL ou TXT)
}

vector<string> caminhoUtil(vector<string> conteudo, string dirFonte){	
	
	vector<string> conteudoUtil;
	
	for(int i = 0; i < conteudo.size(); i++){
		
		string temp = conteudo[i];
		int dist = temp.size() - dirFonte.size(); //Calcula o alcance da parte relevante do endereco (a partir da pasta atual, ate subpastas)
		
		string contTemp = temp.substr(dirFonte.size()+1, dist+1);
		
 		conteudoUtil.push_back(contTemp);
	}
	
	return conteudoUtil;
	
}
