class Product:
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price  # Preço base em BRL (R$)
        self.quantity = quantity


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_out_of_stock(self):
        # Correção: filtra os produtos sem alterar a lista durante a iteração
        self.products = [p for p in self.products if p.quantity > 0]

    def update_quantity(self, product_id, amount):
        for p in self.products:
            if p.id == product_id:
                p.quantity += amount
                return True
        return False

    def converter_moeda(self, valor_brl: float, moeda_destino: str) -> float:
        """Converte um valor em BRL para USD ou EUR."""
        # Cotações de referência (1 USD = X da moeda)
        cotacoes = {
            "USD": 1.0,
            "BRL": 5.60,  # 1 USD = 5,60 BRL
            "EUR": 0.92   # 1 USD = 0,92 EUR
        }
        
        destino = moeda_destino.upper().strip()
        if destino not in cotacoes:
            raise ValueError(f"Moeda '{destino}' inválida. Use BRL, USD ou EUR.")

        # Converte BRL -> USD -> Moeda de Destino
        valor_em_usd = valor_brl / cotacoes["BRL"]
        valor_final = valor_em_usd * cotacoes[destino]
        return round(valor_final, 2)

    def calculate_total_value(self, moeda: str = "BRL") -> float:
        """Calcula o valor total do estoque na moeda especificada."""
        total_brl = sum(p.price * p.quantity for p in self.products)
        
        if moeda.upper() == "BRL":
            return round(total_brl, 2)
            
        return self.converter_moeda(total_brl, moeda)


# --- Execução do Código ---
inv = Inventory()
inv.add_product(Product(1, "Camisa", 50.0, 10))
inv.add_product(Product(2, "Calça", 100.0, 0))
inv.add_product(Product(3, "Sapato", 150.0, 0))
inv.add_product(Product(4, "Meia", 15.0, 5))

# Remove produtos fora de estoque
inv.remove_out_of_stock()

# Exibe o valor total em diferentes moedas
print(f"Total no estoque (BRL): R$ {inv.calculate_total_value('BRL'):.2f}")
print(f"Total no estoque (USD): US$ {inv.calculate_total_value('USD'):.2f}")
print(f"Total no estoque (EUR): € {inv.calculate_total_value('EUR'):.2f}")
