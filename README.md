# build-and-deploy-the-chatbot-lp-author
Repository for liveProject: Build and Deploy the Chatbot


### Part 1: Deploy the LangServe server

You need to have the `chroma_db` database from the previous project. Then you can run the following command to deploy the LangServe server:

```bash
python server.py
```

You can then connect to the [server](http://localhost:8080/docs) and test the endpoints.
```bash


### Part 2: Build a chatbot with Streamlit

You can run the following command to start the chatbot:

```bash
streamlit run ui.py
```


### Part 3: Deploy to Streamlit Cloud

You can deploy the chatbot to Streamlit Cloud by makging sure your streamlit file is in a public repo.
You then need to create a new app on Streamlit Cloud and connect it to your repo.

You also need to use ngrok to give access the port your LangServe app is running on

My bot is available on [https://mychattybox.streamlit.app/](https://mychattybox.streamlit.app/)
