

\# React + FastAPI User Details Application



\## Project Description



A simple web application built using React and FastAPI.

Users can enter their name and email address.

The frontend sends the details to the backend using REST API.

The backend validates the details and returns a JSON response.



\## Technologies Used



\- React

\- Vite

\- JavaScript

\- Python

\- FastAPI

\- Pydantic

\- Uvicorn



\## Project Structure



react-fastapi-project/

&#x20; frontend/

&#x20; backend/

&#x20;   main.py

&#x20;   requirements.txt

&#x20; README.md



\## Backend Setup



1\. Navigate to the backend folder.



&#x20;  cd backend



2\. Create virtual environment.



&#x20;  python -m venv venv



3\. Activate virtual environment.



&#x20;  venv\\Scripts\\activate



4\. Install dependencies.



&#x20;  pip install -r requirements.txt



5\. Start backend server.



&#x20;  uvicorn main:app --reload



Backend URL:

http://127.0.0.1:8000



API Documentation:

http://127.0.0.1:8000/docs



\## Frontend Setup



1\. Navigate to frontend folder.



&#x20;  cd frontend



2\. Install dependencies.



&#x20;  npm install



3\. Start React application.



&#x20;  npm run dev



Frontend URL:

http://localhost:5173



\## API Endpoints



\### GET /api/health



Checks backend status.



\### POST /api/submit



Accepts name and email and returns confirmation.



Example request:



{

&#x20; "name": "Alex",

&#x20; "email": "alex@example.com"

}



\## Features



\- User name and email form

\- Basic form validation

\- REST API integration

\- Pydantic validation

\- Loading and error handling

\- Success response display



