## 🧠 Agentic Prompt Optimization App — Backend Blueprint

### 1. **Overall Architecture**

* **Frontend** → Calls FastAPI endpoints (`/start_optimization`, `/submit_answer`, `/generate_final_prompt`, `/submit_feedback`) with Supabase Auth JWT.
* **FastAPI** → Orchestration layer (“the brain”):

  * Handles API requests, session control, and the agentic loop.
  * Routes LLM calls via an **LLM Router**:

    * **Fast model** for clarifying Q\&A.
    * **Strong model** for final synthesis.
  * Persists state to Supabase (Postgres) via `supabase-py` with Row-Level Security (RLS).
* **Supabase** → Backend services:

  * **Postgres DB**: `opt_sessions`, `opt_messages`, `opt_feedback`.
  * **Auth**: per-user access via RLS.
  * **Optional**: Realtime for live updates.

---

### 2. **FastAPI API Endpoints**

| Endpoint                      | Purpose                                  | Key Logic                                                        |
| ----------------------------- | ---------------------------------------- | ---------------------------------------------------------------- |
| `POST /start_optimization`    | Create session with prompt + selections. | Store session → LLM (fast model) generates clarifying Qs → save. |
| `POST /submit_answer`         | User answers clarifying questions.       | Save answers → LLM updates working memory + next questions.      |
| `POST /generate_final_prompt` | Produce final optimized prompt.          | Strong model + working memory → store final prompt.              |
| `POST /submit_feedback`       | Record user feedback.                    | Store rating + comments.                                         |

---

### 3. **Supabase DB Schema**

**Tables**

* `opt_sessions`
  `id`, `user_id`, `status` (`pending`→`clarifying`→`ready`→`finalized`),
  `initial_prompt`, `selections (jsonb)`, `working_memory (jsonb)`, `final_prompt`.
* `opt_messages`
  `id`, `session_id`, `user_id`, `role` (`system`|`agent`|`user`),
  `kind` (`question`|`answer`|`note`), `content (jsonb)`, `model_name`.
* `opt_feedback`
  `id`, `session_id`, `user_id`, `rating`, `comments`.

**Indexes**

* `(session_id, created_at)` on `opt_messages`
* `(user_id, created_at)` on `opt_sessions`

**RLS**

* Enabled on all tables.
* CRUD allowed only where `auth.uid() = user_id`.

---

### 4. **LLM Routing & Session Flow**

1. **Clarification Phase**
   Fast model (e.g., `gpt-5-mini`) → generate clarifying Qs → save as `agent|question`.
2. **Iteration Phase**
   User answers saved as `user|answer`.
   Fast model updates `working_memory`; decides if more Qs needed.
3. **Finalization Phase**
   Strong model (e.g., `claude-3-7-sonnet`) → synthesize final prompt from memory + selections → save as `final_prompt`.

---

### 5. **Key Implementation Notes**

* **Auth Flow**
  Client → Supabase JWT → FastAPI → `supabase-py` (JWT forwarded) → RLS enforces ownership.
* **Working Memory Structure**
  `{facts: [], constraints: [], gaps: [], rationale: ""}`
* **Observability**
  Log `session_id`, `model_name`, token counts, latency.
* **Safety**
  Max 3 clarifying loops, token/length limits, content validation.

---

**✅ End Result:**
A lightweight FastAPI service orchestrating Supabase and LLMs with clear separation of concerns, secure per-user data, and a transparent agent loop from initial prompt → clarification → synthesis → feedback.

