from project import ma
from project.models import Usuario


class UsuarioSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario
        load_instance = True
        load_only = ('password', )


usuario_schema = UsuarioSchema()
