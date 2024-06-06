import uvicorn
from Services.Aleatoridade import Aleatoridade
from fastapi import FastAPI, Header, Body, Request
app = FastAPI()

@app.post("/Dois_ou_Um")
def sorteio(nomes: list[str] = Body(...)):
    if len(nomes) != 4:
        return {"error": "Você deve fornecer exatamente 4 nomes."}
    return Aleatoridade().Dois_ou_Um(nomes=nomes)

if __name__=="__main__":
    uvicorn.run(app,host='0.0.0.0',port = 8000)