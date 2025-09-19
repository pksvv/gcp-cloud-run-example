# 🚀 FastAPI CRUD on Google Cloud Run — Full Cheat Sheet (with Fixes)

---

## 🔧 Initial Setup

1. **Check active project**
   gcloud config list project  

   If not correct, set your project:  
   gcloud config set project PROJECT_ID  

---

## 👤 Account & Permissions

- **Check active account**
  gcloud auth list  

- If wrong account is active, switch:  
  gcloud config set account YOUR_EMAIL  

- If account not logged in, add:  
  gcloud auth login YOUR_EMAIL  

- **Check IAM role (should be Owner/Editor)**
  gcloud projects get-iam-policy PROJECT_ID  

---

## 💳 Billing Checks

- **Check if billing is linked**
  gcloud beta billing projects describe PROJECT_ID  

  → Should show `billingEnabled: true`  

- If `billingEnabled: false`, then:  
  1. Go to Google Cloud Console → Billing  
  2. Create/select a billing account  
  3. Link it to your project  

- **Enable Cloud Billing API (sometimes needed)**  
  gcloud services enable cloudbilling.googleapis.com  

---

## ⚙️ Enable Required APIs

gcloud services enable run.googleapis.com cloudbuild.googleapis.com artifactregistry.googleapis.com  

Common Error:  
- *"Billing account for project not found"* → means billing not linked  
- *"Permission denied"* → means wrong Google account or IAM role  

---

## 🖥 Local Development

- Create venv: python3 -m venv venv  
- Activate: source venv/bin/activate (Mac/Linux) or venv\Scripts\activate (Windows)  
- Install deps: pip install -r requirements.txt  
- Run app: uvicorn main:app --reload  
- Test: http://127.0.0.1:8000/docs  

---

## 📤 Build & Push Image

From project folder:  
gcloud builds submit --tag gcr.io/PROJECT_ID/crud-notes  

This will:  
- Create a tarball of your source  
- Upload to Cloud Storage  
- Run Docker build steps (FROM python, pip install, copy code, CMD)  
- Push final image to gcr.io registry  

---

## 🚀 Deploy to Cloud Run

gcloud run deploy crud-notes --image gcr.io/PROJECT_ID/crud-notes --platform managed --region asia-south1 --allow-unauthenticated  

Outputs a URL like:  
https://crud-notes-xyz.a.run.app  

---

## 🔍 Test API

- Health check: curl https://SERVICE_URL/  
- Docs: open https://SERVICE_URL/docs  

CRUD examples:  
- Create: POST /notes/1 with body {"title":"Note","content":"Hello"}  
- Read: GET /notes/1  
- Update: PUT /notes/1 with new JSON  
- Delete: DELETE /notes/1  

---

## 🗑 Cleanup (Destroy)

1. Delete Cloud Run service:  
   gcloud run services delete crud-notes --region asia-south1 --platform managed  

2. Delete container image:  
   gcloud container images delete gcr.io/PROJECT_ID/crud-notes --force-delete-tags --quiet  

3. Verify empty:  
   gcloud container images list-tags gcr.io/PROJECT_ID/crud-notes  

---

## 🐞 Common Issues Faced

- **Wrong account active** → switch with gcloud config set account  
- **Permission denied** → ensure correct IAM role (Owner/Editor)  
- **Billing not enabled** → must link billing account to project (even for free tier)  
- **Service enable failed** → enable cloudbilling.googleapis.com first, then retry  
- **Image delete error** → forgot to specify digest or tag; use --force-delete-tags  

---

## ✅ Summary

- Check project & account → Link billing → Enable APIs  
- Local test with uvicorn → Build with Cloud Build → Deploy to Cloud Run  
- Test via public URL & /docs  
- Destroy by deleting service + image  
- Always verify billingEnabled and IAM roles if errors occur  