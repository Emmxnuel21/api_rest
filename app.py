from flask import Flask, jsonify, request

app = Flask(__name__)

from products import products

@app.route('/ping')
def ping():
    return jsonify({"message":"pong"})


@app.route('/products')
def getProducts():
    return jsonify({"products": products, "message": "Lista de productos"})

@app.route('/products/<string:product_nombre>')
def getProduct(product_nombre):
    productsFound = [product for product in products if product['nombre'] == product_nombre] 
    if (len(productsFound) > 0 ):
        return jsonify ({"product": productsFound[0]})
    return jsonify({"message": "Producto no encontrado"})

@app.route('/products', methods=['POST'])
def addProduct():
    new_product = {
        "nombre": request.json['nombre'],
        "precio": request.json['precio'],
        "cantidad": request.json['cantidad']
    }
    products.append(new_product)
    return jsonify({"message": "Prodcuto agregado!", "products": products})

@app.route('/products/<string:product_nombre>', methods=['PUT'])
def editProduct(product_nombre):
    productFound = [product for product in products if product['nombre'] == product_nombre] 
    if (len(productFound) > 0 ):
        productFound[0]['nombre'] = request.json['nombre']
        productFound[0]['precio'] = request.json['precio']
        productFound[0]['cantidad'] = request.json['cantidad']
        return jsonify({
            "message": "Producto actualizado!",
            "product": productFound[0]
        })
    return jsonify({"message": "Producto no encontrado"})

@app.route('/products/<string:product_nombre>', methods=['DELETE'])
def deleteProduct(product_nombre):
     productsFound = [product for product in products if product['nombre'] == product_nombre] 
     if len(productsFound) > 0 :
       products.remove(productsFound[0])
       return jsonify({
           "message": "Producto Eliminado!",
           "products": products
           })
     return jsonify({"message": "Producto no encontrado!"})


if __name__ == '__main__':
    app.run(debug=True)