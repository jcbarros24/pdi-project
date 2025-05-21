
# Projeto de Restauração de Imagens — PDI

Este projeto aplica filtros de restauração (mediana, gaussiano, bilateral e iterativo) em uma imagem com ruído utilizando a biblioteca OpenCV.

---

### 1. clonar o projeto 

```bash
git clone <link-do-repositorio>
cd PDI
```

### 2. Criar o ambiente virtual

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar as dependencias

```bash
pip install -r requirements.txt
```

### Executar

```bash
python restauracao.py
```

---

## 🧪 Requisitos

- Python 3.7 ou superior
- OpenCV
- Matplotlib

---

## 🧼 Saída esperada

Ao rodar o script, será exibida uma janela com as comparações entre os seguintes filtros aplicados:

- Imagem original com ruído
- Filtro da mediana (5x5)
- Filtro gaussiano (5x5)
- Filtro bilateral
- Mediana iterativa

---

## obs

- Certificar de que a imagem `ruido.jpeg` está dentro da pasta `imagens`.
- O ambiente virtual (`venv/`) **não deve ser enviado para o repositório** (ele é gerado localmente).

--
