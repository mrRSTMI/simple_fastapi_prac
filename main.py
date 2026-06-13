from fastapi import FastAPI
# from controllers.admin_route import router
from scalar_fastapi import get_scalar_api_reference
from routes.admin_route import router


app = FastAPI(docs_url=None, redoc_url=None)

app.include_router(router=router)



@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():

    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API ",
    )

