from RFEM.initModel import Model, clearAtributes
from RFEM.enums import NodalMeshRefinementType
from enum import Enum

class FElengthArrangement(Enum):
    LENGTH_ARRANGEMENT_RADIAL, LENGTH_ARRANGEMENT_GRADUALLY, LENGTH_ARRANGEMENT_COMBINED = range(3)

class NodalMeshRefinement():
    def __init__(self,
                 no: int = 1,
                 type = NodalMeshRefinementType.TYPE_CIRCULAR,
                 mesh_parameters: list = None,
                 apply_on_selected_surfaces: bool = False,
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        """
        Nodal Mesh Refinement

        Args:
            no (int, optional): Number
            type (_type_, optional): TYPE_CIRCULAR or TYPE_RECTANGULAR
            mesh_parameters (list, optional): _description_. Defaults to None.
                if TYPE_CIRCULAR:
                    (circular_radius, circular_target_inner_length, circular_target_outer_length, circular_length_arrangement)
                    (2.5, 0.1, 0.5, FElengthArrangement.LENGTH_ARRANGEMENT_RADIAL)
                elif TYPE_RECTANGULAR:
                    (rectangular_side, rectangular_target_inner_length)
                    (0.5, 0.1)
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (_type_, optional): Model instance
        """

        # Client model | Nodal Mesh Refinement
        clientObject = model.clientModel.factory.create('ns0:nodal_mesh_refinement')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Nodal Mesh Refinement No.
        clientObject.no = no

        # Nodal Mesh Refinement Type
        clientObject.type = type.name

        # Mesh Parameters
        if type == NodalMeshRefinementType.TYPE_CIRCULAR:
            clientObject.circular_radius = mesh_parameters[0]
            clientObject.circular_target_inner_length = mesh_parameters[1]
            clientObject.circular_target_outer_length = mesh_parameters[2]
            clientObject.circular_length_arrangement = mesh_parameters[3].name
        elif type == NodalMeshRefinementType.TYPE_RECTANGULAR:
            clientObject.rectangular_side = mesh_parameters[0]
            clientObject.rectangular_target_inner_length = mesh_parameters[1]

        # Apply Only on Selected Surfaces
        clientObject.apply_only_on_selected_surfaces = apply_on_selected_surfaces

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Nodal Mesh Refinement to client model
        model.clientModel.service.set_nodal_mesh_refinement(clientObject)

    @staticmethod
    def Circular(
                 no: int = 1,
                 circular_radius: float = 2.5,
                 circular_target_inner_length: float = 0.1,
                 circular_target_outer_length: float = 0.5,
                 circular_length_arrangement = FElengthArrangement.LENGTH_ARRANGEMENT_RADIAL,
                 apply_on_selected_surfaces: bool = False,
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        """
        Circular Nodal Mesh Refinement

        Args:
            no (int, optional): Number
            circular_radius (float, optional): Radius
            circular_target_inner_length (float, optional): Inner target FE length
            circular_target_outer_length (float, optional): Outer target FE length
            circular_length_arrangement (_type_, optional): FE length arrangenemt
            apply_on_selected_surfaces (bool, optional): Apply only on surfaces
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (_type_, optional): Model instance
        """

        # Client model | Nodal Mesh Refinement
        clientObject = model.clientModel.factory.create('ns0:nodal_mesh_refinement')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Nodal Mesh Refinement No.
        clientObject.no = no

        # Nodal Mesh Refinement Type
        clientObject.type = NodalMeshRefinementType.TYPE_CIRCULAR.name

        # Mesh Parameters
        clientObject.circular_radius = circular_radius
        clientObject.circular_target_inner_length = circular_target_inner_length
        clientObject.circular_target_outer_length = circular_target_outer_length
        clientObject.circular_length_arrangement = circular_length_arrangement.name

        # Apply Only on Selected Surfaces
        clientObject.apply_only_on_selected_surfaces = apply_on_selected_surfaces

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Nodal Mesh Refinement to client model
        model.clientModel.service.set_nodal_mesh_refinement(clientObject)

    @staticmethod
    def Rectangular(
                 no: int = 1,
                 rectangular_side: float = 2.5,
                 rectangular_target_inner_length: float = 0.1,
                 apply_on_selected_surfaces: bool = False,
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        """
        Rectangular Nodal Mesh Refinement

        Args:
            no (int, optional): Number
            rectangular_side (float, optional): Side length
            rectangular_target_inner_length (float, optional): Inner target FE length
            apply_on_selected_surfaces (bool, optional): Apply only on surfaces
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (_type_, optional): Model instance
        """

        # Client model | Nodal Mesh Refinement
        clientObject = model.clientModel.factory.create('ns0:nodal_mesh_refinement')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Nodal Mesh Refinement No.
        clientObject.no = no

        # Nodal Mesh Refinement Type
        clientObject.type = NodalMeshRefinementType.TYPE_RECTANGULAR.name

        # Mesh Parameters
        clientObject.rectangular_side = rectangular_side
        clientObject.rectangular_target_inner_length = rectangular_target_inner_length

        # Apply Only on Selected Surfaces
        clientObject.apply_only_on_selected_surfaces = apply_on_selected_surfaces

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Nodal Mesh Refinement to client model
        model.clientModel.service.set_nodal_mesh_refinement(clientObject)
