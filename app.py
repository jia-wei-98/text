#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, request, render_template


# In[2]:


app = Flask(__name__)


# In[3]:


from textblob import TextBlob

@app.route ("/", methods = ["GET","POST"])
def index():
    if request.method == "POST":
        text = request.form.get("text")
        analysis = TextBlob(text)
        print (analysis.sentiment)
        output = analysis.sentiment
        return (render_template("index.html", badabing = output))
    else:
        return (render_template("index.html", badabing = "2"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:




