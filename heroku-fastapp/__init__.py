import uvicorn
from app.fastapp import app

# Main dirver function
if __name__=='__main__':
    uvicorn.run(app)