import os
from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes, ConvertStrToListOfInt
from RFEM.enums import ObjectTypes

class Section():
    def __init__(self,
                 no: int = 1,
                 name: str = 'IPE 300',
                 material_no: int = 1,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Section Tag
            name (str): Name of Desired Section (As Named in RFEM Database)
            material_no (int): Tag of Material assigned to Section
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Section
        clientObject = model.clientModel.factory.create('ns0:section')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Section No.
        clientObject.no = no

        # Section nNme
        clientObject.name = name

        # Material No.
        clientObject.material = material_no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Section to client model
        model.clientModel.service.set_section(clientObject)

    @staticmethod
    def ImportFromRsection(no: int = None,
                           file_path: str = None,
                           model = Model):
        '''
        Creating Section from RSECtion file

        Args:
            no (int): Section number
            file_path (str): file path where the RSECTION (.rsc) file located
            model (RFEM Class, optional): Model to be edited
        '''

        assert os.path.exists(file_path)

        model.clientModel.service.create_section_from_rsection_file(no, file_path)

    @staticmethod
    def DeleteSection(sections_no: str = '1 2', model = Model):

        '''
        Args:
            sections_no (str): Numbers of Sections to be deleted
            model (RFEM Class, optional): Model to be edited
        '''

        # Delete from client model
        for section in ConvertStrToListOfInt(sections_no):
            model.clientModel.service.delete_object(ObjectTypes.E_OBJECT_TYPE_SECTION.name, section)
