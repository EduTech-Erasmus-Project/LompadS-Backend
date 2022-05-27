import uvicorn
import io
from pprint import pprint
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.openapi.models import Response
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse
from controller import FileController

import glob
import os 
from bs4 import BeautifulSoup
from xml.dom import minidom
import xml.etree.ElementTree as ET

app = FastAPI()
fileFound=''
booleanLomLomes=True #If booleanLomLomes is True represents a lom format, and
                     #if booleanLomLomes is False represents a lomes format.

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
    allow_credentials=True,
)

@app.post("/uploadfile")
async def upload_file(file: UploadFile = File(...)):
    """
    Upload a file from Multipart POST request and return imsmanifest.xml file as JSON.

    :param file: A Multipart Form Data.
    :return:
        imsmanifest.xml as JSON if parse was correct, else raise a new HTTPException with Exception code 500.
       
        file_type = FileController.get_file_type(file.filename)   return:  0: If it's a zip. 1: If it's a XML. -1: If it isn't a valid file format. 
    """
    global fileFound
    global booleanLomLomes
    fileFound=''
    file_type = FileController.get_file_type(file.filename)  
    _filepath = None
    _profile = None
    xml_manifest = None
    xml_manifest_ims = -1
    required_tags = ['identifier', 'title', 'language', 'description', 'aggregationLevel', 'metaMetadata','metadataSchema']

    redundant_elements = [' uniqueElementName="general"', ' uniqueElementName="catalog"',' uniqueElementName="entry"',
                          ' uniqueElementName="aggregationLevel"', ' uniqueElementName="role"', ' uniqueElementName="dateTime"',
                          ' uniqueElementName="source"',' uniqueElementName="value"', ' uniqueElementName="metaMetadata"', 
                          ' uniqueElementName="rights"', ' uniqueElementName="access"', ' uniqueElementName="accessType"', 
                          ' uniqueElementName="source"', ' uniqueElementName="value"','uniqueElementName="lifeCycle"',
                          'uniqueElementName="technical"']

    if file_type == -1:
        return HTTPException(status_code=500, detail='Error, not a valid file type.')
    elif file_type == 1:
        _filepath, _hashed_filename = FileController.save_xml(file)
        xml_manifest = FileController.read_manifest(_filepath)
        for redundant in redundant_elements:
            xml_manifest = xml_manifest.replace(redundant, '')
        doc = minidom.parse(_filepath)
        childTag = doc.firstChild.tagName
        if(childTag == "lom"):
            fileFound=_filepath
            booleanLomLomes=True
        elif(childTag == "lomes:lom"):
            fileFound=_filepath
            booleanLomLomes=False
        else:
            return HTTPException(status_code=500,
                          detail='Error, the uploaded file does not contain metadata')

        if xml_manifest == -1:
            _profile = 'IMS'
        elif xml_manifest != -1:
            _profile = 'SCORM'
        else:
            return  HTTPException(status_code=500,
                          detail='Error, the uploaded file does not contain imslrm.xml nor imsmanifest.xml files.')     

        return {'STATUS_CODE':200,'PERFIL': _profile, 'HASHED_VALUE': _hashed_filename.replace('.xml', ''), 'XML_FILE':FileResponse(path=f'./temp_files/{_hashed_filename}_exported.xml',
                            filename=f'./temp_files/{_hashed_filename}_exported.xml')} \
        if xml_manifest is not None else HTTPException(status_code=500,
                                                       detail='Error trying to parse the'
                                                              ' imsmanifest.xml')

    else:
        print("entra-zip")
        _filepath, _hashed_filename = FileController.save_zip(file=file)
        FileController.unzip_file(file.filename, _hashed_filename, _filepath)
        FileController.delete_temp_file(_filepath)

        hashed=_hashed_filename.replace('.zip', '')
        
        #print(" this is the hash: ",hashed)

        targetPattern = './temp_files/'+hashed+'/**/*.xml'
        
        routes = glob.glob(targetPattern)

        if len(routes) == 0:
            targetPattern = './temp_files/'+hashed+'/*.xml'
            routes = glob.glob(targetPattern)
            #print("The routes found in root are:")
            #print(routes)
        
        print(len(routes))
        #print("The routes found are")
        #print(routes)

        
        
        containmetadata=False

        for filePath in routes:
            try:
                #print("---------------+")
                #print(filePath)
                #doc = minidom.parse(filePath)
                #childTag =doc.firstChild.tagName
                
                doc = ET.parse(filePath)
                root = doc.getroot()
                #print(root.tag)

                childTag = root.tag
                #print("++")
                #print(childTag)
                #print("+-")
                #print(root)
                #print("--")
                #print(root.tag)

                if(childTag == "{http://ltsc.ieee.org/xsd/LOM}lom"):
                    print("Entra LOM")
                    fileFound=filePath
                    booleanLomLomes=True
                    containmetadata=True
                    break

                elif(childTag == "lom"):
                    print("Entra LOM")
                    fileFound=filePath
                    booleanLomLomes=True
                    containmetadata=True
                    break

                elif(childTag == "lomes:lom"):
                    fileFound=filePath
                    booleanLomLomes=False
                    containmetadata=True
                    break
            except:
                print("entra excep")
                try:
                    childTag = doc.getElementsByTagName("lom:lom")
                    if(len(childTag)>=1):
                        fileFound=filePath
                        booleanLomLomes=True
                        containmetadata=True
                    break
                except:
                    print("something happened with the file in the path: "+filePath)
            #print("----------------")

        if not containmetadata:
            print("Archivo no contiene archivo de metadatos")
            return HTTPException(status_code=500,
                          detail='Error, the uploaded file does not contain imslrm.xml nor imsmanifest.xml files.')

        fileFound.replace('./temp_files/', '')
        ##-----------------------------------------------------------
        xml_manifest_scorm = FileController.read_manifest(fileFound)
        print("Lee archivo--")
        for redundant in redundant_elements:
            xml_manifest_scorm = xml_manifest_scorm.replace(redundant, '')
        xml_manifest_scorm = xml_manifest_scorm.replace('lom:', '')
        if xml_manifest_scorm == -1:
            xml_manifest_ims = FileController.read_manifest(_filepath.replace('.zip', '') + '/imsmanifest.xml')
            xml_manifest = xml_manifest_ims
            for redundant in redundant_elements:
                xml_manifest = xml_manifest.replace(redundant, '')
            _profile = 'IMS'
        elif xml_manifest_scorm != -1:
            _profile = 'SCORM'
            xml_manifest = xml_manifest_scorm
            for redundant in redundant_elements:
                xml_manifest = xml_manifest.replace(redundant, '')
        else:
            return HTTPException(status_code=500,
                          detail='Error, the uploaded file does not contain imslrm.xml nor imsmanifest.xml files.')
        print("Sal1 33")
    return {'STATUS_CODE':200,'PERFIL': _profile, 'HASHED_VALUE': _hashed_filename.replace('.zip', '').replace('.xml', '')} \
        if xml_manifest is not None else HTTPException(status_code=500,
                                                       detail='Error trying to parse the'
                                                              ' imsmanifest.xml')

