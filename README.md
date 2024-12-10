# Car Dealership Web App

This project implements a car dealership web application utilizing a **microservices architecture**.

## Key Features

- **Microservices Architecture:**

  - **Node.js API:**
    - Handles all car-related operations:
      - Fetches all cars from the dealership.
      - Registers new car models.
      - Stores and retrieves car reviews.
      - Uses MongoDB for data persistence.
      - Dockerized and deployed on OpenShift.
  - **Django Server:**
    - Primary server for user interactions.
    - Handles user registration and login.
    - Renders static pages.
    - Routes requests to React frontend and Node.js API.
    - Utilizes Django ORM for user and car model management.
  - **Flask Sentiment Analysis API:**
    - Dockerized and deployed as a separate service.
    - Analyzes user reviews to determine sentiment (positive, neutral, negative).
    - Provides sentiment analysis results to the Django server.

- **React Frontend:**

  - Dynamically renders user interfaces for specific pages.
  - Seamlessly integrates with the Django server and Node.js API.

- **GitHub Actions:**

  - Automated workflow for continuous integration and continuous deployment (CI/CD).
  - Ensures smooth and reliable updates to the application.

- **User-Friendly Interface:**
  - Browse available dealerships and their services.
  - Leave reviews for dealerships.
  - View reviews and sentiment analysis results.

## Technology Stack

- **Frontend:** React
- **Backend:** Django, Node.js, Flask
- **Database:** MongoDB
- **Containerization:** Docker
- **Deployment:** OpenShift
- **Cloud Services:** Code engine
- **CI/CD:** GitHub Actions

## Project Structure

```
 car_dealership_app/
├── dealership_api/  # Node.js API
│   ├── server.js
│   ├── models/
│   ├── controllers/
│   ├── routes/
│   ├── Dockerfile
│├── django_server/
│   ├── manage.py
│   ├── apps/
│   │   ├── users/
│   │   ├── cars/
│   │   ├── reviews/
│   ├── templates/
│   ├── static/
│   ├── settings.py
│   ├── urls.py
│   ├── requirements.txt
│├── flask_sentiment_analyzer/
│   ├── app.py
│   ├── Dockerfile
│├── react_frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│├── github_workflows/
│   ├── ci.yml
│   ├── cd.yml
│├── README.md
│├── requirements.txt
```

## Getting Started

1. **Clone the repository:**

   ````bash
   git clone <repository_url>
   Install dependencies:```

   ````

2. **Install dependencies:**

```bash
cd dealership_api && npm install
cd ../django_server && pip install -r requirements.txt
cd ../flask_sentiment_analyzer && pip install -r requirements.txt
cd ../react_frontend && npm install
Start development servers:
```

3. **Start development servers:**

- **Node.js API**: npm start
- **Django Server**: python manage.py runserver
- **Flask Sentiment Analyzer**: flask run
- **React Frontend**: npm start
- **Access the application**:

4. **Access the application:**

- Open your web browser and navigate to `http://localhost:8000` (or the appropriate port).
