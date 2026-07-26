import requests

def get_pageviews(topic):
    url = f"https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/all-agents/{topic}/monthly/2025010100/2025123100"
    headers = {"User-Agent": "HigherLowerGame/1.0 (your-email@example.com)"}
    response = requests.get(url, headers=headers)
    data = response.json()
    total_views = sum(item['views'] for item in data['items'])
    return total_views

if __name__ == "__main__":
    print(get_pageviews("Cristiano_Ronaldo"))
    print(get_pageviews("Lionel_Messi"))



topics = [
    {"slug": "Cristiano_Ronaldo", "name": "Cristiano Ronaldo", "description": "a football player from Portugal"},
    {"slug": "Lionel_Messi", "name": "Lionel Messi", "description": "a football player from Argentina"},
    {"slug": "Elon_Musk", "name": "Elon Musk", "description": "a businessman from South Africa"},
    {"slug": "Taylor_Swift", "name": "Taylor Swift", "description": "a singer from the United States"},
    {"slug": "Rihanna", "name": "Rihanna", "description": "a singer from Barbados"},
    {"slug": "Barack_Obama", "name": "Barack Obama", "description": "a former US president"},
    {"slug": "Beyoncé", "name": "Beyoncé", "description": "a singer from the United States"},
    {"slug": "LeBron_James", "name": "LeBron James", "description": "a basketball player from the United States"},
    {"slug": "Kim_Kardashian", "name": "Kim Kardashian", "description": "a media personality from the United States"},
    {"slug": "Bill_Gates", "name": "Bill Gates", "description": "a businessman from the United States"},
    {"slug": "Dwayne_Johnson", "name": "Dwayne Johnson", "description": "an actor from the United States"},
    {"slug": "Drake_(musician)", "name": "Drake", "description": "a rapper from Canada"},
    {"slug": "Selena_Gomez", "name": "Selena Gomez", "description": "a singer and actress from the United States"},
    {"slug": "Kanye_West", "name": "Kanye West", "description": "a rapper from the United States"},
    {"slug": "Emma_Watson", "name": "Emma Watson", "description": "an actress from the United Kingdom"},
    {"slug": "Neymar", "name": "Neymar", "description": "a football player from Brazil"},
    {"slug": "Ariana_Grande", "name": "Ariana Grande", "description": "a singer from the United States"},
    {"slug": "Mark_Zuckerberg", "name": "Mark Zuckerberg", "description": "a businessman from the United States"},
    {"slug": "Justin_Bieber", "name": "Justin Bieber", "description": "a singer from Canada"},
    {"slug": "Serena_Williams", "name": "Serena Williams", "description": "a tennis player from the United States"},
]