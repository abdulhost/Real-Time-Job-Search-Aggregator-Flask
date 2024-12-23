from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Example API URL (use actual job API URL here, like Indeed, Glassdoor, etc.)
JOB_API_URL = "https://api.example.com/jobs"  # Replace with a real API URL

# Function to fetch job data (replace this with real API call)
def get_job_listings(location=None, salary=None, industry=None):
    params = {}
    if location:
        params["location"] = location
    if salary:
        params["salary"] = salary
    if industry:
        params["industry"] = industry
    
    # Making a GET request to the job API (dummy response here)
    response = requests.get(JOB_API_URL, params=params)
    if response.status_code == 200:
        return response.json()  # Assume the API returns a JSON response
    else:
        return []  # Return an empty list in case of error

# Route to render the homepage with job listings
@app.route('/', methods=['GET', 'POST'])
def index():
    # Default values
    location = request.form.get('location', '')
    salary = request.form.get('salary', '')
    industry = request.form.get('industry', '')
    
    # Fetch job listings from API
    job_listings = get_job_listings(location, salary, industry)
    
    return render_template('index.html', jobs=job_listings)

if __name__ == "__main__":
    app.run(debug=True)
