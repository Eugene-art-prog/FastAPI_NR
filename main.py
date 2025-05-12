from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# Разрешить запросы с вашей Tilda-страницы
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    
	#allow_origins=[
     #   "https://project9935365.tilda.ws",
        # если вы тестируете локально через облачный Tunnel, можно временно:
      #  "*"    ],
    
	allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)





@app.get("/users")
async def get_users():
    return [{"id": 1, "name": "Artem"}]

if __name__ == "__main__":
#     pass 

	uvicorn.run("main:app", host="0.0.0.0")
