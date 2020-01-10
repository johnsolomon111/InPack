from flask_table import Table, Col, LinkCol
 
class Results(Table):

    edit = LinkCol('Edit', 'edit', url_kwargs=dict(item_id='item_id'))