from starlette.datastructures import FormData

def request_treatment(data: FormData) -> dict:
    format_data = {}
    for key, value in data.items():
        format_data.update({key: value})
    return format_data