from pytest_bdd import when, scenarios

from utils.utils import (
    post_request,
    get_request,
    put_request,
    delete_request,
    read_file,
)

scenarios("sample.feature")


@when("I send a POST HTTP request with <payload>")
def send_post_request(context, payload, set_headers, set_api_endpoint):
    request_body = read_file(payload)
    post_response = post_request(
        api_endpoint=set_api_endpoint, payload=request_body, headers=set_headers
    )
    context["post_response"] = post_response.json()
    context["post_status_code"] = post_response.status_code


@when("I send a GET HTTP request")
def send_get_request(context, set_headers, set_api_endpoint):
    get_response = get_request(api_endpoint=set_api_endpoint, headers=set_headers)
    context["get_response"] = get_response.json()
    context["get_status_code"] = get_response.status_code


@when("I send a PUT HTTP request with <payload>")
def send_put_request(context, payload, set_headers, set_api_endpoint):
    request_body = read_file(payload)
    put_response = put_request(
        api_endpoint=set_api_endpoint, payload=request_body, headers=set_headers
    )
    context["put_response"] = put_response.json()
    context["put_status_code"] = put_response.status_code


@when("I send a DELETE HTTP request")
def send_delete_request(context, set_headers, set_api_endpoint):
    delete_response = delete_request(api_endpoint=set_api_endpoint, headers=set_headers)
    context["delete_response"] = delete_response.json()
    context["delete_status_code"] = delete_response.status_code
