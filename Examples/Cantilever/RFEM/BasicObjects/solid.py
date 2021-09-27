from RFEM.initModel import *

class Solid():
    def __init__(self,
                 no: int = 1,
                 boundary_surfaces_no: str = '1 2',
                 material_no: int = 1,
                 comment: str = ''):

        # Client model | Solid
        clientObject = clientModel.factory.create('ns0:solid')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Solid No.
        clientObject.no = no

        # Surfaces No. (e.g. "5 7 8 12 5")
        clientObject.boundary_surfaces = boundary_surfaces_no

        # Material
        clientObject.material = material_no

        # Comment
        clientObject.comment = comment

        # Add Surface to client model
        clientModel.service.set_solid(clientObject)
