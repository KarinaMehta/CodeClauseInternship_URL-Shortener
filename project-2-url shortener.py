class URLShortener:

    def __init__(self):
        self.url_mapping = {}
        self.counter = 1

    def shorten_url(self, long_url):
        short_url = f"http://short.url/{self.counter}"
        self.url_mapping[short_url] = long_url

        self.counter += 1

        return short_url

    def expand_url(self, short_url):
        try:
            counter = int(short_url.split("/")[-1])
        except ValueError:
            return "Invalid URL"
        long_url = self.url_mapping.get(short_url, None)

        if long_url:
            return long_url
        else:
            return "Not found"

if __name__ == "__main__":
    shortener = URLShortener()
    long_url = input("Enter the big URL to make short: ")
    shortened_url = shortener.shorten_url(long_url)
    print(f"Short URL: {shortened_url}")

    