@app.get("/private/read_file/")
async def read_file(hashed_code: str, profile: str):

    redundant_elements = [' uniqueElementName="general"', ' uniqueElementName="catalog"',' uniqueElementName="entry"',
                          ' uniqueElementName="aggregationLevel"', ' uniqueElementName="role"', ' uniqueElementName="dateTime"',
                          ' uniqueElementName="source"',' uniqueElementName="value"', ' uniqueElementName="metaMetadata"', 
                          ' uniqueElementName="rights"', ' uniqueElementName="access"', ' uniqueElementName="accessType"', 
                          ' uniqueElementName="source"', ' uniqueElementName="value"','uniqueElementName="lifeCycle"',
                          'uniqueElementName="technical"']

    import glob
    import os 

    global fileFound

    print ("Se esta recibiendo ", fileFound)

    from_lompad = False

    # xml_manifest = FileController.read_manifest(fileFound)
    # # print(xml_manifest)
    # for redundant in redundant_elements:
    #         xml_manifest = xml_manifest.replace(redundant,'')
    # # print("*********************************************")
    # # print(xml_manifest)

    if profile == 'SCORM':
        #print("SCORM #227")
        xml_manifest = FileController.read_manifest(fileFound)
        #print(xml_manifest)
        for redundant in redundant_elements:
                xml_manifest = xml_manifest.replace(redundant,'')
        xml_manifest = xml_manifest.replace('lom:', '')
        # print("*********************************************")
        # print(xml_manifest)
    else:
        xml_manifest = FileController.read_manifest(f'./temp_files/{hashed_code}/imsmanifest.xml')
        for redundant in redundant_elements:
                xml_manifest = xml_manifest.replace(redundant, '')
        xml_manifest = xml_manifest.replace('lom:', '')
    if xml_manifest == -1:
        xml_manifest = FileController.read_manifest(f'./temp_files/{hashed_code}.xml')
        for redundant in redundant_elements:
                xml_manifest = xml_manifest.replace(redundant, '')
        xml_manifest = xml_manifest.replace('lom:', '')
        from_lompad = True

    if xml_manifest == -1:
        raise HTTPException(status_code=500,
                      detail='Error, file not found or corrupted.')


    if not from_lompad:
        print ("Termina 253")
        return {'statusCode':200,'data': FileController.load_recursive_model(xml_manifest, booleanLomLomes,hashed_code), 'XML_FILE':xml_manifest}
    else:
        print ("Termina 256")
        return {'statusCode':200,'data': FileController.load_recursive_model(xml_manifest, hashed_code, is_lompad_exported=True), 'XML_FILE':xml_manifest}

