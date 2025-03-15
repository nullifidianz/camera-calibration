import cv2
import os
import re
from main import split_image, FATOR_CONVERSAO, LAMBDA

def extrair_b_do_nome(nome_arquivo):
    """Extrai o valor B do nome do arquivo."""
    match = re.search(r'B(\d+\.\d+)', nome_arquivo)
    if match:
        return float(match.group(1))
    return None

def calcular_z(ponto_esq, ponto_dir, B, largura_img):
    """Calcula a distância Z usando os pontos correspondentes."""
    x1 = (ponto_esq[0] - largura_img//2) * FATOR_CONVERSAO
    x2 = (ponto_dir[0] - largura_img//2) * FATOR_CONVERSAO

    # Mantendo x2 - x1 para disparidade
    disparidade = x2 - x1
    if abs(disparidade) < 1e-6:
        return None

    # Reorganizando a fórmula para garantir valores positivos
    z = (LAMBDA * B) / abs(disparidade)
    return z

def mostrar_e_testar_imagem(caminho_imagem):
    """Mostra as imagens e realiza o teste com pontos pré-definidos."""
    nome_arquivo = os.path.basename(caminho_imagem)
    B = extrair_b_do_nome(nome_arquivo)
    if B is None:
        print(f"ERRO: Não foi possível extrair B de {nome_arquivo}")
        return

    img = cv2.imread(caminho_imagem)
    if img is None:
        print(f"ERRO: Não foi possível carregar {caminho_imagem}")
        return
    
    esquerda, direita = split_image(img)
    largura = esquerda.shape[1]

    # Pontos de teste atualizados
    pontos_teste = [
        ((200, 217), (180, 217)),  # Ponto específico com deslocamento à esquerda na imagem direita
    ]

    print(f"\n{'='*60}")
    print(f"Testando par de imagens: {nome_arquivo}")
    print(f"{'='*60}")

    # Mostra as imagens
    cv2.namedWindow('Imagem Esquerda', cv2.WINDOW_NORMAL)
    cv2.namedWindow('Imagem Direita', cv2.WINDOW_NORMAL)
    
    cv2.imshow('Imagem Esquerda', esquerda)
    cv2.imshow('Imagem Direita', direita)
    
    # Posiciona as janelas lado a lado
    cv2.moveWindow('Imagem Esquerda', 50, 50)
    cv2.moveWindow('Imagem Direita', 50 + esquerda.shape[1] + 10, 50)

    # Para cada ponto de teste
    for ponto_esq, ponto_dir in pontos_teste:
        # Desenha os pontos nas imagens
        cv2.circle(esquerda, ponto_esq, 5, (0, 0, 255), -1)
        cv2.circle(direita, ponto_dir, 5, (0, 0, 255), -1)
        
        # Atualiza as imagens com os pontos
        cv2.imshow('Imagem Esquerda', esquerda)
        cv2.imshow('Imagem Direita', direita)

        # Calcula e mostra os resultados
        z = calcular_z(ponto_esq, ponto_dir, B, largura)
        
        print("\nPontos clicados:")
        print(f"Imagem Esquerda: x={ponto_esq[0]}, y={ponto_esq[1]}")
        print(f"Imagem Direita:  x={ponto_dir[0]}, y={ponto_dir[1]}")
        
        if z is not None:
            print(f"Distância calculada: {z:.2f} metros")
        else:
            print("ERRO: Não foi possível calcular a distância")

        # Espera o usuário pressionar uma tecla
        print("\nPressione qualquer tecla para continuar...")
        cv2.waitKey(0)

    # Fecha as janelas desta imagem
    cv2.destroyAllWindows()

def main():
    """Função principal que executa os testes para todas as imagens."""
    pasta_imagens = 'Imagens-Stereoscopic'
    
    # Lista e ordena as imagens PNG
    imagens = [f for f in os.listdir(pasta_imagens) if f.endswith('.png')]
    imagens.sort()

    if not imagens:
        print("Nenhuma imagem PNG encontrada na pasta!")
        return

    print("\nIniciando testes para os 6 pares de imagens...")
    
    # Testa cada imagem
    for imagem in imagens:
        caminho_completo = os.path.join(pasta_imagens, imagem)
        mostrar_e_testar_imagem(caminho_completo)

    print("\nTodos os testes foram concluídos!")

if __name__ == "__main__":
    main() 