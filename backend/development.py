from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response, JSONResponse
import httpx
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Reverse proxy to localhost:8080
@app.middleware("http")
async def proxy_to_localhost(request: Request, call_next):
    try:
        # Build target URL to localhost:8080
        target_url = f"http://127.0.0.1:8080{request.url.path}"
        if request.url.query:
            target_url += f"?{request.url.query}"
        
        logger.info(f"Proxying {request.method} {request.url.path} -> {target_url}")
        
        # Forward the request to localhost:8080
        async with httpx.AsyncClient(timeout=30.0) as client:
            # Get request body
            body = await request.body()
            
            # Prepare headers (remove host header to avoid conflicts)
            headers = dict(request.headers)
            headers.pop('host', None)
            
            # Forward request
            response = await client.request(
                method=request.method,
                url=target_url,
                headers=headers,
                content=body,
                follow_redirects=True
            )
            
            logger.info(f"Response status: {response.status_code}")
            
            # Return the response from localhost:8080
            return Response(
                content=response.content,
                status_code=response.status_code,
                headers=dict(response.headers),
            )
            
    except httpx.ConnectError as e:
        logger.error(f"Connection error: {e}")
        return JSONResponse(
            status_code=502,
            content={"error": "Cannot connect to backend server on 127.0.0.1:8080"}
        )
    except Exception as e:
        logger.error(f"Proxy error: {e}", exc_info=True)
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=443,
        ssl_keyfile="/etc/letsencrypt/live/webstore.fluxapp.co/privkey.pem",
        ssl_certfile="/etc/letsencrypt/live/webstore.fluxapp.co/fullchain.pem"
    )