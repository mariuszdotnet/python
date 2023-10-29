import requests

response = requests.get('http://gitlab.com/api/v4/users/nanuchi/projects')

my_projects = response.json()

for project in my_projects:
    print(f"Project Name: {project['name']} Project URL: {project['web_url']}")
