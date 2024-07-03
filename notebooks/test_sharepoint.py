# %%
import os
from pathlib import Path
from pprint import pformat, pprint

import requests

# %%
# sharepoint site URL & doc path
site_url = "https://pmiorg0.sharepoint.com/sites/DigitalServicesSolutions/"
doc_path = Path("Shared Documents/Data Science/Project Documentation/Segmentation/test.docx")

# sharepoint API endpoint
api_url = site_url + "/_api/sites/"
#  api_urlv2 = site_url + "/_api/v2.0/sites/"
api_url_call = api_url + f"GetFileByServerRelativeURL('{doc_path}')/$value"

# %%
# sharepoint auth
username = "agraber"
password = "pmiJune2023"


# %%
# use token auth?
tenant_name = "efa022f4-2c02-46d8-b614-1b43989d652f"
# tenant_id="7a351b06-8a3a-42f7-a6c4-335039deaac8"
tenant_id = "416261b4-2ea3-49c4-ad07-286e0e89585c"
requests.post(
    f"https://login.microsoftonline.com/{tenant_name}/oauth2/v2.0/token",
    data={
        "header": "Content-Type: application/x-www-form-urlencoded",
        "client_id": tenant_id,
        "grant_type": "authorization_code",
    },
)

# %%
# send API request
response = requests.get(
    api_url,
    auth=(username, password),
    timeout=30,
)

# %%
print(response.status_code)

# %%
pprint(response.content)
