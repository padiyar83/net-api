# Import modules
import requests
import pprint

# Set indentation on pretty print
pp = pprint.PrettyPrinter(indent=2)

# Define base url
url = "http://localhost:5000/"


def nr_inventory_groups_api(url):
    # Define the API path to be tested
    api_path = "api/nr/inventory/groups"
    # Convert dict to json by json.dumps() for body data.
    req = requests.get(url + api_path)
    # Validate response headers and body contents, e.g. status code.
    assert req.status_code == 200
    # req_body = req.json()
    # print full request and response
    # pp.pprint(req)
    # pp.pprint(req_body)


# Execute code
nr_inventory_groups_api(url)