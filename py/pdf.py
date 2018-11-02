import pdfkit

def extract_website(url, key):
    filename = "%s.pdf" % key
    try:
        pdfkit.from_url(url, "temp/%s" % filename)
        return filename
    except Exception as e:
        print(e)
        return False
