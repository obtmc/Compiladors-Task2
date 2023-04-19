# Atividade da Disciplina de Compiladores - Task1 - Olivia Tavares (obtmc)

from Token import Token
from TokenType import TokenType


# Função que processa a expressão
def computing(dataComp):
    result = [];
    #size = len(data);
    i = 0;

    while (dataComp[i].lexeme != ""):
    #for i in range(0,size):
        if  dataComp[i].lexeme == '*':
            result[0] = result[0] * result[1];
            result.pop();
            #print(result[0]);

        elif dataComp[i].lexeme == '/':
            result[0] = result[0] / result[1];
            result.pop();
            #print(result[0]);

        elif dataComp[i].lexeme == '+':
            result[0] = result[0] + result[1];
            result.pop();
            #print(result[0]);

        elif dataComp[i].lexeme == '-':
            result[0] = result[0] - result[1];
            result.pop();
            #print(result[0]);
            
        elif dataComp[i].type == TokenType.NUM:
            result.append(float(dataComp[i].lexeme)); 
            #print(result);

        else: 
            print("\nUNEXPECTED ERROR: " + "\"" + dataComp[i] + "\".\n");
        
        i +=1;

    return result[0];

def scanning(dataScan):
    size = len(data);
    tokens = [];
    j = 0;
    
    # Abrindo e escrevendo no arquivos de saída
    try:
        with open('Tokens.txt', 'w') as fileOutTokens:
            #with open('Tokens.txt', 'a') as fileOutTokens:
            
                for i in range(0,size):
                    if   dataScan[i] == '*':
                        tokens.append(Token(TokenType.STAR, "*"));
                        print(tokens[j]);
                        fileOutTokens.write(f"{tokens[j]}\n");
                        j +=1;          

                    elif dataScan[i] == '/':
                        tokens.append(Token(TokenType.SLASH, "/"));
                        print(tokens[j]);
                        fileOutTokens.write(f"{tokens[j]}\n");
                        j +=1; 

                    elif dataScan[i] == '+':
                        tokens.append(Token(TokenType.PLUS, "+"));
                        print(tokens[j]);
                        fileOutTokens.write(f"{tokens[j]}\n");
                        j +=1; 

                    elif dataScan[i] == '-':
                        tokens.append(Token(TokenType.MINUS, "-"));
                        print(tokens[j]);
                        fileOutTokens.write(f"{tokens[j]}\n");
                        j +=1; 
                        
                    elif dataScan[i].isdigit():
                        tokens.append(Token(TokenType.NUM, dataScan[i]));
                        print(tokens[j]);
                        fileOutTokens.write(f"{tokens[j]}\n");
                        j +=1;
                        
                    elif dataScan[i] == "":
                        tokens.append(Token(TokenType.EOF, dataScan[i]));
                        if i+1 != size:
                            print(f"\nERROR: unexpected token: \"{dataScan[i]}\".\nThere is probably a blank line in the input: line {i+1}.\n");
                            return [];
                        
                        print(tokens[j]);
                        fileOutTokens.write(f"{tokens[j]}\n");
                        j +=1;
                            
                    else:
                        print("\nERROR: unexpected token: " + "\"" + dataScan[i] + "\".\n");
                        return [];
                    
    except Exception as e:
        print(f"\"Tokens.txt\": Return an error: {e}");
        return [];
    finally:
        fileOutTokens.close();
        
    return tokens;

# INÍCIO DO PROGRAMA

# Abrindo e lendo arquivo de entrada preservando a informação de fim de arquivo
try:
    with open('Calc1.stk', 'r') as fileIn:
        data = [];
        i = 0;
        while True:
            data.append(fileIn.readline());
            
            if data[i] == "":
                break;
            
            i +=1; 
            
except Exception as e:
    print(f"\"Calc1.stk\": Return an error: {e}");
finally:
    fileIn.close();

# Tratando entrada
# eliminando os '/n' copiados do arquivo de entrada
data = [i.strip() for i in data]; 

# Tokenização
scanResult = scanning(data);
    
if scanResult:
    # Resolvendo a expressão
    compResult = computing(scanResult);
    
    # Devolvendo resultado
    print ('\nSaída: ', compResult, '\n');

    # Abrindo e escrevendo no arquivo de saída        
    try:
        with open('Out.txt', 'w') as fileOutResult:
            fileOutResult.write(str(compResult));
    except Exception as e:
        print(f"\"Out.txt\": Return an error: {e}");
    finally:
        fileOutResult.close();
#else:
    # Não faz nada o erro já foi informado.