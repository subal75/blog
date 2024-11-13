# This project is a Blog API built with Django and Django REST Framework (DRF). It allows users to create, edit, and delete blog posts, leave comments (including nested replies), and manage their accounts. The API uses session-based authentication to secure endpoints and token authentication for user login.


Clone the repository:
`git clone https://github.com/subal75/blog.git`

1. Create and activate a virtual environment
`python -m venv venv`

on windows- 
`venv\Scripts\activate`
on ubuntu-
`source venv/bin/activate`

2. Install dependencies:
`pip install -r requirements.txt`

3. `python manage.py migrate`

4. 
- **Authentication:**
  - `POST /api/register/` - Register a new user.
  - `POST /api/login/` - Login to get a token.

- **Blog Posts:**
  - `GET /api/posts/` - List all blog posts.
  - `POST /api/posts/` - Create a new blog post (authenticated users only).
  - `GET /api/posts/{id}/` - Retrieve a specific blog post.
  - `PUT /api/posts/{id}/` - Update a specific blog post (only the author can update).
  - `DELETE /api/posts/{id}/` - Delete a specific blog post (only the author can delete).

- **Comments:**
  - `GET /api/posts/{post_id}/comments/` - List all comments for a specific post.
  - `POST /api/posts/{post_id}/comments/` - Create a new comment (authenticated users only).
  - `DELETE /api/comments/{comment_id}/` - Delete a specific comment (only the author can delete).
