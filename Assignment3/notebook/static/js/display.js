function displayAndHide() {
    const commentForm = document.getElementById('comment_form');
    if (commentForm.style.display === 'none') {
        commentForm.style.display = 'block';
    } else {
        commentForm.style.display = 'none';
    }
}