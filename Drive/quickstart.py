from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaIoBaseDownload
import io, os
import pandas as pd
from pathlib import Path
from Docs import docs

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive']
aux = []

def api(cond):
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('drive', 'v3', credentials=creds)

    # Call the Drive v3 API
    #results = service.files().list(
    #    pageSize=10, fields="nextPageToken, files(id, name)").execute()
    #items = results.get('files', [])

    #if not items:
    #    print('No files found.')
    #else:
    #    print('Files:')
    #    for item in items:
    #        print(u'{0} ({1})'.format(item['name'], item['id']))
    n=cond
    if n == 'excel':
        consultaExcel(service)
    if n == 'word':
        consultaWord(service)
    if n == 'pres':
        consultaSlides(service)
    if n == 'PDF':
        consultaPDF(service)
    if n == 'carpeta':
        consultaCarpetas(service)
    if n == 'descarga':
        descarga(service)
    if n == 'crear':
    	crearCarpetas(service)
    if n == 'crearDoc':
        creaDocs(service, creds)

def crearCarpetas(service):
    df= pd.read_excel('prueba2.xlsx', skiprows=2, usecols="C")
        #print(df)
    arreglo=df.values
   # lista=[ 20152020007, 20152020042, 20152020222, 20161020004, 20161020505,
#		20161020540, 20161020544, 20161150007, 20162005886, 20162020015, 20162020029,
#		20162020033, 20162020093, 20162020103, 20162020105, 20162020427, 20162025711,
#		20171020014, 20171020021, 20171020047, 20171020059, 20171020075, 20171020087,
#		20171020099, 20171020113, 20171020118, 20171020139, 20171020153, 20172020029,
#		20172020035, 20172020050, 20172020067, 20172020079, 20172020093, 20172020100,
#		20172020125, 20172020141, 20172025108 ]
    file_metadata = {
    'name': 'Prueba',
    'mimeType': 'application/vnd.google-apps.folder'
    }
    file = service.files().create(body=file_metadata,fields='id').execute()
    print('Folder ID: %s' % file.get('id'))
    for i in range(len(arreglo)):
            num = str(arreglo[i])
            file_metadata2 ={
            'name': num,
            'parents': [file.get('id')],'mimeType': 'application/vnd.google-apps.folder'
            }    
            file2 = service.files().create(body=file_metadata2, 
            fields='id').execute()
            print(str(file2.get('id')))
    print(arreglo)
    print(len(arreglo))

def creaDocs(service, creds1):
    file_metadata = {
    'name': 'Docu Prueba',
    'mimeType': 'application/vnd.google-apps.document'
    }
    file = service.files().create(body=file_metadata,fields='id').execute()
    print('Doc ID: %s' % file.get('id'))
    docs.mngDocs(file.get('id'))

def consultaExcel(service):
    global aux
    aux.clear()
    page_token = None
    response = service.files().list(q="mimeType='application/vnd.google-apps.spreadsheet'",
                                         spaces='drive',
                                         fields='nextPageToken, files(id, name)',
                                         pageToken=page_token, pageSize=10).execute()
    for file in response.get('files', []):
        # Process change
        #print ('Found file: %s (%s)' % (file.get('name'), file.get('id')))
        page_token = response.get('nextPageToken', None)
        aux.append((file.get('name'), file.get('id')))
    return aux

def consultaPDF(service):
    global aux
    aux.clear()
    page_token = None
    response = service.files().list(q="mimeType='application/PDF'",
                                         spaces='drive',
                                         fields='nextPageToken, files(id, name)',
                                         pageToken=page_token, pageSize=10).execute()
    for file in response.get('files', []):
        # Process change
        #print ('Found file: %s (%s)' % (file.get('name'), file.get('id')))
        page_token = response.get('nextPageToken', None)
        aux.append((file.get('name'), file.get('id')))
    return aux

def consultaWord(service):
    global aux
    aux.clear()
    page_token = None
    response = service.files().list(q="mimeType='application/vnd.google-apps.document'",
                                         spaces='drive',
                                         fields='nextPageToken, files(id, name)',
                                         pageToken=page_token, pageSize=10).execute()
    for file in response.get('files', []):
        # Process change
        #print ('Found file: %s (%s)' % (file.get('name'), file.get('id')))
        page_token = response.get('nextPageToken', None)
        aux.append((file.get('name'), file.get('id')))
    return aux
def consultaSlides(service):
    global aux
    aux.clear()
    page_token = None
    response = service.files().list(q="mimeType='application/vnd.google-apps.presentation'",
                                         spaces='drive',
                                         fields='nextPageToken, files(id, name)',
                                         pageToken=page_token, pageSize=10).execute()
    for file in response.get('files', []):
        # Process change
        #print ('Found file: %s (%s)' % (file.get('name'), file.get('id')))
        page_token = response.get('nextPageToken', None)
        aux.append((file.get('name'), file.get('id')))
    return aux

def consultaCarpetas(service):
    global aux
    aux.clear()
    page_token = None
    response = service.files().list(q="mimeType='application/vnd.google-apps.folder'",
                                         spaces='drive',
                                         fields='nextPageToken, files(id, name)',
                                         pageToken=page_token, pageSize=10).execute()
    for file in response.get('files', []):
        # Process change
        #print ('Found file: %s (%s)' % (file.get('name'), file.get('id')))
        page_token = response.get('nextPageToken', None)
        aux.append((file.get('name'), file.get('id')))
    return aux

def consultaExcelC(service, id):
    global aux
    aux.clear()
    page_token = None
    response = service.files().list(q="mimeType='application/vnd.google-apps.spreadsheet' and '1PU_VAANZKGHAS4buj2tEQZGdxcaCtMEa' in parents",
                                         spaces='drive',
                                         fields='nextPageToken, files(id, name)',
                                         pageToken=page_token, pageSize=10).execute()
    for file in response.get('files', []):
        # Process change
        #print ('Found file: %s (%s)' % (file.get('name'), file.get('id')))
        page_token = response.get('nextPageToken', None)
        aux.append((file.get('name'), file.get('id')))
    return aux

def descargaMedia(service):
    file_id = '0BwwA4oUTeiV1UVNwOHItT0xfa2M'
    request = service.files().get_media(fileId=file_id)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print ("Download %d%%." % int(status.progress() * 100))

def descarga(service):
    file_id = '1qgCPBSoyihrLQOiPmW5_d6X14OmyW-nr'
    request = service.files().get_media(fileId=file_id)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print ("Download %d%%." % int(status.progress() * 100))
    with io.open('C:/Users/BRIANORLANDO/Documents/monContexto/APIS/Drive/prueba.pdf', 'wb') as f:
        fh.seek(0)
        f.write(fh.read())
