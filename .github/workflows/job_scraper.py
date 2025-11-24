import requests
from bs4 import BeautifulSoup

def fetch_jobs():
    urls = [
        "https://www.indeed.com/jobs?q=Software+Tester&l=India",
        "https://www.indeed.com/jobs?q=QA+Analyst&l=India",
        "https://www.naukri.com/software-testing-jobs",
        "https://www.naukri.com/qa-analyst-jobs",
        "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=software+testing&txtLocation="
    ]

    all_jobs = []

    for url in urls:
        try:
            headers = {"User-Agent": "Mozilla/5.0"}
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, "html.parser")

            # -----------------------------
            # INDEED
            # -----------------------------
            if "indeed" in url:
                cards = soup.find_all("div", class_="jobsearch-SerpJobCard")
                for job in cards[:10]:
                    title = job.find("a").get_text(strip=True)
                    link = "https://www.indeed.com" + job.find("a")["href"]
                    company = job.find("span", class_="company")
                    company = company.get_text(strip=True) if company else "Company Not Listed"

                    all_jobs.append(f"**{title}** at {company}\n{link}\n")

            # -----------------------------
            # NAUKRI
            # -----------------------------
            elif "naukri" in url:
                cards = soup.find_all("article", class_="jobTuple")
                for job in cards[:10]:
                    title = job.find("a", class_="title").get_text(strip=True)
                    company = job.find("a", class_="subTitle").get_text(strip=True)
                    link = job.find("a", class_="title")["href"]

                    all_jobs.append(f"**{title}** at {company}\n{link}\n")

            # -----------------------------
            # TIMESJOBS
            # -----------------------------
            elif "timesjobs" in url:
                cards = soup.find_all("li", class_="clearfix job-bx")
                for job in cards[:10]:
                    title = job.find("h2").get_text(strip=True)
                    company = job.find("h3", class_="joblist-comp-name").get_text(strip=True)
                    link = job.find("a")["href"]

                    all_jobs.append(f"**{title}** at {company}\n{link}\n")

        except:
            continue

    return "\n".join(all_jobs) if all_jobs else "No jobs found today."

if __name__ == "__main__":
    jobs = fetch_jobs()
    print(jobs)

