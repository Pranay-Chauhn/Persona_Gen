from .utils.scrape.url_scraper import extract_username

name = extract_username("https://www.reddit.com/user/jeon_beom/")
print(f'Extracted UserName : {name}')