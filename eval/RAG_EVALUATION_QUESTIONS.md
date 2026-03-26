# RAG Engine Evaluation Questions: Contract Families

This document contains 10 diverse, complex questions designed to evaluate the performance of a Retrieval-Augmented Generation (RAG) agent backed by a vector database.

Because your dataset consists of "Contract Families" (a Master Agreement plus multiple Amendments), simple keyword search will fail. A high-performing RAG agent must demonstrate temporal reasoning, cross-document synthesis, and the ability to detect when a newer document overrides an older one.

Here are 10 intelligent questions to test your GCP RAG engine, along with the specific capability each question evaluates:

### 1. The Temporal Evolution (Value Tracking)
**Question:** *"Trace the evolution of the maximum credit limit (or total compensation/fees) from the original Master Agreement through all of its subsequent amendments. What was the original amount, and what is the final finalized amount as of the latest amendment?"*
* **Why it tests the RAG:** The vector DB must retrieve chunks from multiple documents, and the LLM must correctly order them chronologically to calculate or identify the final state, ignoring outdated numbers from the original agreement.

### 2. Clause Override Detection (Conflict Resolution)
**Question:** *"Identify the specific amendment that modified the 'Termination' or 'Notice' clause found in the original agreement. How does the required notice period differ between the original agreement and the currently amended version?"*
* **Why it tests the RAG:** Tests the agent's ability to recognize semantic relationships between a specific clause in the Master Agreement and a targeted override in an Amendment, accurately reporting the delta rather than hallucinating a blend of both.

### 3. Entity Addition/Removal
**Question:** *"Across the entire contract family for [Insert Company Name, e.g., Walt Disney or AbbVie], list all counterparties, guarantors, or subsidiaries that were explicitly added or removed over time. Which specific amendment made the most changes to the parties involved?"*
* **Why it tests the RAG:** Requires exhaustive retrieval across the entire family (high recall) and precise entity extraction without mixing up who was added versus who was removed.

### 4. Synthesizing Net-New Obligations
**Question:** *"Based on the original agreement and Amendment No. 2, what are the net-new compliance, reporting, or delivery obligations imposed on the parties that were entirely absent from the original text?"*
* **Why it tests the RAG:** The agent must compare the semantic meaning of the obligations in two different documents and perform a "diff" operation to isolate what is genuinely new.

### 5. Date Extensions and Milestones
**Question:** *"What was the original expiration or maturity date of this contract, how many times was it extended through amendments, and what is the final effective expiration date?"*
* **Why it tests the RAG:** Often, amendments only say "Section X is amended by replacing '2023' with '2025'". The RAG system needs to retrieve the context of Section X from the Master and map the date change accurately.

### 6. Semantic Search on Abstract Concepts (Risk/Liability)
**Question:** *"Which amendments in this dataset introduce stricter data privacy, confidentiality, or security requirements compared to their respective master agreements?"*
* **Why it tests the RAG:** Tests the vector database's embedding model. "Stricter" is an abstract concept; the database must retrieve clauses related to data/security and the LLM must evaluate the severity of the language.

### 7. Dependency and Conditionality
**Question:** *"According to the fully amended contract, what are the exact conditions under which a 'Change of Control' triggers an automatic termination or default? Did any amendment alter these conditions?"*
* **Why it tests the RAG:** "Change of Control" clauses are notoriously complex. The agent must stitch together definitions from the Master Agreement with potential re-definitions in later amendments to provide a legally accurate answer.

### 8. The "Needle in a Haystack" (Schedule/Exhibit Changes)
**Question:** *"Generate a chronological summary of all structural changes made to the 'Pricing', 'Fees', or 'Interest Rate' schedules from the inception of the contract through its final amendment."*
* **Why it tests the RAG:** Schedules and Exhibits are often attached at the very end of long documents. This tests if your chunking strategy properly preserved the context of tabular or list-based financial data.

### 9. Tracing Definitions
**Question:** *"How was the definition of 'EBITDA' (or 'Material Adverse Effect') modified by the amendments? Quote the original definition and the final amended definition."*
* **Why it tests the RAG:** Amendments frequently redefine capitalized terms. The RAG agent must successfully locate the "Definitions" section of the Master Agreement and track any targeted re-definitions in subsequent files.

### 10. Cross-Family Comparison (Meta-Analysis)
**Question:** *"Compare the 'Governing Law' and 'Dispute Resolution' clauses across all the different contract families in the database. Did any company change their preferred jurisdiction or arbitration rules via an amendment?"*
* **Why it tests the RAG:** This is a massive multi-hop query. It tests the system's ability to retrieve specific thematic chunks across entirely different directories/companies and aggregate them into a comparative analysis.
