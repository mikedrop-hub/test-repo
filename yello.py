#This whole module is completely unnecessary bytheway
import wikipediaapi as wiki


def only_function():
    wiki_wiki = wiki.Wikipedia('MyProjectName (merlin@example.com)', 'en')
    page_py = wiki_wiki.page('Python_(programming_language)')
    print("Page - Title: %r" % page_py.title)
    # Page - Title: Python (programming language)

    print("Page - Summary: %r" % page_py.summary)
    # Page - Summary: Python is a widely used high-level programming language for
    return True
