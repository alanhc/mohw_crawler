from application import app
from crawler import crawler_page
import time
import application
pool_time = 60*30

def serve():
    app.run(host='0.0.0.0', port=8000, debug=False)

def crawl():
    while (1):
        application.data=crawler_page()
        time.sleep(pool_time)

import threading
t1 = threading.Thread(target = serve)
t2 = threading.Thread(target = crawl)

def main():
    t2.start()
    t1.start()

if __name__ == "__main__":
    main()


        
