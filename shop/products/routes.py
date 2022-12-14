from ast import literal_eval

from flask import render_template, session, request, redirect, url_for, flash, current_app, make_response
from flask_login import login_required
from shop import app, db, photos, search
from .models import Category, Brand, Addproduct
from .forms import Addproducts
from ..customers.forms import CustomerLoginFrom, CustomerRegisterForm
import secrets
import os
from flask_babel import gettext
from flask_babel import _ 
from ..admin.forms import LoginForm

from ..admin.forms import LoginForm


def brands():
    brands = Brand.query.join(Addproduct, (Brand.id == Addproduct.brand_id)).all()
    return brands


def categories():
    categories = Category.query.join(Addproduct, (Category.id == Addproduct.category_id)).all()
    return categories

@app.route('/')
def home():
    loginform = CustomerLoginFrom()
    registerform = CustomerRegisterForm()
    page = request.args.get('page', 1, type=int)
    products = Addproduct.query.filter(Addproduct.stock > 0).order_by(Addproduct.id.desc()).paginate(page=page,
                                                                                                     per_page=8)
    return render_template('index.html', products=products, brands=brands(), categories=categories(), loginform=loginform, registerform=registerform)


@app.route('/result')
def result():
    searchword = request.args.get('q')
    products = Addproduct.query.msearch(searchword, fields=['name', 'desc'], limit=6)
    return render_template('products/result.html', products=products, brands=brands(), categories=categories())


@app.route('/product/<int:id>')
def single_page(id):
    product = Addproduct.query.get_or_404(id)
    resp = make_response(
        render_template('products/single_page.html', product=product, brands=brands(), categories=categories()))
    cookies = literal_eval(request.cookies.get('checked') or "[]")
    if not (id in cookies):
        cookies.append(id)
    print(cookies)
    resp.set_cookie("checked", str(cookies))
    return resp


@app.route('/brand/<int:id>')
def get_brand(id):
    page = request.args.get('page', 1, type=int)
    get_brand = Brand.query.filter_by(id=id).first_or_404()
    brand = Addproduct.query.filter_by(brand=get_brand).paginate(page=page, per_page=8)
    return render_template('products/index.html', brand=brand, brands=brands(), categories=categories(),
                           get_brand=get_brand)


@app.route('/categories/<int:id>')
def get_category(id):
    page = request.args.get('page', 1, type=int)
    get_cat = Category.query.filter_by(id=id).first_or_404()
    get_cat_prod = Addproduct.query.filter_by(category=get_cat).paginate(page=page, per_page=8)
    return render_template('products/index.html', get_cat_prod=get_cat_prod, brands=brands(), categories=categories(),
                           get_cat=get_cat)


@app.route('/gender/<string:gender>')
def get_gender(gender):
    page = request.args.get('page', 1, type=int)
    products = Addproduct.query.filter_by(gender=gender).paginate(page=page, per_page=8)
    return render_template('products/index.html', get_gen_prod=products, get_gen=gender, brands=brands(), categories=categories())



@app.route('/addbrand', methods=['GET', 'POST'])
@login_required
def addbrand():
    if request.method == "POST":
        getbrand = request.form.get('brand')
        brand = Brand(name=getbrand)
        db.session.add(brand)
        flash(f'?????????? {getbrand} ???????????????? ?? ????????', 'success')
        db.session.commit()
        return redirect(url_for('addbrand'))
    return render_template('products/addbrand.html', title='Add brand', brands='brands')


@app.route('/updatebrand/<int:id>', methods=['GET', 'POST'])
@login_required
def updatebrand(id):
    if 'email' not in session:
        flash(gettext('?????????????? ?????????????? ?? ??????????????!'), 'danger')
        return redirect(url_for('login'))
    updatebrand = Brand.query.get_or_404(id)
    brand = request.form.get('brand')
    if request.method == "POST":
        updatebrand.name = brand
        flash(f'?????????? {updatebrand.name} ?????? ?????????????? ???? {brand}', 'success')
        db.session.commit()
        return redirect(url_for('brands'))
    brand = updatebrand.name
    return render_template('products/addbrand.html', title='Udate brand', brands='brands', updatebrand=updatebrand)


@app.route('/deletebrand/<int:id>', methods=['GET', 'POST'])
@login_required
def deletebrand(id):
    brand = Brand.query.get_or_404(id)
    if request.method == "POST":
        db.session.delete(brand)
        flash(f"?????????? {brand.name} ???????????? ???? ????????", "success")
        db.session.commit()
        return redirect(url_for('admin'))
    flash(f"?????????? {brand.name} ???? ?????????? ???????? ???????????? ???? ????????", "warning")
    return redirect(url_for('admin'))


