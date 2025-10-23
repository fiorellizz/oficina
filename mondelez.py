# ============================================================
# 📊 OFICINA DE ANÁLISE DE DADOS EMPRESARIAL - MÓDULO INICIAL
# ============================================================

# Bibliotecas principais
import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------------------------------------
# 1️⃣ CARREGANDO A BASE
# ------------------------------------------------------------
# Aqui você deve colocar o nome do seu arquivo CSV gerado
df = pd.read_csv("vendas_mondelez.csv", encoding="latin1", delimiter=";")

# 🔧 Ajusta valores numéricos
df["VALOR_UNIT"] = df["VALOR_UNIT"].str.replace(",", ".").astype(float)
df["VALOR_TOTAL"] = df["VALOR_TOTAL"].str.replace(",", ".").astype(float)

# Mostra as 5 primeiras linhas para conhecer a estrutura
print("\n🔍 Visualizando a base de dados:")
print(df.head())

# ------------------------------------------------------------
# 2️⃣ ENTENDENDO A ESTRUTURA DA BASE
# ------------------------------------------------------------
print("\n📦 Informações gerais:")
print(df.info())

print("\n📊 Estatísticas básicas:")
print(df.describe())

# Quantas linhas e colunas tem
print(f"\n📏 Total de linhas: {len(df)} | Total de colunas: {len(df.columns)}")

# ------------------------------------------------------------
# 3️⃣ AJUSTANDO TIPOS DE DADOS
# ------------------------------------------------------------
# Converter a coluna DATA para o tipo datetime
df["DATA"] = pd.to_datetime(df["DATA"], dayfirst=True, errors="coerce")

# Criar colunas auxiliares para análises temporais
df["ANO"] = df["DATA"].dt.year
df["MES"] = df["DATA"].dt.month_name()

# ------------------------------------------------------------
# 4️⃣ ANÁLISE GERAL DE VENDAS
# ------------------------------------------------------------
# Receita total, quantidade e ticket médio
receita_total = df["VALOR_TOTAL"].sum()
qtd_total = df["QTD"].sum()
ticket_medio = receita_total / qtd_total

print("\n💰 Métricas gerais:")
print(f"Receita total: R$ {receita_total:,.2f}")
print(f"Quantidade total vendida: {qtd_total:,}")
print(f"Ticket médio: R$ {ticket_medio:,.2f}")

# ------------------------------------------------------------
# 5️⃣ ANÁLISE ANUAL
# ------------------------------------------------------------
receita_por_ano = df.groupby("ANO")["VALOR_TOTAL"].sum()

print("\n📆 Receita total por ano:")
print(receita_por_ano)

# Gráfico de barras da receita por ano
receita_por_ano.plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Receita Total por Ano")
plt.ylabel("Valor em R$")
plt.xlabel("Ano")
plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.show()

# ------------------------------------------------------------
# 6️⃣ ANÁLISE MENSAL (EVOLUÇÃO AO LONGO DO TEMPO)
# ------------------------------------------------------------
df["MES_NUM"] = df["DATA"].dt.month
receita_mensal = df.groupby(["ANO", "MES_NUM"])["VALOR_TOTAL"].sum().reset_index()

# Gráfico de linha de evolução mensal
for ano in receita_mensal["ANO"].unique():
    dados_ano = receita_mensal[receita_mensal["ANO"] == ano]
    plt.plot(dados_ano["MES_NUM"], dados_ano["VALOR_TOTAL"], marker="o", label=str(ano))

plt.title("Evolução Mensal da Receita")
plt.xlabel("Mês")
plt.ylabel("Receita (R$)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()

# ------------------------------------------------------------
# 7️⃣ ANÁLISE POR PRODUTO
# ------------------------------------------------------------
# Top 10 produtos por receita
top_produtos = df.groupby("DESCRICAO")["VALOR_TOTAL"].sum().sort_values(ascending=False).head(10)
print("\n🏆 Top 10 produtos mais vendidos (por receita):")
print(top_produtos)

top_produtos.plot(kind="bar", color="orange", edgecolor="black")
plt.title("Top 10 Produtos por Receita")
plt.ylabel("Receita (R$)")
plt.xlabel("Produto")
plt.xticks(rotation=45, ha="right")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.show()

# ------------------------------------------------------------
# 8️⃣ ANÁLISE POR CATEGORIA
# ------------------------------------------------------------
categoria_receita = df.groupby("CATEGORIA")["VALOR_TOTAL"].sum().sort_values(ascending=False)

plt.pie(
    categoria_receita,
    labels=categoria_receita.index,
    autopct="%1.1f%%",
    startangle=90,
    colors=["gold", "lightcoral", "skyblue", "lightgreen", "violet"]
)
plt.title("Distribuição de Receita por Categoria")
plt.show()

# ------------------------------------------------------------
# 9️⃣ ANÁLISE POR VENDEDOR
# ------------------------------------------------------------
top_vendedores = df.groupby("VENDEDOR")["VALOR_TOTAL"].sum().sort_values(ascending=False)

plt.bar(top_vendedores.index, top_vendedores.values, color="lightseagreen", edgecolor="black")
plt.title("Receita Total por Vendedor")
plt.ylabel("Valor em R$")
plt.xticks(rotation=45, ha="right")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.show()

# ------------------------------------------------------------
# 🔟 ANÁLISE POR LOCAL (CIDADE)
# ------------------------------------------------------------
top_locais = df.groupby("LOCAL")["VALOR_TOTAL"].sum().sort_values(ascending=False)

plt.bar(top_locais.index, top_locais.values, color="mediumpurple", edgecolor="black")
plt.title("Receita Total por Local de Venda")
plt.ylabel("Valor em R$")
plt.xticks(rotation=45, ha="right")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.show()

# ------------------------------------------------------------
# 1️⃣2️⃣ CONCLUSÕES RÁPIDAS
# ------------------------------------------------------------
print("\n📈 Conclusões rápidas:")
print("- Há crescimento de receita de 2024 para 2025 (ver gráfico anual).")
print("- Chocolates dominam a receita total.")
print("- Alguns vendedores concentram a maior parte das vendas.")
print("- As cidades maiores (SP, RJ, BH) tendem a ter mais faturamento.")
print("- O ticket médio e volume de vendas podem ser monitorados mensalmente.")