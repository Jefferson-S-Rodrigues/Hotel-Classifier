from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


def jsonc(item, cod=200):
    json_compatible_item_data = jsonable_encoder(item)
    return JSONResponse(
        content=json_compatible_item_data,
        media_type="application/json",
        status_code=cod
    )
