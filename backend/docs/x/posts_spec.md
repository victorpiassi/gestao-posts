# X (Twitter) API v2 - Posts Integration Specification

This document specifies the integration between our FastAPI backend and the official X (Twitter) API v2 for publishing posts, deleting posts, and retrieving engagement metrics.

---

## 1. Authentication & Base URL

- **Base URL:** `https://api.x.com/2`
- **Authentication:** OAuth 2.0 (Authorization Code Flow with PKCE) or OAuth 1.0a User Context.
- **Required Headers:**
  ```http
  Authorization: Bearer <ACCESS_TOKEN>
  Content-Type: application/json
  ```

---

## 2. Endpoints Mapping

### 2.1. Publish Post

#### Backend Endpoint
`POST /api/v1/posts/publish`

#### X API Destination Endpoint
`POST https://api.x.com/2/tweets`

#### Pydantic Schemas (FastAPI)

