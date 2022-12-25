from flask import render_template, session, redirect, url_for, flash
from shop import app, db, bcrypt
from .forms import RegistrationForm, LoginForm
from .models import User
from shop.products.models import Addproduct, Category, Brand
from flask_login import login_required

@app.route('/admin')
@login_required
def admin():
    products = Addproduct.query.all()
    return render_template('admin/index.html', title='Admin page', products=products)


@app.route('/brands')
@login_required
def brands():
    brands = Brand.query.order_by(Brand.id.desc()).all()
    return render_template('admin/brand.html', title='brands', brands=brands)


@app.route('/categories')
@login_required
def categories():
    categories = Category.query.order_by(Category.id.desc()).all()
    return render_template('admin/brand.html', title='categories', categories=categories)


@app.route('/login', methods=['GET', 'POST'])
@login_required
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['email'] = form.email.data
            flash(f'Добро пожаловать {form.email.data} вы вошли в аккаунт!', 'success')
            return redirect(url_for('admin'))
        else:
            flash(f'Неверный email или пароль', 'success')
            return redirect(url_for('login'))
    return render_template('admin/login.html', title='Вход', form=form)
