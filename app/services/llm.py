import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def categorize_applicant(job, applicant):
    prompt = f"""
Job Description:
{job['description']}

Selection Criteria:
Required Skills: {job['required_skills']}
Experience: {job['experience']}

Resume:
Name: {applicant['name']}
Skills: {', '.join(applicant['skills'])}
Experience: {applicant['experience']}
Education: {applicant['education']}

Based on the above, categorize the applicant as "Good Fit", "Maybe Fit", or "Not a Fit".
Also provide a short summary of the reasoning.
Return in this format:
Category: <category>
Summary: <summary>
"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or "gpt-4"
        messages=[{"role": "user", "content": prompt}]
    )

    content = response['choices'][0]['message']['content']
    lines = content.strip().split("\n")
    category = lines[0].split(": ")[1]
    summary = lines[1].split(": ")[1]
    return category, summary
