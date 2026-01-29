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
    {"day": 20, "product_a": 210, "product_b": 57, "product_c": 324},
    {"day": 19, "product_a": 229, "product_b": 133, "product_c": 241},
]

def total_sales_by_product(data, product_key):
    total_sales = 0

    for i in range(len(data)):
        total_sales += data[i][product_key]

    return total_sales

    

def average_daily_sales(data, product_key):
    total_sales = 0

    for i in range(len(data)):
        total_sales += data[i][product_key]

    avg_sales = total_sales / len(data)

    return avg_sales



def best_selling_day(data):
    # defining variables to keep track of the maximum sales and the corresponding day
    total_sale_max = 0
    best_day = 0

    # for loop to iterate through each day's sales data
    for i in range(len(data)):

        # calculating total sales for the day by summing sales of all products
        total_sales = data[i]["product_a"] + data[i]["product_b"] + data[i]["product_c"]

        if total_sales > total_sale_max:
            total_sale_max = total_sales
            best_day = data[i]["day"]

    return best_day


def days_above_threshold(data, product_key, threshold):
    
    days_above = 0

    # for loop to iterate through each day's sales data
    for i in range(len(data)):
        if data[i][product_key] > threshold:
            days_above += 1

    return days_above


def top_product(data):
    
    a_sales = total_sales_by_product(data, "product_a")
    b_sales = total_sales_by_product(data, "product_b")
    c_sales = total_sales_by_product(data, "product_c")

    if a_sales > b_sales and a_sales > c_sales:
        return "product_a"
    elif b_sales > a_sales and b_sales > c_sales:
        return "product_b"
    else:
        return "product_c"
    


def worst_selling_day(data):
    # defining variables to keep track of the minimum sales and the corresponding day
    total_sale_min = float('inf')
    worst_day = 0

    # for loop to iterate through each day's sales data
    for i in range(len(data)):

        # calculating total sales for the day by summing sales of all products
        total_sales = data[i]["product_a"] + data[i]["product_b"] + data[i]["product_c"]

        if total_sales < total_sale_min:
            total_sale_min = total_sales
            worst_day = i

    return worst_day

# we already have a function to calculate the top selling day. Now, we can find that day, and "pop" it, then rerun the function twice more
def show_top_three(data):

    data_copy = data.copy()
    top_days = []

    for i in range(3):
        best_day_index = best_selling_day(data_copy)
        top_days.append(best_day_index)
        data_copy.pop(best_day_index)

    return top_days


def get_range(data, product_key):

    min_sales = float('inf')
    max_sales = 0

    for i in range(len(data)):
        sales = data[i][product_key]

        if sales < min_sales:
            min_sales = sales
        if sales > max_sales:
            max_sales = sales

    range = max_sales - min_sales
    return range

# # Function tests
print("Total sales of product_a:", total_sales_by_product(sales_data, "product_a"))
print("Average daily sales of product_b:", average_daily_sales(sales_data, "product_b"))
print("Day with highest total sales:", best_selling_day(sales_data))
print("Days when product_c exceeded 300 sales:", days_above_threshold(sales_data, "product_c", 300))
print("Product with highest total sales:", top_product(sales_data))
print("Top Three Selling Days:", show_top_three(sales_data))


