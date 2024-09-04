def read_txt():
    product_array = []

    # Read the file line by line
    with open('products.txt', 'r') as file:
        for line in file:
            # Split the line into components using commas and strip whitespace
            product_id = 1
            components = [part.strip() for part in line.split(',')]

            # Extract the relevant information
            product_name = components[0]
            brand = components[1]
            price = components[2]
            price=price.replace('$','')
            quantity = components[3]
            product_id=product_id+1

            # Create an array with the extracted information
            product_info = [product_id, product_name, brand, price, quantity]

            # Append the product_info array to the product_array
            product_array.append(product_info)
            
    return (product_array)

read_txt()
