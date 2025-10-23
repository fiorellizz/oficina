# ============================================================
# 🚗 OFICINA DE ANÁLISE DE DADOS EMPRESARIAL - VENDAS DE CARROS
# ============================================================

# Bibliotecas principais
import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------------------------------------
# 1️⃣ CARREGANDO A BASE
# ------------------------------------------------------------
# Aqui você deve colocar o nome do arquivo CSV gerado anteriormente
df = pd.read_csv("vendas_carros.csv", encoding="latin1", delimiter=";")

# 🔧 Ajusta valores numéricos
df["VALOR_UNIT"] = df["VALOR_UNIT"].str.replace(",", ".").astype(float)
df["VALOR_TOTAL"] = df["VALOR_TOTAL"].str.replace(",", ".").astype(float)

# Visualiza as primeiras linhas
print("\n🔍 Visualizando a base de dados:")
print(df.head())

# ------------------------------------------------------------
# 2️⃣ ENTENDENDO A ESTRUTURA DA BASE
# ------------------------------------------------------------
print("\n📦 Informações gerais:")
print(df.info())

print("\n📊 Estatísticas básicas:")
print(df.describe())

print(f"\n📏 Total de linhas: {len(df)} | Total de colunas: {len(df.columns)}")

# ------------------------------------------------------------
# 3️⃣ AJUSTANDO TIPOS DE DADOS
# ------------------------------------------------------------
df["DATA"] = pd.to_datetime(df["DATA"], dayfirst=True, errors="coerce")
df["ANO"] = df["DATA"].dt.year
df["MES"] = df["DATA"].dt.month_name()

# ------------------------------------------------------------
# 4️⃣ ANÁLISE GERAL DE VENDAS
# ------------------------------------------------------------
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

receita_por_ano.plot(kind="bar", color="lightblue", edgecolor="black")
plt.title("Receita Total por Ano")
plt.ylabel("Valor em R$")
plt.xlabel("Ano")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.show()

# ------------------------------------------------------------
# 6️⃣ EVOLUÇÃO MENSAL DA RECEITA
# ------------------------------------------------------------
df["MES_NUM"] = df["DATA"].dt.month
receita_mensal = df.groupby(["ANO", "MES_NUM"])["VALOR_TOTAL"].sum().reset_index()

for ano in receita_mensal["ANO"].unique():
    dados_ano = receita_mensal[receita_mensal["ANO"] == ano]
    plt.plot(dados_ano["MES_NUM"], dados_ano["VALOR_TOTAL"], marker="o", label=str(ano))

plt.title("📈 Evolução Mensal da Receita")
plt.xlabel("Mês")
plt.ylabel("Receita (R$)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()

# ------------------------------------------------------------
# 7️⃣ ANÁLISE POR MODELO DE CARRO
# ------------------------------------------------------------
top_modelos = df.groupby("MODELO")["VALOR_TOTAL"].sum().sort_values(ascending=False).head(10)

print("\n🏆 Top 10 modelos mais vendidos (por receita):")
print(top_modelos)

top_modelos.plot(kind="bar", color="orange", edgecolor="black")
plt.title("Top 10 Modelos de Carros por Receita")
plt.ylabel("Receita (R$)")
plt.xlabel("Modelo")
plt.xticks(rotation=45, ha="right")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.show()

# ------------------------------------------------------------
# 8️⃣ ANÁLISE POR MODELO
# ------------------------------------------------------------
modelo_receita = df.groupby("MODELO")["VALOR_TOTAL"].sum().sort_values(ascending=False)

plt.pie(
    modelo_receita,
    labels=modelo_receita.index,
    autopct="%1.1f%%",
    startangle=90,
    colors=["gold", "skyblue", "lightcoral", "lightgreen", "violet", "salmon"]
)
plt.title("Distribuição de Receita por Modelo")
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
# 🔟 ANÁLISE POR CONCESSIONARIA
# ------------------------------------------------------------
top_concessionarias = df.groupby("CONCESSIONARIA")["VALOR_TOTAL"].sum().sort_values(ascending=False)

plt.bar(top_concessionarias.index, top_concessionarias.values, color="mediumpurple", edgecolor="black")
plt.title("Receita Total por Concessionaria")
plt.ylabel("Valor em R$")
plt.xticks(rotation=45, ha="right")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.show()

# ------------------------------------------------------------
# 1️⃣1️⃣ TICKET MÉDIO POR MODELO
# ------------------------------------------------------------
ticket_por_modelo = (df.groupby("MODELO")["VALOR_TOTAL"].sum() /
                     df.groupby("MODELO")["QTD"].sum()).sort_values(ascending=False).head(10)

ticket_por_modelo.plot(kind="bar", color="steelblue", edgecolor="black")
plt.title("Ticket Médio por Modelo (Top 10)")
plt.ylabel("Ticket Médio (R$)")
plt.xlabel("Modelo")
plt.xticks(rotation=45, ha="right")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.show()

# ------------------------------------------------------------
# 1️⃣2️⃣ CONCLUSÕES RÁPIDAS
# ------------------------------------------------------------
print("\n📈 Conclusões rápidas:")
print("- Há crescimento de receita entre os anos (ver gráfico anual).")
print("- Alguns modelos dominam o faturamento total (ver gráfico de pizza).")
print("- Os vendedores top representam grande parte das vendas.")
print("- As Concessionarias maiores concentram a maior parte da receita.")
print("- O ticket médio varia bastante entre modelos de carro.")
