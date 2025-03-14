import cv2

# Configurações fixas
CAMINHO_IMAGEM = 'Imagens-Stereoscopic\img07_B0.8.png'
B = 0.8  # Alterar valor para cada imagem
FATOR_CONVERSAO = 0.004125
LAMBDA = 2.1513

# Variáveis de clique
left_click, right_click = None, None

def split_image(img):
    meio = img.shape[1] // 2
    return img[:, :meio], img[:, meio:]

def LBM_click(event, x, y, flags, param):
    global left_click
    if event == cv2.EVENT_LBUTTONDOWN:
        left_click = (x, y)
        print(f"Esquerda: X={x}, Y={y}")

def RMB_click(event, x, y, flags, param):
    global right_click
    if event == cv2.EVENT_LBUTTONDOWN:
        right_click = (x, y)
        print(f"Direita: X={x}, Y={y}")

def calc_z():
    global left_click, right_click
    if not left_click or not right_click:
        print("Clique nas duas imagens primeiro!")
        return

    # Ajuste das coordenadas
    x1 = (left_click[0] - esquerda.shape[1]//2) * FATOR_CONVERSAO
    x2 = (right_click[0] - direita.shape[1]//2) * FATOR_CONVERSAO

    # Cálculo da disparidade
    disparidade = x2 - x1
    if disparidade == 0:
        print("Erro: pontos iguais!")
        return

    z = LAMBDA - (LAMBDA * B) / disparidade
    print(f"Distância calculada: {z:.2f} metros")
    left_click = right_click = None  # Resetar cliques



img = cv2.imread(CAMINHO_IMAGEM)
esquerda, direita = split_image(img)

# Janelas e callbacks
cv2.namedWindow('Esquerda')
cv2.imshow('Esquerda', esquerda)
cv2.moveWindow("Esquerda", 20, 50)
cv2.setMouseCallback('Esquerda', LBM_click)

cv2.namedWindow('Direita')
cv2.imshow('Direita', direita)
cv2.moveWindow("Direita", 850, 50)
cv2.setMouseCallback('Direita', RMB_click)

print("Clique em pontos correspondentes e pressione:")
print("[c] Calcular distância")
print("[e] Sair")

while True:
    tecla = cv2.waitKey(1) & 0xFF
    if tecla == ord('e'):
        break
    elif tecla == ord('c'):
        calc_z()
cv2.destroyAllWindows()