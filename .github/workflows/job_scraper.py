import requests
from bs4 import BeautifulSoup

def fetch_jobs():
    urls = [
        "https://www.linkedin.com/jobs/search/?keywords=Software%20Testing&location=India&f_E=2",
        "https://www.linkedin.com/jobs/search/?keywords=QA%20Analyst&location=India&f_E=2",
    ]

    all_jobs = []

    for url in urls:
        try:
            headers = {"User-Agent": "Mozilla/5.0"}
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, "html.parser")

            job_cards = soup.find_all("div", class_="base-card")

            for job in job_cards[:10]:
                title = job.find("h3").get_text(strip=True)
                company = job.find("h4").get_text(strip=True)
                link = job.find("a")["href"]

                all_jobs.append(f"**{title}** at *{company}*\n{link}\n")
        except:
            continue

    return "\n".join(all_jobs) if all_jobs else "No jobs found today."

if __name__ == "__main__":
    jobs = fetch_jobs()
    print(jobs)
