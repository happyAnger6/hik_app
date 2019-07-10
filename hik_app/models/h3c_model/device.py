from hik_app.models.base.fields import UintField, GroupField, StringField
from hik_app.models.base.table import Table

class Base(Table):
    Uptime = UintField("Uptime", json_name='uptime', configurable=False)