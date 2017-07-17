from app import app
from flask_assets import Environment, Bundle

assets = Environment(app)
js = Bundle(
  'js/admin/admin-init.js',
  filters='jsmin',
  output='gen/packed.js'
)
assets.register('js_all', js)


