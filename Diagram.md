Finance Copilot Architecture

Component Diagram (PlantUML)

@startuml
title Finance Copilot - Component Architecture

rectangle "👤 User (Business Analyst)" as User

node "Frontend (React - Vercel)" as Frontend
node "Backend (FastAPI + LangChain - Cloud Functions)" as Backend

package "Data Layer" {
  database "Supabase (Relational)" as RelDB
  database "Supabase (pgvector)" as VecDB
  folder "Google Cloud Storage" as GCS
}

package "LLM Layer" {
  [Hugging Face API] as HF
  [OpenAI API (Optional)] as OpenAI
}

User --> Frontend : Interact (Chat / Upload)
Frontend --> Backend : HTTPS Requests (API Calls)
Backend --> RelDB : Store/Retrieve\nUser Metadata, Workflows
Backend --> VecDB : Store/Retrieve\nEmbeddings, Chunks
Backend --> GCS : Upload/Fetch\nFiles, Docs
Backend --> HF : Prompt + Context\n(Query LLM)
Backend --> OpenAI : Prompt + Context\n(Optional)
RelDB --> Backend : Relational Data
VecDB --> Backend : Relevant Chunks
GCS --> Backend : File Links / Content
Backend --> Frontend : Responses / Insights
@enduml


⸻

Exporting Diagrams (PlantUML → SVG/PNG)

PlantUML diagrams can be exported directly to SVG or PNG.

1. PlantUML Online
	•	Open PlantUML Online Editor.
	•	Paste your code → Download as SVG or PNG.

2. VS Code + PlantUML Extension
	•	Install PlantUML extension.
	•	Open .puml file → Right-click → Export Current Diagram → Choose SVG.

3. CLI (Local Install)
	•	Install:
	•	Mac: brew install plantuml
	•	Ubuntu: sudo apt install plantuml
	•	Export SVG:
	•	plantuml -tsvg diagram.puml
	•	Export PNG:
	•	plantuml -tpng diagram.puml

✅ SVG Advantage: Scales without pixelation, perfect for docs, slides, and web apps.

⸻

When to Use Different Diagramming Tools

🟢 PlantUML
	•	Best for enterprise diagrams (component, class, deployment, C4 model).
	•	Supports swimlanes in activity diagrams (good for process flows).
	•	Strong theming and export options (SVG/PNG/PDF).

🔵 D2 (Terrastruct)
	•	Modern, clean syntax DSL for diagrams.
	•	Best when you want auto-layout and fast prototyping.
	•	Swimlanes can be simulated using group or container blocks.
	•	Works well for docs and modern developer tooling.

🟣 Python Diagrams (Mingrammer)
	•	Write diagrams in Python code.
	•	Perfect for infrastructure architecture (AWS, GCP, Azure icons included).
	•	Use when you need cloud infra visualization with official icons.
	•	Less suited for swimlanes, but can group elements with clusters.

⸻

Swimlanes
	•	In PlantUML: use activity diagrams with |LaneName| to separate flows.
	•	In D2: use group blocks to simulate swimlanes.
	•	Useful when showing end-to-end workflows across Frontend, Backend, Data, and LLM layers.

⸻

📌 Rule of Thumb
	•	PlantUML → Formal enterprise docs, architecture reviews.
	•	D2 → Quick, modern, and clean diagrams for developer-centric docs.
	•	Mingrammer Diagrams → Infrastructure (cloud resources, services, network maps).