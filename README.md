# GOOSETHINGS

### To install:
Run the following in the command line:  

```git clone https://github.com/jonathan-conroy/goosethings.git```  

Navigate to the newly-created `goosethings` folder (using `cd`).  
Check that the command `python --version` is Python 3.  

```python -m pip install -r requirements.txt```

To finish setup, open `main.py` and edit the three global variables. (As is hopefully obvious, `DOWNLOADS` should contain the filepath to the Downloads folder, and `OUTPUT_FOLDER` should contain the filepath to whichever folder you want to contain the output...) `NUM_FILES` is the number of articles that will be parsed, as explained below.

---

### To run:
Open the news articles in a browser; save the HTML to the Downloads folder (on Firefox, the shortcut is just `cmd-s`, and it should be saved as "Web Page, HTML only" or perhaps "Web Page, complete"). Running `python main.py` will look at the most recently modified files in `DOWNLOADS`; it will attempt to parse the most recent `NUM_FILES` of them and save the output as a word document.

**Currently supported sites:**
- Washington Post  
  (Hopefully, this works)
- New York Times  
  (Some headers may be incorrectly removed, but they will probably be marked as "Removed")
- Wall Street Journal  
   (This one has some issues with detecting the end of the article, but this is fixable manually)
- The Hill  
    (Basically untested)