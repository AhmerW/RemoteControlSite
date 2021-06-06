
from .core.utils.config import app
from .resources.site.routes import router



app.include_router(router, prefix='/site')