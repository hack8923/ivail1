class Product:
    def __init__(self, name, weight, height, width, volume):
        self.name = name
        self.weight = weight
        self.height = height
        self.width = width
        self.volume = volume

products = [
    Product("Товар А", 10, 20, 30, 6000),
    Product("Товар B", 15, 25, 35, 8750),
    Product("Товар C", 8, 18, 28, 4704),
]

def filter_products(criteria):
    filtered_products = []
    
    for product in products:
        if (
            criteria.get('weight_min', 0) <= product.weight <= criteria.get('weight_max', float('inf')) and
            criteria.get('height_min', 0) <= product.height <= criteria.get('height_max', float('inf')) and
            criteria.get('width_min', 0) <= product.width <= criteria.get('width_max', float('inf')) and
            criteria.get('volume_min', 0) <= product.volume <= criteria.get('volume_max', float('inf'))
        ):
            filtered_products.append(product)
            
    return filtered_products

criteria = {
    'weight_min': 9,
    'weight_max': 16,
    'height_min': 19,
    'height_max': 26,
    'width_min': 29,
    'width_max': 36,
    'volume_min': 5000,
    'volume_max': 9000,
}

filtered_products = filter_products(criteria)

for product in filtered_products:
    print(f"{product.name}: Вес {product.weight}, Высота {product.height}, Ширина {product.width}, Объем {product.volume}")
