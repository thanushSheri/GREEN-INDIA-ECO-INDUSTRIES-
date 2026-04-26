from flask import Flask, render_template
import os

app = Flask(__name__)

# Full Database of Eco-Friendly Products
products_data = {
    'u-cut-bag': {
        'name': 'U-Cut Shape Carry Bag',
        'images': ['bag-side.jpg', 'bag-sizes.jpg', 'bag-front.jpg', 'bag-chart.jpg'],
        'stock': True,
        'desc': [
            "🌱 100% Biodegradable Corn Starch",
            "💪 Load Capacity: 500g to 15kg",
            "📏 Thickness: 40 - 50 Microns",
            "✅ Fully Compostable & Eco-Friendly"
        ]
    },
    'neem-brush': {
        'name': 'Natural Neem Toothbrush',
        'images': ['neem_brush.jpg','neem-brush-trio.jpg','neem-brush-side.jpg'],
        'stock': True,
        'desc': [
            "Handcrafted from medicinal neem wood.",
            "Naturally anti-bacterial and anti-fungal.",
            "Soft bristles for gentle gum care.",
            "100% plastic-free and biodegradable."
        ]
    },
    'neem-comb': {
        'name': 'Handcrafted Neem Wood Comb',
        'images': ['neem_comb.jpg','neem-comb-real.jpg','neem-comb-info.jpg','neem-comb-packaging.jpg'],
        'stock': True,
        'desc': [
            "Made from 100% natural young neem wood.",
            "Helps reduce dandruff and scalp itchiness.",
            "Static-free combing to prevent hair breakage.",
            "Polished finish with no chemicals."
        ]
    },
    'wooden-pen': {
        'name': 'Sustainable Wooden Pen',
        'images': ['wooden_pen.jpg','pen.jpg','pen-box.jpg'],
        'stock': True,
        'desc': [
            "Elegant body made from recycled wood.",
            "Refillable ink to reduce single-use plastic.",
            "Smooth grip for comfortable writing.",
            "Perfect for eco-conscious gifting."
        ]
    },
    'wooden-bottle': {
        'name': 'Handcrafted Wooden Water Bottle',
        'images': ['wooden bottle(4).jpg','wooden_bottle(2).jpg','wooden_bottle.jpg','wooden_bottle(3).jpg'],
        'stock': True,
        'desc': [
            "Natural insulation keeps water cool.",
            "Leak-proof cap with food-grade lining.",
            "Chemical-free and BPA-free.",
            "Unique wood grain pattern on every bottle."
        ]
    },
    'bamboo-tongue-cleaner': {
        'name': 'Bamboo Tongue Cleaner',
        'images': ['bamboo_cleaner.jpg','bamboo_cleaner(1).jpg','bamboo_cleaner2.jpg'],
        'stock': True,
        'desc': [
            "Pure bamboo construction — no plastic.",
            "Ergonomic design for effective cleaning.",
            "Naturally antimicrobial and water-resistant.",
            "Compostable at the end of its life."
        ]
    },
    'wooden-coffee-cup': {
        'name': 'Eco-Friendly Wooden Coffee Cup',
        'images': ['wooden_cup.jpg','wooden_cup2.jpg','wooden_cup1.jpg'],
        'stock': True,
        'desc': [
            "Carved from durable, heat-resistant wood.",
            "Lightweight and perfect for travel.",
            "Zero plastic or wax coating.",
            "Enhances the natural aroma of your coffee."
        ]
    },
    'coconut-scrubber': {
        'name': 'Natural Coconut Fiber Scrubber',
        'images': ['coconut_scrubber.jpg','coconut_scrubber1.jpg','coconut_scrubber2.jpg',],
        'stock': True,
        'desc': [
            "Tough on stains, gentle on your pans.",
            "Made from 100% natural coconut coir.",
            "Naturally grease-resistant and odor-free.",
            "Dries quickly to prevent bacteria growth."
        ]
    },
    'jute-body-scrubber': {
        'name': 'Exfoliating Jute Body Scrubber',
        'images': ['jute_scrubber.jpg', 'jute_scrubber1.jpg', 'jute_scrubber3.jpg'],
        'stock': True,
        'desc': [
            "Hand-woven natural jute fibers.",
            "Perfect for deep skin exfoliation.",
            "Stimulates blood circulation naturally.",
            "Durable and plastic-free bathing accessory."
        ]
    },
    'paper-pouches': {
        'name': 'Eco-Friendly Paper Pouches',
        'images': ['paper_pouches.jpg', 'paper_pouches1.jpg', 'paper_pouches2.jpg'],
        'stock': True,
        'desc': [
            "High-quality recycled Kraft paper.",
            "Food-safe and perfect for dry snacks.",
            "Strong seams to prevent tearing.",
            "Fully recyclable and compostable."
        ]
    }
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/mission')
def mission():
    return render_template('mission.html')

@app.route('/products')
def products():
    # We pass products_data here so products.html can loop through it
    return render_template('products.html', products_data=products_data)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/product/<item_id>')
def product_detail(item_id):
    # This finds the specific item (like 'u-cut-bag') from the list above
    product = products_data.get(item_id.lower())
    
    if not product:
        return "<h1>Product Not Found</h1><p>Please return to the <a href='/products'>shop</a>.</p>", 404

    # We pass the found product 'p' to the detail template
    return render_template('product_detail.html', p=product)

if __name__ == '__main__':
    # This handles both local hosting and server deployment (like Heroku or Render)
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
    