# Content Planner

Capture, organize, and track your content ideas.  
Move smoothly from draft to published.

---

## Track Chosen + Why
**Track A — Content Scratchpad + Planning Queue**

I chose this track because content planning is a real-world problem faced by creators and teams. It allowed me to demonstrate a complete full-stack workflow with clean UI and REST APIs.

---

## Features Implemented
- Create content ideas
- List all ideas
- Update ideas (title, description, status)
- Delete ideas with confirmation
- Track workflow: Draft → Scheduled → Published
- Optional scheduled publish date
- Clean and consistent HTML/CSS UI
- REST API for full CRUD operations

---

## Tech Stack
- Backend: Python, Django, Django REST Framework
- Frontend: HTML, CSS
- Database: SQLite
- Version Control: Git, GitHub

---

## How to Run Locally

```bash
git clone https://github.com/SathiyasriRaman/content-planner.git
cd content-planner
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Open in browser:
```
http://127.0.0.1:8000/
```

---

## API Endpoints
- GET /api/ideas/ – List all ideas
- POST /api/ideas/ – Create a new idea
- GET /api/ideas/{id}/ – Get a single idea
- PATCH /api/ideas/{id}/ – Update an idea
- DELETE /api/ideas/{id}/ – Delete an idea

---

## Data Model

**Idea**
- title
- description
- status (draft / scheduled / published)
- scheduled_date (optional)
- created_at

---

## AI Collaboration Log

**AI Tool Used:** ChatGPT

**How it helped:**
- Assisted in structuring Django views and REST APIs
- Helped design a clean, minimal HTML/CSS UI
- Suggested realistic content-planning examples
- Helped improve UI consistency and workflow clarity

**Example Prompt:**
```
Build a simple full-stack Django content planner with CRUD operations and clean UI.
```

**Correction / Refactor Example:**
- Refactored the delete confirmation page to match the overall UI for consistency and better user experience.

---

## Trade-offs & Next Improvements
- Add user authentication for multiple users
- Filter ideas by status and scheduled date
- Add pagination for large datasets
- Deploy the application to a cloud platform

---

## Sample Data
- Instagram carousel: What is a REST API?
- YouTube video: How a full-stack app works
- Blog post: Django vs MERN stack
- Product launch announcement

---

## Screenshots
UI screenshots are available in the `screenshots/` folder.
