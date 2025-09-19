
🚀 FastAPI CRUD on Google Cloud Run — Full Cheat Sheet (with Fixes + Flow Diagram)

⸻

📂 Flow Diagram

[ Local Dev ]
     |  (test locally)
     |-- uvicorn main:app --reload
     v
[ Cloud Build ]
     |  (build + push image)
     |-- gcloud builds submit --tag gcr.io/PROJECT_ID/crud-notes
     v
[ Container Registry ]
     |  (deploy service)
     |-- gcloud run deploy crud-notes --image gcr.io/PROJECT_ID/crud-notes --platform managed --region asia-south1 --allow-unauthenticated
     v
[ Cloud Run Service ]
     |  (public URL auto-generated)
     v
[ Public URL ]
   → open https://SERVICE_URL/
   → open https://SERVICE_URL/docs

Cleanup flow:
[ Cloud Run Service ]
     |-- gcloud run services delete crud-notes --region asia-south1 --platform managed
     v
 (Service deleted)

[ Container Registry ]
     |-- gcloud container images delete gcr.io/PROJECT_ID/crud-notes --force-delete-tags --quiet
     v
 (Image deleted)




⸻

🔧 Initial Setup
	1.	Check active project → gcloud config list project
	2.	If wrong → gcloud config set project PROJECT_ID
	3.	Check active account → gcloud auth list
	4.	If wrong → gcloud config set account YOUR_EMAIL

⸻

👤 IAM & Billing
	•	Check IAM role → gcloud projects get-iam-policy PROJECT_ID (must be Owner/Editor)
	•	Check billing linked → gcloud beta billing projects describe PROJECT_ID (should say billingEnabled: true)
	•	If billing is false →
	•	Link billing account in Cloud Console
	•	Enable API → gcloud services enable cloudbilling.googleapis.com

⸻

⚙️ Enable Required Services

gcloud services enable run.googleapis.com cloudbuild.googleapis.com artifactregistry.googleapis.com

Common errors:
	•	Billing account not found → link billing first
	•	Permission denied → wrong Google account or IAM role

⸻

🖥 Local Test
	•	Install deps → pip install -r requirements.txt
	•	Run app → uvicorn main:app –reload
	•	Browser → http://127.0.0.1:8000/docs

⸻

📤 Build & Push Image

gcloud builds submit –tag gcr.io/PROJECT_ID/crud-notes

⸻

🚀 Deploy to Cloud Run

gcloud run deploy crud-notes –image gcr.io/PROJECT_ID/crud-notes –platform managed –region asia-south1 –allow-unauthenticated

Result → Public URL like https://crud-notes-xyz.a.run.app

⸻

🔍 Test API
	•	Health check → curl https://SERVICE_URL/
	•	Docs → https://SERVICE_URL/docs
	•	CRUD calls:
	•	POST /notes/1 → create
	•	GET /notes/1 → read
	•	PUT /notes/1 → update
	•	DELETE /notes/1 → delete

⸻

🗑 Cleanup
	1.	Delete service → gcloud run services delete crud-notes –region asia-south1 –platform managed
	2.	Delete image → gcloud container images delete gcr.io/PROJECT_ID/crud-notes –force-delete-tags –quiet
	3.	Verify → gcloud container images list-tags gcr.io/PROJECT_ID/crud-notes

⸻

🐞 Common Issues & Fixes
	•	Wrong account active → fix with gcloud config set account
	•	Permission denied → assign Owner role in IAM
	•	Billing not enabled → must link billing account
	•	Service enable failed → enable cloudbilling.googleapis.com first
	•	Image delete error → add –force-delete-tags

⸻

✅ Quick Lifecycle
	1.	Local dev → uvicorn test
	2.	Build image → gcloud builds submit
	3.	Deploy → gcloud run deploy
	4.	Test → Public URL + /docs
	5.	Destroy → gcloud run services delete + gcloud container images delete

