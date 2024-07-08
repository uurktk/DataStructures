class Codec:

    def __init__(self):
        self.hashMap = {}

    def encode(self, longUrl: str) -> str:
        hashCode = hash(longUrl)
        self.hashMap[hashCode] = longUrl

        return f"http://tinyurl.com/{hashCode}"

    def decode(self, shortUrl: str) -> str:
        hashCode = int(shortUrl[19::])
        return self.hashMap.get(hashCode)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))