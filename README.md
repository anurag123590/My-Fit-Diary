# FitDiary - Fitness Tracking Web Application

**FitDiary** is a fitness tracking web application that allows users to monitor their fitness journey, form workout groups, and track progress. The project combines a FastAPI backend with a Bootstrap-enhanced frontend for a seamless and responsive user experience.

## Features

- **User Registration**: Secure user registration and profile management using FastAPI and PostgreSQL.
- **Group Creation**: Users can create workout groups, invite members by phone number, and track group progress.
- **Post Creation**: Users can share posts about their fitness activities and progress within their groups.
- **Daily Questions**: The app provides a feature where users can answer daily fitness-related questions to track their habits.

## API Endpoints

- `POST /register/`: Register a new user.
- `POST /create_group/`: Create a new workout group and invite members.
- `POST /posts/`: Create a new post about fitness activities.
- `POST /daily_questions/`: Add daily questions to track habits and progress.

## Tech Stack

- **Backend**: FastAPI, SQLAlchemy, PostgreSQL
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: PostgreSQL
- **Other Tools**: Docker, Git

## How to Run

1. Clone the repository:
   
   ```bash
   git clone https://github.com/your-username/your-repo-name.git

2. Set up a virtual environment:
   
bash
python3 -m venv myenv
source myenv/bin/activate   # For Windows: myenv\Scripts\activate

3. Install dependencies:

bash
pip install -r requirements.txt

4. Run the application:

bash
uvicorn main:app --reload


Screenshots
<img src="static/diagram1.jpg" alt="Health Diagram" width="200"> <img src="static/diagram2.jpg" alt="Workout Progress" width="200">
License
This project is licensed under the MIT License.


**Make sure to replace `https://github.com/your-username/your-repo-name.git` with your actual GitHub repository link.









