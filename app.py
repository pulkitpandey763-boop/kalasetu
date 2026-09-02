from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Aapke project ke real craft products
    products = [
        {
            'title': 'MITHILA TREE OF LIFE & SACRED KOHBAR',
            'artist': 'Smt. Mahasundari Devi',
            'state': 'Bihar',
            'category': 'Painting & Folk Art',
            'desc': 'Authentic GI-certified Madhubani painting made with natural dyes.',
            'price': '3,400',
            'old_price': '8,500',
            'days': '14',
            'image': 'https://images.unsplash.com/photo-1579783900882-c0d3dad7b119?w=500'
        },
        {
            'title': 'TALAPATRA PALM LEAF DASHAVATARA',
            'artist': 'Shri Raghunath Mohapatra Guild',
            'state': 'Odisha',
            'category': 'Painting & Folk Art',
            'desc': 'Exquisite hand-etched Talapatra Pattachitra palm-leaf scroll.',
            'price': '4,600',
            'old_price': '11,500',
            'days': '21',
            'image': 'https://images.unsplash.com/photo-1579783902614-a3fb3927b675?w=500'
        },
        {
            'title': 'ROYAL BANARASI KADWA SILK SAREE',
            'artist': 'Ustad Ghulam Mohammad',
            'state': 'Varanasi, UP',
            'category': 'Handloom & Textiles',
            'desc': 'Hand-woven pure silk saree with real gold zari motifs.',
            'price': '12,500',
            'old_price': '28,000',
            'days': '45',
            'image': 'https://images.unsplash.com/photo-1610030469983-98e550d6193c?w=500'
        },
        {
            'title': 'BLUE POTTERY DECORATIVE VASE',
            'artist': 'Kripal Kumbh Studio',
            'state': 'Jaipur, Rajasthan',
            'category': 'Terracotta & Pottery',
            'desc': 'Traditional quartz glass hand-painted Jaipur blue pottery.',
            'price': '1,850',
            'old_price': '4,200',
            'days': '8',
            'image': 'https://images.unsplash.com/photo-1578749556568-bc2c40e68b61?w=500'
        }
    ]
    return render_template('index.html', products=products)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)