@app.post("/private/update/")
async def update_file(hashed_code: str, hoja, data):
    print("++")
    print(hashed_code)
    print("-+")
    print(hoja)
    print("+-")
    print(data)
    print("--")
    global booleanLomLomes
    

    redundant_elements = [' uniqueElementName="general"', ' uniqueElementName="catalog"',' uniqueElementName="entry"',
                          ' uniqueElementName="aggregationLevel"', ' uniqueElementName="role"', ' uniqueElementName="dateTime"',
                          ' uniqueElementName="source"',' uniqueElementName="value"', ' uniqueElementName="metaMetadata"', 
                          ' uniqueElementName="rights"', ' uniqueElementName="access"', ' uniqueElementName="accessType"', 
                          ' uniqueElementName="source"', ' uniqueElementName="value"','uniqueElementName="lifeCycle"',
                          'uniqueElementName="technical"']

    manifest = FileController.read_manifest(f'./temp_files/{hashed_code}_exported.xml')

    for redundant in redundant_elements:
        manifest = manifest.replace(redundant, '')
    manifest = manifest.replace('lom:', '')
    manifest = manifest.replace("['", '')
    manifest = manifest.replace("']", '')
    manifest = manifest.replace('"]', '')
    manifest = manifest.replace('["', '')
    manifest = manifest.replace(", 'None']", "]")
    #print('PASO 1')
    lom = FileController.load_recursive_as_class(manifest, booleanLomLomes)
    #print(lom.__getattribute__('lifeCycle').__dict__())
    #print('PASO 2')
    response = FileController.update_model(hashed_code, hoja, lom, data,booleanLomLomes)
    manifest = FileController.read_manifest(f'./temp_files/{hashed_code}_exported.xml')
    #print("*********************************************************************")
    #print(manifest)

    return {'data': response, 'XML_FILE':manifest}

@app.get("/private/download/", response_class=FileResponse)
def get_file(hashed_code, option):
    import glob
    import os

    # print("el hash es: ",hashed_code)
    # print("la opcion es: ",option)

    paths = glob.glob('./temp_files/*')
    if option == "zip":
        for path in paths:
            if hashed_code in path and os.path.isdir(path):
                fileFound=''
                targetPattern = './temp_files/'+hashed_code+'/**/*.xml'
        
                routes = glob.glob(targetPattern)
                # print("The routes found are")
                # print(routes)

                if len(routes) == 0:
                    targetPattern = './temp_files/'+hashed_code+'/*.xml'
                    routes = glob.glob(targetPattern)
                    # print("The routes found in root are:")
                    # print(routes)
                for filePath in routes:
                    try:
                        doc = minidom.parse(filePath)
                        childTag = doc.firstChild.tagName
                        if(childTag == "lom"):
                            fileFound=filePath
                            break
                        elif(childTag == "lomes:lom"):
                            fileFound=filePath
                            break
                    except:
                        try:
                            childTag = doc.getElementsByTagName("lom:lom")
                            if(len(childTag)>=1):
                                fileFound=filePath
                            break
                        except:
                            print("something happened with the file in the path: "+filePath)
                
                FileController.write_data(''.join(open(f'./temp_files/{hashed_code}_exported.xml')).strip(),
                                        fileFound, hashed_code,True)
                return FileResponse(path=f'./temp_files/{hashed_code}.zip', filename=f'./temp_files/{hashed_code}.zip')
            if path == f"./temp_files\{hashed_code}.xml":
                FileController.write_data(''.join(open(f'./temp_files/{hashed_code}_exported.xml')).strip(),
                                        (f'./temp_files/{hashed_code}.xml'), hashed_code,False)
                return FileResponse(path=f'./temp_files/{hashed_code}.zip', filename=f'./temp_files/{hashed_code}.zip')
    else:
        return FileResponse(path=f'./temp_files/{hashed_code}_exported.xml',
                            filename=f'./temp_files/{hashed_code}_exported.xml')
