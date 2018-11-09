from pywebcopy import save_webpage

def extract_website_zip(url, key):
    filename = '%s.zip' % key
    try:
        save_webpage(
            url,
            project_folder='temp',
            project_name=key,
            zip_project_folder=True,
            delete_project_folder=True,
        )
        return filename
    except Exception as e:
        print(e)
        return False
