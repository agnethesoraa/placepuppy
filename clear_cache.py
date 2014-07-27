from cache import cache
from views import app


def main():
    cache.init_app(app)
    with app.app_context():
        cache.clear()
        print "Cleared cache"

if __name__ == '__main__':
    main()
