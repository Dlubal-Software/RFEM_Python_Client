from RFEM.initModel import Model, clearAtributes

class SurfaceStiffnessModification():
    def __init__(self,
                 no: int = 1,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        # Client model | Surface Stifness Modification
        clientObject = model.clientModel.factory.create('ns0:surface_stiffness_modification')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Surface Stifness Modification No.
        clientObject.no = no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Surface Stifness Modification to client model
        model.clientModel.service.set_surface_stiffness_modification(clientObject)
