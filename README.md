(Due to technical issues, the search service is temporarily unavailable.)

### GUIA RÁPIDO DE USO DO PROGRAMA DE CÁLCULO DE DISTÂNCIA ESTEREOSCÓPICA  

---

#### **PRÉ-REQUISITOS**  
1. Ter o programa configurado com:  
   - Caminho da imagem já definido no código (não precisa inserir durante a execução).  
   - Valor de `B` correto para a imagem (pré-configurado no código).  
2. A imagem deve ser um par estereoscópico (duas perspectivas lado a lado em um único arquivo).  

---

#### **PASSO A PASSO**  

1. **INICIAR O PROGRAMA**  
   - Execute o script Python.  
   - Duas janelas aparecerão automaticamente:  
     - **Esquerda**: Metade esquerda da imagem original.  
     - **Direita**: Metade direita da imagem original.  

   

2. **SELECIONAR PONTOS CORRESPONDENTES**  
   - **Clique na Janela Esquerda**:  
     - Selecione um ponto de interesse (ex: topo de um objeto).  
     - Coordenadas serão exibidas no terminal (ex: `Esquerda: X=320, Y=240`).  
   - **Clique na Janela Direita**:  
     - Selecione o **mesmo ponto** na perspectiva direita.  
     - Coordenadas serão exibidas no terminal (ex: `Direita: X=300, Y=240`).  

3. **CALCULAR A DISTÂNCIA**  
   - Pressione a tecla **`C`** no teclado.  
   - O resultado será exibido no terminal (ex: `Distância calculada: 7.50 metros`).  

4. **REINICIAR OU SAIR**  
   - Para novo cálculo:  
     - Clique em novos pontos e pressione **`C`** novamente.  
   - Para sair:  
     - Pressione a tecla **`Q`**.  

---

#### **EXEMPLO PRÁTICO**  
**Objetivo**: Calcular a distância até o topo de um cone.  
1. Clique no topo do cone na janela **Esquerda**.  
2. Clique no mesmo topo do cone na janela **Direita**.  
3. Pressione **`C`**:  
   ```  
   Distância calculada: 7.50 metros  
   ```  

---

#### **NOTAS IMPORTANTES**  
- **Precisão**:  
  - Clique exatamente no mesmo ponto nas duas janelas.  
  - Valores de `B` e `λ` já estão configurados – não altere a menos que saiba o que está fazendo.  
- **Conversão de Pixels para Metros**:  
  - O programa faz automaticamente usando o fator `F = 0.004125`.  

---

#### **SOLUÇÃO DE PROBLEMAS**  
| Problema               | Solução                          |  
|-------------------------|----------------------------------|  
| Imagem não carrega      | Verifique o caminho no código.   |  
| Resultado incoerente    | Clique em pontos correspondentes.|  
| Valor de `B` incorreto  | Ajuste-o diretamente no código.  |  

--- 

✌️ **Pronto! Agora você pode medir distâncias em suas imagens estereoscópicas de forma rápida.**
