#crear todas las tablas que no existan en la base de datos 
from app.config.database import Base, engine
#se necesita importar el modelo para que se cree la tabla
from app.models.Users import Users, create_admin_user
# Crear tablas en la BD si no existen
Base.metadata.create_all(engine)

create_admin_user()

