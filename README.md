# 📷 PDV Scan - Computer Vision & Shelf Analytics

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://pdv-scan-computer-vision.streamlit.app/)

> Protótipo funcional de Visão Computacional e OCR aplicado à auditoria automatizada de gôndolas no varejo, reduzindo erros manuais e identificando rupturas de estoque em tempo real.

---

## 🎯 Sobre o Projeto
Inspirado na solução de automação **PDV Scan**, este projeto demonstra como técnicas de processamento de imagem, reconhecimento de objetos e extracção de texto (OCR) podem transformar a auditoria de trade marketing no ponto de venda.

A ferramenta permite o envio de imagens de prateleiras/gôndolas, desenha as caixas delimitadoras (*Bounding Boxes*) nos produtos e etiquetas e calcula instantaneamente indicadores de presença e rupturas.

---

## 🛠️ Tecnologias Utilizadas
* **Python**: Linguagem principal.
* **Streamlit**: Interface web interativa para testes e demonstrações do motor de visão.
* **Pillow (PIL) & Pandas**: Processamento de imagens, manipulação matricial e relatórios tabulares.
* **Streamlit Cloud**: Deploy e hospedagem contínua.

---

## 🚀 Como Funciona
1. **Upload / Entrada de Imagem:** Envio da fotografia tirada pela equipa de campo no PDV.
2. **Processamento & Detecção:** Identificação automatizada das posições dos produtos e espaços vazios.
3. **Extração OCR de Etiquetas:** Leitura simulada de preços e SKUs nas etiquetas de gôndola.
4. **Geração do KPI de Ruptura:** Cálculo automático da % de ruptura e exportação do relatório em CSV.

---
*Desenvolvido por [Amanda Coraiola](https://github.com/amanda-coraiola).*