@app.route('/addcat', methods=['GET', 'POST'])
@login_required
def addcat():
    if request.method == "POST":
        getcat = request.form.get('category')
        category = Category(name=getcat)
        db.session.add(category)
        flash(f'?????????? {getcat} ?????? ?????????????? ???????????????? ?? ????????', 'success')
        db.session.commit()
        return redirect(url_for('addcat'))
    return render_template('products/addbrand.html', title='Add category')


@app.route('/updatecat/<int:id>', methods=['GET', 'POST'])
@login_required
def updatecat(id):
    if 'email' not in session:
        flash('Login first please', 'danger')
        return redirect(url_for('login'))
    updatecat = Category.query.get_or_404(id)
    category = request.form.get('category')
    if request.method == "POST":
        updatecat.name = category
        flash(f'?????????????????? {updatecat.name} ???????? ?????????????? ???????????????? ???? {category}', 'success')
        db.session.commit()
        return redirect(url_for('categories'))
    category = updatecat.name
    return render_template('products/addbrand.html', title='Update cat', updatecat=updatecat)


@app.route('/deletecat/<int:id>', methods=['GET', 'POST'])
@login_required
def deletecat(id):
    category = Category.query.get_or_404(id)
    if request.method == "POST":
        db.session.delete(category)
        flash(f"?????????? {category.name} ?????? ???????????? ???? ????????", "success")
        db.session.commit()
        return redirect(url_for('admin'))
    flash(f"?????????? {category.name} ???? ?????????? ???????? ???????????? ???? ????????", "warning")
    return redirect(url_for('admin'))


@app.route('/addproduct', methods=['GET', 'POST'])
@login_required
def addproduct():
    form = Addproducts(request.form)
    brands = Brand.query.all()
    categories = Category.query.all()
    if request.method == "POST" and 'image_1' in request.files:
        name = form.name.data
        price = form.price.data
        discount = form.discount.data
        stock = form.stock.data
        colors = form.colors.data
        desc = form.discription.data
        gender = form.gender.data
        brand = request.form.get('brand')
        category = request.form.get('category')
        image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + ".")
        image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + ".")
        image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + ".")
        addproduct = Addproduct(name=name, price=price, discount=discount, stock=stock, colors=colors, desc=desc,
                                category_id=category, brand_id=brand, image_1=image_1, image_2=image_2, image_3=image_3,
                                gender=gender)
        db.session.add(addproduct)
        flash(f'?????????????? {name} ?????? ???????????????? ?? ????????', 'success')
        db.session.commit()
        return redirect(url_for('admin'))
    return render_template('products/addproduct.html', form=form, title='Add a Product', brands=brands,
                           categories=categories)


@app.route('/updateproduct/<int:id>', methods=['GET', 'POST'])
@login_required
def updateproduct(id):
    form = Addproducts(request.form)
    product = Addproduct.query.get_or_404(id)
    brands = Brand.query.all()
    categories = Category.query.all()
    brand = request.form.get('brand')
    category = request.form.get('category')
    gender = request.form.get('gender')
    size = request.form.get('size')
    if request.method == "POST":
        product.name = form.name.data
        product.price = form.price.data
        product.discount = form.discount.data
        product.stock = form.stock.data
        product.colors = form.colors.data
        product.desc = form.discription.data
        product.category_id = category
        product.brand_id = brand
        product.gender = gender
        product.size = size
        if request.files.get('image_1'):
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_1))
                product.image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + ".")
            except:
                product.image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + ".")
        if request.files.get('image_2'):
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_2))
                product.image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + ".")
            except:
                product.image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + ".")
        if request.files.get('image_3'):
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_3))
                product.image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + ".")
            except:
                product.image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + ".")

        flash('?????????????? ?????? ?????????????? ????????????????', 'success')
        db.session.commit()
        return redirect(url_for('admin'))
    form.name.data = product.name
    form.price.data = product.price
    form.discount.data = product.discount
    form.stock.data = product.stock
    form.colors.data = product.colors
    form.discription.data = product.desc
    brand = product.brand.name
    category = product.category.name
    return render_template('products/addproduct.html', form=form, title='Update Product', getproduct=product,
                           brands=brands, categories=categories)


@app.route('/deleteproduct/<int:id>', methods=['GET', 'POST'])
@login_required
def deleteproduct(id):
    product = Addproduct.query.get_or_404(id)
    if request.method == "POST":
        try:
            os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_1))
            os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_2))
            os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_3))
        except Exception as e:
            print(e)
        db.session.delete(product)
        db.session.commit()
        flash(f'?????????????? {product.name} ?????? ???????????? ???? ????????????', 'success')
        return redirect(url_for('admin'))
    flash(f'???????????????????? ?????????????? ??????????????', 'success')
    return redirect(url_for('admin'))
