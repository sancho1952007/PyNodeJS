def require(module):
    return __import__(module)

class console:
    def log(text):
        print(text)