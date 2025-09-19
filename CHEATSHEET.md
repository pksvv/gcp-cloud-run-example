# 🚀 FastAPI on Google Cloud Run — Quick Cheat Sheet

---

## 🔧 Setup

1. Create a new GCP project (example: NewAgent).
2. Link billing account.
3. Enable APIs:  
   gcloud services enable run.googleapis.com cloudbuild.googleapis.com artifactregistry.googleapis.com

---

## 🖥 Local Test

- Install dependencies: pip install -r requirements.txt  
- Run locally: uvicorn main:app --reload  
- Test: http://127.0.0.1:8000/docs  

---

## 📤 Build & Push

From project folder:  
gcloud builds submit --tag gcr.io/PROJECT_ID/crud-notes  

---

## 🚀 Deploy

Deploy service:  
gcloud run deploy crud-notes --image gcr.io/PROJECT_ID/crud-notes --platform managed --region asia-south1 --allow-unauthenticated  

Copy the generated URL, example: https://crud-notes-xyz.a.run.app  

---

## 🔍 Test

- Health check: curl https://SERVICE_URL/  
- API docs: https://SERVICE_URL/docs  
- CRUD:  
  - Create: POST /notes/1  
  - Read: GET /notes/1  
  - Update: PUT /notes/1  
  - Delete: DELETE /notes/1  

---

## 🗑 Cleanup

1. Delete Cloud Run service:  
   gcloud run services delete crud-notes --region asia-south1 --platform managed  

2. Delete image from registry:  
   gcloud container images delete gcr.io/PROJECT_ID/crud-notes --force-delete-tags --quiet  

3. Verify cleanup:  
   gcloud container images list-tags gcr.io/PROJECT_ID/crud-notes  
   (should return empty)  

---

## ✅ Summary

- Local dev → Test with uvicorn  
- Build → gcloud builds submit  
- Deploy → gcloud run deploy  
- Test → Public URL + /docs  
- Destroy → delete service + delete image  