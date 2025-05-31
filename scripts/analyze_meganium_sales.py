import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar dados
df = pd.read_csv("Meganium_Sales_Data.csv")

# Calcular total por produto
popular_products = df.groupby("product_sold")["quantity"].sum().sort_values(ascending=False)
top_selling_product = df.groupby("product_sold")["total_price"].sum().sort_values(ascending=False)

# Idade dos compradores
df["buyer_birth_date"] = pd.to_datetime(df["buyer_birth_date"], errors='coerce')
df["buyer_age"] = pd.to_datetime("today").year - df["buyer_birth_date"].dt.year
average_age = df["buyer_age"].mean()

# Estilo gráfico
sns.set(style="whitegrid")

# Gráfico 1: Produtos mais populares
plt.figure(figsize=(10, 6))
popular_products.plot(kind='bar', color='skyblue')
plt.title("Produtos Mais Populares (Quantidade Vendida)")
plt.xlabel("Produto")
plt.ylabel("Quantidade Vendida")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("produtos_mais_populares.png")

# Gráfico 2: Produtos com maior valor de venda
plt.figure(figsize=(10, 6))
top_selling_product.plot(kind='bar', color='salmon')
plt.title("Produtos com Maior Valor de Venda")
plt.xlabel("Produto")
plt.ylabel("Valor Total (€)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("produtos_lider_valor.png")

# Gráfico 3: Idade dos compradores
plt.figure(figsize=(8, 6))
sns.histplot(df["buyer_age"].dropna(), bins=10, kde=True, color='mediumseagreen')
plt.title("Distribuição de Idade dos Compradores")
plt.xlabel("Idade")
plt.ylabel("Frequência")
plt.tight_layout()
plt.savefig("distribuicao_idade_compradores.png")

# Exibir insights no terminal
print("Produtos mais populares:\n", popular_products, "\n")
print("Produtos com maior valor vendido:\n", top_selling_product, "\n")
print(f"Idade média dos compradores: {average_age:.2f} anos")
