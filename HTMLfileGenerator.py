"""HTML file generator
By Marti157
Very simple. May add an image option."""

import time

def Start():
    print "\n"
    print "Please type a title for your"
    print "website (maximum 15 characters)"
    print "\n"
    title = raw_input()
    title = str(title)
    print "\n"
    titleLength = len(title)
    if titleLength > 15:
        time.sleep(0.5)
        print "The title has to be less that 15 characters!"
        print "\n"
        Start()
    else:
        time.sleep(0.5)
        print "Ok."
        time.sleep(0.5)
        print "Now type a line of text (maximum 50 characters)"
        time.sleep(0.3)
        print "We only support one at the moment."
        print "\n"
        text = raw_input()
        text = str(text)
        textLength = len(text)
        if textLength > 50:
            print "\n"
            print "The text has to be less than 50 characters!"
            print "\n"
            Start()
        else:
            print "\n"
            time.sleep(0.5)
            print "Ok."
            time.sleep(0.5)
            print "\n"
            print "Converting..."
            time.sleep(0.7)
            print "\n"
            print "Done."
            print "\n"
            time.sleep(0.3)
            print "Choose file name for the output:"
            print "\n"
            fileName = raw_input()
            fileName = str(fileName)
            filenameLength = len(fileName)
            if filenameLength < 100:
                print "\n"
                htmlString =  "<html>\n  <header>\n    <title>" + title + "</title>\n  </header>\n  <body>\n    <p>" + text + "</p>\n  </body>\n</html>"
                print "Saving..."
                importedFile = open(fileName + ".html", "w")
                importedFile.write(htmlString)
                importedFile.close()
                time.sleep(0.5)
                print "Saved."
                print "\n"
                print "File name:"
                print fileName + ".html"
                time.sleep(2)
                print "\n"
                print "To start again, press any key"
                print "\n"
                raw_input()
                Start()
            else:
                print "File name length is too big. Please,"
                print "choose another location."
                Start()

print "\n"
print "                          Simple HTML file generator"
print "                                 By Marti157"
print "\n"
time.sleep(1)
Start()
