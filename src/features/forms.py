from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField,IntegerField
from wtforms.fields.html5 import DateField 
from wtforms.widgets import html5
from wtforms.validators import DataRequired, ValidationError




class FeaturesForm(FlaskForm):
	title= StringField('Title', validators=[DataRequired()])
	description = TextAreaField('Description', validators=[DataRequired()])
	client= SelectField('Client', choices=[('Client A', 'Client A'), ('Client B', 'Client B'), ('Client C', 'Client C')])
	client_priority = IntegerField('Client Priority', widget=html5.NumberInput(), validators=[DataRequired()])
	target_date = DateField('Target Date', validators=[DataRequired()])
	product_area = SelectField('Product Area', choices=[('Policies', 'Policies'), ('Billing', 'Billing'), ('Claims', 'Claims'), ('Reports', 'Reports')])
	submit = SubmitField('Request Features')

	def validate_client_priority(self, client_priority):
		if client_priority.data < 0:
			raise ValidationError('Client Priority should be a positive integer')
