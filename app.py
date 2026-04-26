from flask import Flask, render_template

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
    products_data = {
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
        },
        'kitchen-set': {
            'name': 'Sheesham Wood Kitchen Set',
            'img': 'wooden_spoons.jpg',
            'stock': True,
            'desc': [
                "Premium Sheesham wood for luxury cooking.",
                "Natural heat resistance — won't melt.",
                "Safe for non-stick pans — zero scratches.",
                "Chemical-free finish for food safety.",
                "Durable and built for daily use."
            ]
        },
        'toothbrush': {
            'name': 'Bamboo Toothbrush',
            'img': 'bamboo_toothbrush.jpg',
            'stock': True,
            'desc': [
                "100% biodegradable bamboo handle.",
                "Charcoal-infused bristles for deep cleaning.",
                "Naturally antimicrobial and water-resistant.",
                "Plastic-free, eco-friendly packaging.",
                "Reduces plastic waste in our oceans."
            ]
        },
        'carry-bag': {
            'name': 'Compostable Carry Bags',
            'img': 'carry_bag.jpg',
            'stock': True,
            'desc': [
                "Plant-based corn starch material.",
                "Fully compostable within 180 days.",
                "Highly durable and leak-proof design.",
                "Leaves zero microplastics in the soil.",
                "Certified eco-friendly for grocery use."
            ]
        },
        'garbage-liner': {
            'name': 'Bio-Garbage Liners',
            'img': 'garbage_liner.jpg',
            'stock': False,
            'desc': [
                "Eco-friendly alternative to plastic liners.",
                "Heavy-duty strength to handle wet waste.",
                "Fully decomposes in composting environments.",
                "Fits standard kitchen and office bins.",
                "Supports a zero-waste lifestyle."
            ]
        }
    }

    product = products_data.get(item_id.lower())

    if not product:
        return "<h1>Product Not Found</h1><p>Please return to the <a href='/products'>shop</a>.</p>", 404

    return render_template('product_detail.html', p=product)


if __name__ == '__main__':
    app.run(debug=True)