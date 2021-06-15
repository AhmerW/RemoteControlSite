
from .core.utils.const import app
from .resources.site.routes import router

print("ran")

app.include_router(router, prefix='/site')
