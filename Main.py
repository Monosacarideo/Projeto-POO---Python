from Cadastro import Cadastro
import os
from Validacao import verificar_inteiro

def menu():
    cadastro = Cadastro()
    titulo = "\n\n == Guarda-Roupas == \n\n"
    menuTexto = "[1] Cadastrar peça de roupa \n[2] Inserir peça de roupa no estoque \n[3] Mostrar peças de roupa \n[4] Excluir peça de roupa \n[5] Remover peça de roupa do estoque \n[6] Editar peça de roupa \n[7] Sair \n\n========================\n" 

    print(titulo)
    print(menuTexto)
    opcaoMenu = verificar_inteiro("Sua escolha: ")
    while(opcaoMenu != 7):
        if opcaoMenu == 1:
            os.system("cls") 
            cadastro.cadastrar_peca()
        
        elif opcaoMenu == 2:
            os.system("cls")
            cadastro.acessar_estoque()
        
        elif opcaoMenu == 3:
            os.system("cls")
            cadastro.exibir_pecas()
        
        elif opcaoMenu == 4:
            os.system("cls")  
            cadastro.deletar_peca()

        elif opcaoMenu == 5:
            os.system("cls")  
            cadastro.remove_estoque() 
        
        elif opcaoMenu == 6:
            os.system("cls")
            cadastro.editar_peca()
    
        os.system("cls")
        print(titulo) 
        print(menuTexto)
        opcaoMenu = verificar_inteiro("Escolha uma opção: ")

if __name__ == "__main__":
    print("  ____                         _           _                                         ____                     _         ____                                  ")                                                        
    print(" | __ )  ___ _ __ ___   __   _(_)_ __   __| | ___     __ _  ___    ___  ___ _   _   / ___|_   _  __ _ _ __ __| | __ _  |  _ \ ___  _   _ _ __   __ _ ___      ")                                                        
    print(" |  _ \ / _ \ '_ ` _ \  \ \ / / | '_ \ / _` |/ _ \   / _` |/ _ \  / __|/ _ \ | | | | |  _| | | |/ _` | '__/ _` |/ _` | | |_) / _ \| | | | '_ \ / _` / __|     ")                                                        
    print(" | |_) |  __/ | | | | |  \ V /| | | | | (_| | (_) | | (_| | (_) | \__ \  __/ |_| | | |_| | |_| | (_| | | | (_| | (_| | |  _ < (_) | |_| | |_) | (_| \__ \     ")                                                        
    print(" |____/ \___|_| |_| |_|   \_/ |_|_| |_|\__,_|\___/   \__,_|\___/  |___/\___|\__,_|  \____|\__,_|\__,_|_|  \__,_|\__,_| |_| \_\___/ \__,_| .__/ \__,_|___/     ")  
    print("\n")
    print("                .=-----------------------============================:.  ")               
    print("                 .=                       =.                        .=   ")             
    print("                 .=                       =.                        .=   ")            
    print("                 .=                       =.                        .=   ")            
    print("                 .=                       =.                        .=   ")            
    print("                 .=                       =.                        .=   ")            
    print("                 .=                       =.                        .=   ")            
    print("                 .=                       =.                        .=   ")            
    print("                 .=                       =. ..                     .=   ")            
    print("                 .=                   %#  =. #*                     .=   ")            
    print("                 .=                   #*  =. **                     .=   ")            
    print("                 .=                   #*  =. **                     .=   ")            
    print("                 .=                   #*  =. **                     .=   ")            
    print("                 .=                   ==  =. -:                     .=   ")            
    print("                 .=                       =.                        .=   ")            
    print("                 .=                       =.                        .=   ")            
    print("                 .=                       =.                        .=   ")            
    print("                 .=                       =.                        .=   ")            
    print("                 .=                       =.                        .=   ")            
    print("                 .=                       =.                        .=   ")            
    print("                 .*-----------------------*=------------------------==   ")            
    print("                 .=                  .=--------+                    .=   ")            
    print("                 .=                  :+--------#                    .=   ")            
    print("                 .#==================++=============================+=   ")            
    print("                 .*                  *+++++++++#-                   .=   ")            
    print("                 .*                  ............                   :=   ")            
    print("                 .#==================++++++++++++===================*=   ")            
    print("                 .=                  %==========*                   -=   ")            
    print("                 .=                                                 -=   ")            
    print("                 .+-------------------------------------------------=:   ")            
    print("\n") 
    input("Pressione a tecla ENTER para seguir")                                                                            
                                                                                                                            

    menu()