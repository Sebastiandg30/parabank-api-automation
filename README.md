🚀 The Big Idea

This project shows a complete QA process I built from scratch for a demo banking app. I started with a manual test strategy, then built an automated safety net for both the backend API (with Postman) and the frontend UI (with Selenium). Finally, I plugged it all into a CI/CD pipeline that runs automatically on every code change.

🛠️ Tech & Skills I Used

Manual & Exploratory Testing to find initial bugs.

API Testing with Postman & Newman.

Performance Testing with JMeter to see if the API could handle pressure.

UI Automation with Selenium, Python & Pytest (using the Page Object Model).

CI/CD with GitHub Actions to automate the whole workflow.

⚙️ How to Run It

API Tests (Newman)
You'll need Node.js/npm. First, npm install -g newman, then run:

newman run "ParaBank API Tests.postman_collection.json" -e "Parabank.postman_environment.json"

UI Tests (Pytest & Selenium)
You'll need Python. Set up a virtual environment (python -m venv venv & activate it), install dependencies (pip install -r requirements.txt), then run the tests with:

pytest

💡 The Plot Twist: When the API and UI Disagreed

This is where the project got really interesting and realistic.

When I tested the login API directly with Postman, it worked perfectly every time, returning a 200 OK status. From a backend perspective, everything looked fine.

But when I wrote a Selenium test to simulate a real user logging in through the website, it always failed.

After debugging, I discovered that the website's frontend code was broken and wasn't handling the login process correctly. This is a classic, real-world bug: the API works, but the user's experience is still broken.

This story shows how critical it is to test at both the API and UI levels. My portfolio demonstrates I can find these kinds of discrepancies and adapt my strategy to test what the user actually experiences.
