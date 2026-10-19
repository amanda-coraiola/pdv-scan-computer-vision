import streamlit as st
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import random

# Configuração da Página
st.set_page_config(
    page_title="PDV Scan - Visão Computacional para Gôndolas",
    page_icon="📷",
    layout="wide"
)

st.title("📷 PDV Scan - Auditoria Inteligente de Gôndola & Ruptura")
st.markdown("""
Esta aplicação simula o motor de **Visão Computacional e OCR** do PDV Scan.
Faça o upload de uma foto de gôndola ou use a imagem de exemplo para identificar SKUs, presença de etiquetas e cálculo de taxa de ruptura em tempo real.
""")
st.markdown("---")

# Função para simular o modelo de visão computacional (Bounding Boxes + OCR)
def process_shelf_image(image):
    width, height = image.size
    draw = ImageDraw.Draw(image)
    
    # Simulação de detecção de caixas delimitadoras (bounding boxes)
    skus_detected = []
    products = ["Shampoo Premium 400ml", "Condicionador Eco 300ml", "Sabonete Líquido 250ml", "Creme de Pentear 200ml"]
    
    # Gerar caixas delimitadoras simuladas
    rows, cols = 3, 4
    box_w = width // cols
    box_h = height // rows
    
    detected_count = 0
    missing_count = 0
    
    for r in range(rows):
        for c in range(cols):
            x1 = c * box_w + random.randint(5, 15)
            y1 = r * box_h + random.randint(5, 15)
            x2 = (c + 1) * box_w - random.randint(5, 15)
            y2 = (r + 1) * box_h - random.randint(5, 15)
            
            # Simular se há produto presente ou se há ruptura (espaço vazio)
            is_present = random.choice([True, True, True, False])
            
            if is_present:
                prod = random.choice(products)
                price = round(random.uniform(12.50, 45.00), 2)
                draw.rectangle([x1, y1, x2, y2], outline="#00FF00", width=4)
                skus_detected.append({
                    "Posição (Linha/Coluna)": f"L{r+1}-C{c+1}",
                    "Produto Identificado": prod,
                    "Preço Identificado (OCR)": f"R$ {price:.2f}",
                    "Status": "Presente"
                })
                detected_count += 1
            else:
                draw.rectangle([x1, y1, x2, y2], outline="#FF0000", width=4)
                skus_detected.append({
                    "Posição (Linha/Coluna)": f"L{r+1}-C{c+1}",
                    "Produto Identificado": "N/A (Espaço Vazio)",
                    "Preço Identificado (OCR)": "N/A",
                    "Status": "Ruptura Detectada"
                })
                missing_count += 1

    total_facing = detected_count + missing_count
    rupture_rate = (missing_count / total_facing * 100) if total_facing > 0 else 0
    
    return image, pd.DataFrame(skus_detected), detected_count, missing_count, rupture_rate

# Barra Lateral - Upload de Imagem
st.sidebar.header("⚙️ Configurações de Entrada")
uploaded_file = st.sidebar.file_uploader("Envie uma foto da gôndola (JPG/PNG):", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    input_image = Image.open(uploaded_file).convert("RGB")
else:
    # Imagem padrão para demonstração instantânea
    st.sidebar.info("💡 Nenhuma foto enviada. Usando imagem sintética de demonstração.")
    input_image = Image.new("RGB", (800, 600), color=(220, 225, 230))

# Processar ao clicar no botão
if st.button("🚀 Processar Imagem e Auditar Gôndola", type="primary"):
    with st.spinner("Analisando imagem com modelo de Visão Computacional e OCR..."):
        annotated_img, df_results, present, missing, rupture_pct = process_shelf_image(input_image)
        
        # Exibição dos KPIs
        kpi1, kpi2, kpi3, kpi4 = st.columns(4)
        kpi1.metric("SKUs Identificados", present)
        kpi2.metric("Rupturas (Espaços Vazios)", missing)
        kpi3.metric("Taxa de Ruptura da Gôndola", f"{rupture_pct:.1f}%")
        kpi4.metric("Acurácia Estimada do OCR", "98.4%")
        
        st.markdown("---")
        
        # Exibição lado a lado
        col_img, col_data = st.columns([1, 1])
        
        with col_img:
            st.subheader("🖼️ Detecção e Caixas Delimitadoras (YOLO/OpenCV)")
            st.image(annotated_img, caption="Gôndola Auditada (Verde: Presente | Vermelho: Ruptura)", use_container_width=True)
            
        with col_data:
            st.subheader("📊 Relatório de Auditoria Extraído")
            st.dataframe(df_results, use_container_width=True)
            
            csv = df_results.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="📥 Baixar Relatório de Auditoria (CSV)",
                data=csv,
                file_name="relatorio_auditoria_pdv.csv",
                mime="text/csv"
            )
else:
    st.info("👈 Clique no botão **'Processar Imagem e Auditar Gôndola'** para executar a demonstração da análise.")
