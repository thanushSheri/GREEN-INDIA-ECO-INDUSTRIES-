from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/mission')
def mission():
    return render_template('mission.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/product/<item_id>')
def product_detail(item_id):
    # UPDATED: Added u-cut-bag and matched your preferred descriptions
    products_data = {
        'u-cut-bag': {
            'name': 'U-Cut Shape Carry Bag',
            'img': 'bag-front.jpg', # Requested front image
            'stock': True,
            'desc': [
                "🌱 100% Biodegradable Corn Starch",
                "💪 Load Capacity: 500g to 15kg",
                "📏 Thickness: 40 - 50 Microns",
                "✅ Fully Compostable & Eco-Friendly"
            ]
        },
        'neem-comb': {
            'name': 'Handcrafted Neem Wood Comb',
            'img': 'neem_comb.jpg',
            'stock': True,
            'desc': [
                "Made from 100% natural young neem wood.",
                "Anti-bacterial properties help reduce dandruff.",
                "Smooth teeth prevent hair breakage.",
                "Eco-friendly alternative to plastic combs.",
                "Handcrafted by local Indian artisans."
            ]
        }
        # You can keep or remove the others based on your catalog needs
    }

    product = products_data.get(item_id.lower())

    if not product:
        return "<h1>Product Not Found</h1><p>Please return to the <a href='/products'>shop</a>.</p>", 404

    return render_template('product_detail.html', p=product)

if __name__ == '__main__':
    # Combined your two run configurations for better stability
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)