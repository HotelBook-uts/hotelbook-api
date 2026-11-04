from fastapi import FastAPI

app = FastAPI(
    title="HotelBook API",
    description="Sistema de reservas hoteleras",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "HotelBook API funcionando"
    }
