import pdfkit

def extract_website(url, filename):
    pdfkit.from_url(url, "temp/%s.pdf" % filename)

def extract_youtube(url, filename):
    # todo
    pass
