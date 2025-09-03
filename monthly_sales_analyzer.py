# Example data
sales_data = [
    {"day": 1, "product_a": 202, "product_b": 142, "product_c": 164},
    {"day": 2, "product_a": 206, "product_b": 121, "product_c": 338},
    {"day": 3, "product_a": 120, "product_b": 152, "product_c": 271},
    {"day": 4, "product_a": 174, "product_b": 137, "product_c": 266},
    {"day": 5, "product_a": 199, "product_b": 153, "product_c": 301},
    {"day": 6, "product_a": 230, "product_b": 199, "product_c": 202},
    {"day": 7, "product_a": 101, "product_b": 137, "product_c": 307},
    {"day": 8, "product_a": 137, "product_b": 179, "product_c": 341},
    {"day": 9, "product_a": 287, "product_b": 70, "product_c": 310},
    {"day": 10, "product_a": 157, "product_b": 71, "product_c": 238},
    {"day": 11, "product_a": 148, "product_b": 108, "product_c": 319},
    {"day": 12, "product_a": 287, "product_b": 64, "product_c": 339},
    {"day": 13, "product_a": 289, "product_b": 100, "product_c": 257},
    {"day": 14, "product_a": 154, "product_b": 113, "product_c": 280},
    {"day": 15, "product_a": 150, "product_b": 184, "product_c": 170},
    {"day": 16, "product_a": 172, "product_b": 67, "product_c": 281},
    {"day": 17, "product_a": 188, "product_b": 109, "product_c": 163},
    {"day": 18, "product_a": 108, "product_b": 139, "product_c": 202},
    {"day": 19, "product_a": 229, "product_b": 133, "product_c": 241},
    {"day": 20, "product_a": 210, "product_b": 57, "product_c": 324}
]


# Calcula las ventas totales de un producto dado
def total_sales_by_product(data, product_key):
    total = 0
    for item in data:
        total += item[product_key]
    return total


# Calcula el promedio diario de ventas de un producto dado
def average_daily_sales(data, product_key):
    suma_total = total_sales_by_product(data, product_key)
    average = suma_total / len(data)
    return average


# Encuentra el dia con las ventas totales mas altas de todos los productos
def best_selling_day(data):
    max_sales = 0
    best_day = 0
    for item in data:
        total_sales = item["product_a"] + item["product_b"] + item["product_c"]
        if total_sales > max_sales:
            max_sales = total_sales
            best_day = item["day"]
    return best_day


# Cuenta cuántos días las ventas de un producto superaron un umbral dado
def days_above_threshold(data, product_key, threshold):
    conteo_dias = 0
    for item in data:
        if item[product_key] > threshold:
            conteo_dias += 1
    return conteo_dias


# Identifica qué producto (A, B o C) tuvo las ventas totales más altas
def top_product(data):
    total_sales_a = total_sales_by_product(data, "product_a")
    total_sales_b = total_sales_by_product(data, "product_b")
    total_sales_c = total_sales_by_product(data, "product_c")
    if total_sales_a >= total_sales_b and total_sales_a >= total_sales_c:
        return "product_a"
    elif total_sales_b >= total_sales_a and total_sales_b >= total_sales_c:
        return "product_b"
    else:
        return "product_c"
    

# Encuentra el dia con las peores ventas totales
def worst_selling_day(data):
    min_sales = 100000
    worst_day = 0
    for item in data:
        total_sales = item["product_a"] + item["product_b"] + item["product_c"]
        if total_sales < min_sales:
            min_sales = total_sales
            worst_day = item["day"]
    return worst_day


# Muestra los 3 mejores dias de ventas
def best_3_days(data):
    sales_per_day = []
    for item in data:
        total_sales = item["product_a"] + item["product_b"] + item["product_c"]
        sales_per_day.append((item["day"], total_sales))
    sorted_data = sorted(sales_per_day, key = lambda x: x[1])
    best_days = []
    for item in sorted_data:
        best_days.append(item[0])
    return best_days[-3:]


# Calcula el rango (máximo - mínimo) de las ventas de un producto
def sales_range(data, product_key):
    max_sales = 0
    min_sales = 10000
    for item in data:
        if item[product_key] > max_sales:
            max_sales = item[product_key]
        elif item[product_key] < min_sales:
            min_sales = item[product_key]
    return f"{max_sales} - {min_sales}"




# Function tests
print("Total sales of product_a:", total_sales_by_product(sales_data, "product_a"))
print("Average daily sales of product_b:", average_daily_sales(sales_data, "product_b"))
print("Day with highest total sales:", best_selling_day(sales_data))
print("Days when product_c exceeded 300 sales:", days_above_threshold(sales_data, "product_c", 300))
print("Product with highest total sales:", top_product(sales_data))
print("Day with lowest total sales:", worst_selling_day(sales_data))
print("Best 3 days of total sales:", best_3_days(sales_data))
print("Sales range of product_a:", sales_range(sales_data, "product_a"))