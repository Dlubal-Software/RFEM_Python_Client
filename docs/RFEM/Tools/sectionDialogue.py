from RFEM.initModel import Model

def CreateSectionFavoriteList(name: str = "Favorites"):

    if isinstance(name, str):
        Model.clientModel.service.create_section_favorite_list(name)
    else:
        print("WARNING:Name of the section favorite list should be a string. Please kindly check the inputs.")

def AddSectionToFavoriteList(list_name: str = "Favorites",
                             section_name: str = "IPE 300"):

    if isinstance(list_name, str) and isinstance(section_name, str):
        Model.clientModel.service.add_section_to_favorite_list(list_name, section_name)
    else:
        print("WARNING:Name of the section favorite list and the section should be a string. Please kindly check the inputs.")

def DeleteSectionFromFavoriteList(list_name: str = "Favorites",
                                  section_name: str = "IPE 300"):

    if isinstance(list_name, str) and isinstance(section_name, str):
        Model.clientModel.service.delete_section_from_favorite_list(list_name, section_name)
    else:
        print("WARNING:Name of the section favorite list and the section should be a string. Please kindly check the inputs.")

def GetSectionFavoriteLists():

    return Model.clientModel.service.get_section_favorite_lists()

def DeleteSectionFavoriteList(name: str = "Favorites"):

    if isinstance(name, str):
        Model.clientModel.service.delete_section_favorite_list(name)
    else:
        print("WARNING:Name of the section favorite list should be a string. Please kindly check the inputs.")

def CreateSectionFromRsectionFile(no: int = 1,
                                  file_path: str = "/rsection_file_path/"):

    if isinstance(no, int) and isinstance(file_path, str):
        Model.clientModel.service.create_section_from_rsection_file(no, file_path)
    else:
        print("WARNING: Type of file_path argument should be string and the type of the no argument should be integer. Please kindly check the inputs.")
