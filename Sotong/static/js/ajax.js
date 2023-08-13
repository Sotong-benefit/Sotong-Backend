$('.star').click(function () {
    const postId = $(this).attr('id');
    console.log(postId);
    $.ajax({
        url: "{% url 'community:post-like' %}",  // 해당 시즌 게시물을 가져오는 URL
        method: 'GET',
        dataType: 'html',
        data: { 'post_id': postId },
        success: function (response) {
            $('.my-post').html(response);
        },
        error: function (xhr, status, error) {
            console.error(error);
        }
    });

});