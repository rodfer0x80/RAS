import sys
import os

from .app import app


class Server:
    def __init__(self, scrapper, parser):
        self.scrapper = scrapper
        self.parser = parser
        self.running = False
        return None

    def runScrapper(self):
        self.scrapper.runme()
        return 0

    def runParser(self):
        self.parser.runme()
        return 0

    def start(self):
        fl = open("links.txt", 'w')
        fl.write("")
        fl.close()
        fq = open("questions.txt", 'w')
        fq.write("")
        fq.close()
        #os.chdir("src/")
        try:
            self.running = True
            app.run(debug=True)
        except:
            return 2
        return 0

    def stop(self):
        try:
            self.running = False
            app.stop(debug=True)
        except:
            return 3
        return 0

    