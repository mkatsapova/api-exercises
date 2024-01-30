"""Get, create, update, delete GitHub file/repository"""


import base64
import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()


# Get all the user`s repositories from the GitHub - GET
def get_all_repository():
    base_url = 'https://api.github.com/user/repos'

    response = requests.get(base_url, headers={'Authorization': 'token {}'.format(os.getenv('GITHUB_TOKEN'))})

    for x in response.json():
        print(x['name'])


# Create a new repository - POST
def create_new_repository():
    repository_name = 'api exercises'
    repository_description = 'The repo was created using GitHub API.'
    base_url = 'https://api.github.com/user/repos/'
    repo_config = json.dumps({'name': f'{repository_name}',
                              'description': f'{repository_description}',
                              'auto_init': True,
                              'private': False,
                              'gitignore_template': ''})

    response_create_repository = requests.post(base_url,
                                               data=repo_config,
                                               headers={'Authorization': 'token {}'.format(os.getenv('GITHUB_TOKEN'))})

    print(response_create_repository.status_code)
    print(response_create_repository.json())


# Create a new file inside the repo - PUT
def create_new_file():
    new_file_name = 'github_requests.py'
    new_file_content = f'"""Get, create, update, delete GitHub file/repository"""'
    base_url = f'https://api.github.com/repos/mkatsapova/api-exercises/contents/{new_file_name}'
    base64_string = base64.b64encode(bytes(f'{new_file_content}', 'utf-8'))
    data = {'message': f'Creating the `{new_file_name}` file',
            'content': base64_string.decode('utf-8')}

    response = requests.put(base_url,
                            data=json.dumps(data),
                            headers={'Authorization': 'token {}'.format(os.getenv('GITHUB_TOKEN'))})
    print(response.status_code)
    print(response.json())


# Update the file - PUT
def update_file():
    updating_file_name = 'README.md'
    updating_file_text = 'The repo was created and updated using GitHub API.'
    base_url = f'https://api.github.com/repos/mkatsapova/api-exercises/contents/{updating_file_name}'

    base64_string = base64.b64encode(bytes(f'{updating_file_text}', 'utf-8'))
    data = {'message': f'Creating the `{updating_file_name}` file',
            'content': base64_string.decode('utf-8'),
            'sha': '0a0fe6c23d12e6640f16f242e0d43f196eb93f7f'}
    response = requests.put(base_url,
                            data=json.dumps(data),
                            headers={'Authorization': 'token {}'.format(os.getenv('GITHUB_TOKEN'))})
    print(response.status_code)
    print(response.json())


# Delete the repo - DELETE
def delete_repo():
    name_of_deleting = ''  # enter the repo name
    base_url = f'https://api.github.com/repos/mkatsapova/{name_of_deleting}'
    data = {'message': f'Deleting the `{name_of_deleting}` repo',
            # 'sha': '', instead of id for deleting file
            'id': '749894959'}
    response = requests.delete(base_url,
                               data=json.dumps(data),
                               headers={'Authorization': 'token {}'.format(os.getenv('GITHUB_TOKEN'))})
    print(response.status_code)  # 204 -> 'No content', no JSON


# Delete the file - DELETE
def delete_file():
    name_of_deleting = ''  # enter the deleting file name
    name_repo = ''  # enter the repo name
    base_url = f'https://api.github.com/repos/mkatsapova/{name_repo}/contents/{name_of_deleting}'
    data = {'message': f'Delete the `{name_of_deleting}` file',
            'sha': ''}
    response = requests.delete(base_url,
                               data=json.dumps(data),
                               headers={'Authorization': 'token {}'.format(os.getenv('GITHUB_TOKEN'))})
    print(response.status_code)  # 200
    print(response.json())


if __name__ == '__main__':
    # create_new_repository()
    # get_all_repository()
    # create_new_file()
    # update_file()
    # delete_repo()
    pass
