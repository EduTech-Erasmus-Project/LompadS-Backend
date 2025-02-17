import os
from os.path import basename
from pprint import pprint
from zipfile import ZipFile
from datetime import datetime
import zipfile

import json
from libraries import xmltodict

# Temporal file storage path
from model import LOMESLOMModel
from controller import LOMController

import pprint

_temp_files = './temp_files/'


def get_temp_folder():
    """
    Create a new temporal folder for data storage.

    :return:
        _temp_files represents the temporal folder.

    """
    if not os.path.exists(_temp_files):
        os.makedirs(_temp_files)
    return _temp_files


def get_temp_filefolder(filename: str):
    """
    Creates a temporal file folder for extracting the ZIP file.

    :param filename: The name of the file (isn't it obvious)
    :type filename str

    :return: The name of the temporal folder.
    """
    temp_filefolder = f'{filename}'
    if not os.path.exists(f'{filename}'):
        os.makedirs(get_temp_folder() + temp_filefolder.replace('.zip', ''))
    return temp_filefolder


def get_file_type(file):
    """
    Determines the type of the file to upload.

    :param file: Name of the file.
    :type file str

    :return:
        0: If it's a zip.
        1: If it's a XML.
        -1: If it isn't a valid file format.
    """
    if '.zip' in file:
        return 0
    elif '.xml' in file:
        return 1
    else:
        return -1


def save_xml(file):
    """
    Save a XML file in the specified path using hash values avoiding overwriting.

    :param file: The name of the file with its path.
    :return: The path of the file created and it's hashed value.
    """
    _temporal = get_temp_folder()
    hashed_filename = str(file.filename).split('.xml')[0] + "_" \
                      + str(hash(file.filename + datetime.today().strftime('%Y-%m-%d-%H:%M:%S'))) \
                      + '.xml'
    path = _temporal + hashed_filename
    #print("****",path)
    with open(path, 'wb+') as f:
        #f=etree.parse(f)
        f.write(file.file.read())
        f.close()
    return path, hashed_filename

 


def save_zip(file):
    """
    Save a file in the specified path using hash values, by this avoid overwrite by users.

    param file: The name of the file with its path.
    type: file UploadFile (FastAPI)

    :return: The path of the file created and it's hashed value.
    """
    #print("entra")
    _temporal = get_temp_folder()
    hashed_filename = str(file.filename).split('.zip')[0] + "_" \
                      + str(hash(file.filename + datetime.today().strftime('%Y-%m-%d-%H:%M:%S'))) \
                      + '.zip'
    path = _temporal + hashed_filename
    with open(path, 'wb+') as f:
        f.write(file.file.read())
        f.close()
    return path, hashed_filename


def unzip_file(file_name, hashed_filename, file_path, extraction_path=os.getcwd() + '/temp_files/'):
    """
    Uncompress a zip file inside a folder with the same name.

    param file_path: The path of the zip file.
    type file_path str

    param extraction_path: The path of extraction, by default it's inside temporal folder.
    type extraction_path str

    :return:
        None
    """
    with ZipFile(file_path) as file:
        file.extractall((extraction_path + get_temp_filefolder(hashed_filename)).replace('.zip', '') + '/')


def delete_temp_file(file_path):
    """
    Try to delete a temporal file.

    param file_path: The location of the file with its name.
    type file_path str

    :return:
        True if file was deleted or False if an error occurred.
    """
    try:
        os.remove(file_path)
        return True
    except Exception as e:
        print(e)
        return False


def read_manifest(ims_manifest_path):
    """
    Read the ims_manifest XML file by its path.

    param ims_manifest_path: The path of the ims_manifest XML.
    type ims_manifest_path str

    :return:
        A string representing the whole file.
    """
    #print("Entra 1: ",ims_manifest_path)
    try:
        with open(ims_manifest_path,'r',encoding='UTF-8') as file:
            #file=etree.parse(file)
            read=file.readlines()
            file.close()
            return ''.join(read)

    except Exception as e:
        print(e)
        return -1


def parse_manifest(ims_manifest_data):
    """
    Parse a valid XML string to JSON.

    param ims_manifest_data: An XML string with ims_manifest data.
    type ims_manifest_data str

    :return:
        A valid JSON if parsing process was correct, else None.
    """
    try:
        return xmltodict.parse(ims_manifest_data)
    except Exception as e:
        print(e)
        return None


def load_recursive_as_class(manifest,booleanLomLomes):
    #print("File Con# 188 - Manifest",manifest)
    lom_controller = LOMController.Controller()
    parsed_dict = lom_controller.parse_str_to_dict(manifest)
    #print("File Con# 191 - parset",manifest)
    lom_controller.map_recursively(parsed_dict, booleanLomLomes,is_lompad_exported=True)
    #print("File Con# 193 - mapet",manifest)
    lom = lom_controller.get_mapped_class()
    return lom


def load_recursive_model(manifest, booleanLomLomes,hashed_code, is_lompad_exported=False):
    """
    Load LOMPAD XML file into Python Class

    :param manifest: A valid XML string.
    :param is_lompad_exported: Check if manifest comes from lompad application.
    :return: string (as json) representing mapped values.
    """

    lom_controller = LOMController.Controller()
    parsed_dictionary: dict = lom_controller.parse_str_to_dict(manifest)

    #print("Diccionario 208:",parsed_dictionary)

    # print("=============================================================")
    # print(parsed_dictionary.get('lomes:lom').keys())
    # print("=============================================================")
    lom_controller.__setattr__("_mapped_data", dict())
    lom_controller.__setattr__("_object_dict", dict())
    lom_controller.map_recursively(parsed_dictionary, booleanLomLomes,is_lompad_exported=is_lompad_exported)
    # print(lom_controller.__getattribute__('_mapped_data'))
    new_dict={}

    for key in lom_controller.get_mapped_manifest(hashed_code, booleanLomLomes).keys():
        if "lomes:" in key:
            key2 = key.replace('lomes:', '')
            new_dict[key2]=lom_controller.get_mapped_manifest(hashed_code, booleanLomLomes)[key]
    if bool(new_dict):
        # print(new_dict)
        return new_dict
    # print(lom_controller.get_mapped_manifest(hashed_code, booleanLomLomes))
    return lom_controller.get_mapped_manifest(hashed_code, booleanLomLomes)



def update_model(hashed_code, leaf, model, data, booleanLomLomes):

    model = LOMESLOMModel.update_leaf(leaf, model, data)
    
    ##
    #mydata = etree.tostring(model.to_xml().strip())
    #myfile = open('temp_files/' + hashed_code + '_exported.xml', 'w')
    #myfile.write(mydata)
    ##


    with open('temp_files/' + hashed_code + '_exported.xml', 'w',encoding='UTF-8') as file:
        #file=etree.parse(file)
        file.write(model.to_xml().strip())
        file.close()

    return model.__dict__()


def write_data(data, folder, hased_code,path_in_folder):
    from os import path

    if path.exists(f'{folder}'):
        with open(f'{folder}', 'w', encoding="UTF-8") as file:
            file.write(data, encoding="UTF-8")
            file.close()
    with ZipFile(f'./temp_files/{hased_code}.zip', 'w') as zipObj:
        if path_in_folder:
            for folderName, subfolders, filenames in os.walk(f'./temp_files/{hased_code}'):
                for filename in filenames:
                    filePath = os.path.join(folderName, filename)
                    zipObj.write(filePath, basename(filePath))
        else:
            zipObj.write(folder, compress_type=zipfile.ZIP_STORED)

"""
    TODO:
        - Remove files after working with them.
    
    DONE:
        - Zip file is deleted after uncompressed.

"""
