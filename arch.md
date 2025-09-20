flowchart TD

  subgraph User["👤 User (Business / Tax Analyst)"]
    A1["React Frontend (Vercel)"]
  end

  subgraph Backend["⚙️ Backend (Google Cloud Functions)"]
    B1["FastAPI + LangChain API"]
  end

  subgraph Data["🗄️ Data & Storage"]
    C1["Supabase Postgres (Relational DB)\n• Users\n• Workflows\n• Chat history\n• Metadata"]
    C2["Supabase pgvector (Vector DB)\n• Embeddings\n• Rules\n• Chunked Docs"]
    C3["Google Cloud Storage (Files/Docs)"]
  end

  subgraph LLMs["🤖 LLM / Inference Layer"]
    D1["Hugging Face Free Endpoint"]
    D2["OpenAI API (optional, paid)"]
  end

  %% Connections with labels
  A1 -->|REST/GraphQL API Calls| B1
  B1 -->|Store/Retrieve User Data, Metadata| C1
  B1 -->|Generate & Query Embeddings| C2
  B1 -->|Upload / Retrieve Files| C3
  B1 -->|Send Prompts + Context| D1
  B1 -->|Send Prompts (Optional fallback)| D2
  C2 -->|Return Relevant Chunks| B1
  C3 -->|Return File Links/Content| B1
  C1 -->|Return Relational Data| B1