from fastapi import FastAPI

# Inicializa o aplicativo FastAPI
app = FastAPI()

# Cria a rota principal (/)
@app.get("/")
def read_root():
    return {"mensagem": "Hello World"}