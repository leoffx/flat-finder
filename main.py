import scraperClient
import gcloudClient
import emailClient
import json

FILE_NAME = "flats.json"


def find_new_postings():
    new_postings = {}
    for url in postings:
        new_postings[url] = []
        for headline in postings[url]:
            if headline not in seen_postings:
                new_postings[url].append(headline)

    return new_postings


def compose_email(posts):
    # Stringify dict
    email_body = ""

    for url in posts:
        if not posts[url]:
            continue
        for headline in posts[url]:
            email_body += headline + "\n"
        email_body += url + "\n"

    return email_body


if __name__ == "__main__":

    # Initialize clients
    scraper = scraperClient.ScraperClient()
    gcloud = gcloudClient.GcloudClient()
    email = emailClient.EmailClient()

    # Scrape websites
    postings = scraper.get_postings()

    # Download database and load it
    gcloud.download_file(FILE_NAME)
    try:
        with open(FILE_NAME) as f:
            seen_postings = json.load(f)
    except Exception as e:
        print("No seen postings found ", e)
        seen_postings = []

    # Check new results
    new_postings = find_new_postings()

    email_body = compose_email(new_postings)

    # If any, update database and send emails
    new_posting_titles = [item for sublist in list(
        new_postings.values()) for item in sublist]
    if len(new_posting_titles):
        with open(FILE_NAME, "w+") as f:
            json.dump(seen_postings + new_posting_titles, f)

        email.send_emails(new_posting_titles[0], email_body)
        gcloud.upload_file(FILE_NAME)
