from flask import Flask, render_template, request
import dao

app = Flask(__name__)


@app.route('/')
def index():
    categories = dao.load_categories()
    q = request.args.get('q')
    cate_id = request.args.get('category_id')
    products = dao.load_products(q, cate_id)
    return render_template('index.html', mucluc=categories, products=products)


@app.route('/products/<int:id>')
def detail(id):
    products = dao.get_product_by_id(product_id=id)
    return render_template('product_detail.html', products=products)


if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)