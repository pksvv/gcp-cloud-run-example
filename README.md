# 🚀 Deploy and Destroy a FastAPI CRUD App on Google Cloud Run

This guide explains how to build, deploy, and later clean up a simple FastAPI CRUD API using Google Cloud Run.

---

## 📂 Project Structure

crud-notes/  
 ├── main.py  
 ├── requirements.txt  
 └── Dockerfile  

---

## 1. ✨ FastAPI App (CRUD Example)

- main.py contains CRUD endpoints:
  - GET / → Health message
  - POST /notes/{note_id} → Create a note
  - GET /notes/{note_id} → Read a note
  - PUT /notes/{note_id} → Update a note
  - DELETE /notes/{note_id} → Delete a note

---

## 2. 📦 Requirements

requirements.txt should include:
- fastapi  
- uvicorn  

---

## 3. 🐳 Dockerfile

Dockerfile steps:  
1. Use base image python:3.11-slim  
2. Set working directory /app  
3. Copy requirements.txt  
4. Install dependencies with pip  
5. Copy source code  
6. Run the app with uvicorn main:app --host 0.0.0.0 --port 8080  

---

## 4. 🖥 Local Setup & Testing

1. Create and activate virtual environment  
2. Install dependencies using pip install -r requirements.txt  
3. Run the app locally using uvicorn main:app --reload  
4. Test in browser at http://127.0.0.1:8000  
5. API docs available at http://127.0.0.1:8000/docs  

---

## 5. ⚙️ Google Cloud Project Setup

1. Create a new project in Google Cloud Console  
2. Link a billing account  
3. Enable APIs: run.googleapis.com, cloudbuild.googleapis.com, artifactregistry.googleapis.com  

---

## 6. 📤 Build & Push Docker Image

From your project folder, run:  
gcloud builds submit --tag gcr.io/PROJECT_ID/crud-notes  

This uploads your source, builds a Docker image, and pushes it to Google’s container registry.  

---

## 7. 🚀 Deploy to Cloud Run

Deploy the image with:  
gcloud run deploy crud-notes --image gcr.io/PROJECT_ID/crud-notes --platform managed --region asia-south1 --allow-unauthenticated  

After deployment, you’ll get a public URL like:  
https://crud-notes-xyz-uc.a.run.app  

---

## 8. 🔍 Test the API

- Health check: curl https://SERVICE_URL/  
- API Docs: open https://SERVICE_URL/docs  

---

## 9. 🧪 CRUD Operations (Examples)

- Create: POST /notes/1 with body {"title":"First Note","content":"Hello"}  
- Read: GET /notes/1  
- Update: PUT /notes/1 with new JSON body  
- Delete: DELETE /notes/1  

---

## 10. 🗑 Destroy / Cleanup

1. Delete Cloud Run service:  
   gcloud run services delete crud-notes --region asia-south1 --platform managed  

2. Delete container image from registry:  
   gcloud container images delete gcr.io/PROJECT_ID/crud-notes --force-delete-tags --quiet  

3. Verify cleanup:  
   gcloud run services list --region asia-south1  
   gcloud container images list  

---

## ✅ Summary

You have:  
- Built a FastAPI CRUD app  
- Containerized it with Docker  
- Deployed it on Cloud Run  
- Accessed it via a public URL  
- Learned how to safely destroy it after use  