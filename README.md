## Blog Django – DRF Views Showcase

This project is a simple blog API built with **Django 4.2** and **Django REST Framework (DRF)**.  
It is mainly intended as a learning playground to compare the **different types of DRF views** and how they implement the same CRUD behaviour for a `Post` model.

### Main DRF View Types Demonstrated

- **Function-Based API Views (`@api_view`)**
  - Example: `index` in `posts/views.py`.
  - Uses the `@api_view` decorator to handle HTTP verbs explicitly (e.g. `GET`, `POST`).
  - Accesses query parameters via `request.query_params` and returns serialized data with `Response`.

- **Low-level Class-Based API Views (`APIView`)**
  - Examples: `PostListRestView`, `PostDetailRestView`.
  - Inherit from `rest_framework.views.APIView`.
  - You manually:
    - Query the database (`Post.objects.all()`, `get_object` helper).
    - Instantiate serializers with `data` / `instance`.
    - Call `.is_valid()`, `.save()`, and build `Response` objects.
    - Handle errors and return proper status codes (e.g. `400`, `404`, `204`).

- **Generic Class-Based Views (Full Generic Views)**
  - Examples: `PostListRestViewGenericsFull` (`ListCreateAPIView`), `PostDetailRestViewGenericsFull` (`RetrieveUpdateDestroyAPIView`).
  - Inherit from DRF’s highly-opinionated generic views that implement full behaviour for you.
  - You typically only set:
    - `queryset`
    - `serializer_class`
  - DRF automatically wires up:
    - `GET` list / retrieve
    - `POST` create
    - `PUT` / `PATCH` update
    - `DELETE` destroy

- **GenericAPIView + Mixins**
  - Examples: `PostListRestViewGenerics`, `PostDetailRestViewGenerics`.
  - Combine `generics.GenericAPIView` with mixins such as:
    - `ListModelMixin`, `CreateModelMixin`
    - `RetrieveModelMixin`, `UpdateModelMixin`, `DestroyModelMixin`
  - You explicitly map HTTP verbs to mixin methods:
    - `get()` → `self.list()` / `self.retrieve()`
    - `post()` → `self.create()`
    - `put()` → `self.update()`
    - `delete()` → `self.destroy()`
  - This pattern is useful when you want control over which operations are exposed while still reusing a lot of DRF logic.

- **ViewSets + Routers**
  - Example: `PostViewSet` combined with `DefaultRouter` in `posts/urls.py`.
  - `PostViewSet` subclasses `viewsets.ModelViewSet` and declares:
    - `queryset = Post.objects.all()`
    - `serializer_class = PostSerializer`
    - `permissions = [permissions.IsAuthenticatedOrReadOnly]`
  - `DefaultRouter` automatically generates RESTful routes:
    - List / create: `GET /posts/`, `POST /posts/`
    - Detail actions: `GET /posts/{id}/`, `PUT /posts/{id}/`, `DELETE /posts/{id}/`
  - This is the most concise way to build a full-featured REST API with DRF.

### Traditional Django Views Demonstrated

Alongside DRF views, the project also includes **classic Django views** for comparison:

- Function-based template views: `post_list`, `post_detail`, `post_create`.
- Class-based generic views:
  - `PostList` (`ListView`)
  - `PostDetail` (`DetailView`)

These are used to render HTML templates (`posts/post_list.html`, `posts/post_detail.html`, etc.) and help you see the difference between traditional Django views and DRF API views.

### URL Configuration Overview

- `weblog/urls.py`
  - Mounts:
    - `admin/` → Django admin.
    - `index/` → DRF function-based API example.
    - `home/` → simple HTML response.
    - `posts/create/` → HTML form-based post creation.
    - `posts/` → includes `posts.urls`.

- `posts/urls.py`
  - Registers a `DefaultRouter`:
    - `router.register(r'', PostViewSet, basename='posts')`
  - Includes router URLs at the root of `posts/`.
  - Commented-out paths show alternative wiring for:
    - `APIView` list/detail views.
    - Generic views and mixin-based views.
    - Manual `ViewSet.as_view({...})` mapping.

### How to Run the Project Locally

- **Clone and create a virtualenv**
  - `git clone <this-repo-url>`
  - `cd Blog_Django`
  - Create and activate a virtual environment (optional but recommended).

- **Install dependencies**
  - `pip install -r requirements.txt`

- **Apply migrations**
  - `python manage.py migrate`

- **Run the development server**
  - `python manage.py runserver`

Then visit:

- `http://127.0.0.1:8000/index/` – DRF `@api_view` example.
- `http://127.0.0.1:8000/posts/` – DRF `ViewSet` + router-powered API.
- `http://127.0.0.1:8000/posts/create/` – classic Django form-based create view.

### Running Tests

This project uses **pytest** and **pytest-django**.

- Run the test suite:
  - `pytest`

Tests currently cover:

- The string representation of `Post`.
- A custom `Post.live` manager for filtering enabled posts.

---

This README is intentionally focused on **learning the different DRF view styles**.  
You can uncomment alternative URL patterns in `posts/urls.py` to switch between implementations and compare their behaviour.

## 👤 Author

**Taha Hamedani**  
📧 [taha.hamedani8@gmail.com](mailto:taha.hamedani8@gmail.com)  


