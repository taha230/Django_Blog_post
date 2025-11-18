import pytest

from posts.models import Post


@pytest.mark.django_db
def test_post_string_representation():
    post = Post.objects.create(title="Hello World")
    assert str(post) == f"{post.pk}- {post.title}"


@pytest.mark.django_db
def test_live_manager_filters_enabled_posts():
    Post.objects.create(title="Draft", is_enable=False)
    live_post = Post.objects.create(title="Live", is_enable=True)

    queryset = Post.live.all()

    assert list(queryset) == [live_post]
