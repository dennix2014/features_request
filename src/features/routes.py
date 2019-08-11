from flask import render_template, redirect, url_for, flash
from src import db
from src.features import bp
from src.features.forms import FeaturesForm
from src.models import Features
from flask_login import login_required
import datetime





@bp.route('/add_features', methods=['GET', 'POST'])
@login_required
def add_features():
	form = FeaturesForm()
	if form.validate_on_submit():

		exists = Features.query.filter(int(form.client_priority.data)==Features.client_priority, form.client.data==Features.client).first()
		if exists:
		
			other_features_request_by_same_client = Features.query.filter( \
				Features.client == form.client.data, \
				Features.client_priority >= form.client_priority.data)
		
			for item in other_features_request_by_same_client:
				item.client_priority += 1
		
		feature = Features(title=form.title.data, description=form.description.data, \
			client=form.client.data, client_priority=form.client_priority.data, \
			target_date=form.target_date.data, product_area=form.product_area.data, request_date=datetime.datetime.now())
		
		db.session.add(feature)
		db.session.commit()
		flash('Request for features added sucessfully')
		return redirect(url_for('features.home'))
	return render_template('features/add_features.html', title='Add Features', form=form)


@bp.route('/')
@bp.route('/home')
@login_required
def home():
	features = Features.query.order_by(Features.request_date)
	return render_template('features/home.html', title='Home', features=features)

@bp.route('/edit_feature/<feature_id>', methods=['GET', 'POST'])
@login_required
def edit_feature(feature_id):
	feature_id = Features.query.filter_by(id=feature_id).first_or_404()
	form = FeaturesForm(obj=feature_id)
	if form.validate_on_submit():
		exists = Features.query.filter(int(form.client_priority.data)==Features.client_priority, form.client.data==Features.client).first()
		if exists:
			requests_by_same_client = Features.query.filter(Features.client == form.client.data, \
				Features.client_priority >= form.client_priority.data, form.client_priority.data != feature_id.client_priority)
			for item in requests_by_same_client:
				item.client_priority += 1
		

		form.populate_obj(feature_id)

		db.session.commit()
		flash('Request updated sucessfully')
		return redirect(url_for('features.home'))
	return render_template('features/edit_feature.html', title='Edit Feature', form=form)


