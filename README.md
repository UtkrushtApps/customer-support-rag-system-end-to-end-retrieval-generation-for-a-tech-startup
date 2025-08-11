# Customer Support RAG System: End-to-End Document Retrieval and Generation

## Task Overview
You are implementing a complete retrieval-augmented generation (RAG) system for customer support at a tech startup. Your system should let end users query a support corpus and receive relevant, accurate responses with supporting citations. The setup gives you a running, empty Chroma vector database and a Python project scaffold. You must build all logic for document ingestion, chunking, embedding, database storage, semantic retrieval, context assembly, and response generation.

## Guidance
- Source or create sample customer support content: FAQs, troubleshooting guides, product manuals, etc., and add them to the `data/documents/` directory.
- Design a processing pipeline to clean, chunk, and prepare your documents; generate and attach relevant metadata for each chunk.
- Select and configure an embedding model (local or API-based) suitable for your corpus and store vector representations in Chroma with all required metadata.
- Implement efficient retrieval based on vector search (e.g., cosine or dot-product) and top-k strategies; consider token budgeting and context limits.
- Build a response pipeline that assembles retrieved context and generates helpful, referenced support answers for incoming queries.
- Measure and log retrieval performance using recall@k and precision@k; include 1–2 evaluation examples for spot checks.
- You may use any libraries, frameworks, or language models and are free to design all chunking, metadata, retrieval, and context strategies as you see fit.

## Database Access Information
- Vector DB is available at `http://<DROPLET_IP>:8000` on your host.
- No schema, collections, or data are pre-populated—initialize all collections, dimension/metric types, and ingest logic as required.
- Use provided Python utilities to connect, create, and query collections.
- Confirm via vector DB API/UI that your chunks, metadata, and embeddings are stored and retrievable.

## Objectives
- Ingest and preprocess a realistic support corpus, chunk and embed the content, and persist it in Chroma with useful metadata.
- Implement fast and accurate top-k retrieval and context assembly to enable effective support responses for a variety of typical customer queries.
- Expose an interface (CLI or script) for submitting queries and receiving answers grounded in your support content.
- Evaluate retrieval accuracy and coverage for several query types using precision@k and recall@k with outputs logged or exported as CSV.

## How To Verify
- Confirm via Chroma client or API that your vectors, metadata, and references are correctly ingested.
- Submit sample support queries and check that the system returns cited context from the most relevant document segments.
- Ensure the answer generator synthesizes support responses using content from your sources, with appropriate context windows, citations, or references.
- Run provided test queries and compare retrieval accuracy (precision@k/recall@k) against expected relevant chunks or document hits.
