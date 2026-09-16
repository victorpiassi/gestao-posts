# Posts API Specification

## 1. Publish a Post
Creates and schedules or immediately publishes a new post.

* **Endpoint:** `POST /posts`
* **Status Code:** `201 Created`

### Request Body (Pydantic Schema: `PostCreate`)
