from fastapi import FastApi

app = FastApi();

@app.get("/health")
async def getHealth ():
    return Response(content="pong", status_code=200, media_type="text/plain")
