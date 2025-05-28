showPreview = function (element) {
  const preview = document.getElementById("preview-photo");
  preview.src = element.src;
  document.getElementById("preview-dialog").showModal();
}

closePreview = function () {
  document.getElementById("preview-dialog").close();
}

loadComments = function (activityId, page) {
  const commentsContainer = document.getElementById("comments-container");
  const url = `/actividad/${activityId}/comentarios/${page}`;
  fetch(url)
    .then(response => response.json())
    .then(comments => {
      console.log(comments);
      if (comments.length == 0) {
        const commentNotice = document.createElement("p");
        commentNotice.className = "notice";
        commentNotice.textContent ="No hay comentarios.";
        commentsContainer.appendChild(commentNotice);
        return;
      }
      for (const index in comments) {
        if (comments.hasOwnProperty(index)) {
          var comment = comments[index];
          const commentElement = document.createElement("article");

          const commentName = document.createElement("h4");
          commentName.textContent = index + ". " + comment["name"];
          commentElement.appendChild(commentName);

          const commentText = document.createElement("p");
          commentText.textContent = comment["text"];
          commentElement.appendChild(commentText);

          const commentDate = document.createElement("p");
          commentDate.textContent = new Date(comment["date"]).toLocaleString();
          commentElement.appendChild(commentDate);

          commentsContainer.appendChild(commentElement);
        }
      }
    })
    .catch(error => {
      console.error("Error loading comments:", error);
    });
}

submitComment = (comment) => {
  const url = `/actividad/${activityId}/comentarios/agregar`;
  const response = fetch(url, {
    "method": "POST",
    "body": commentForm
  })
  response.then(response => response.json())
    .then(data => {
    if (data["success"]) {
      loadComments(data, 0);
    }
    else {
      const commentsContainer = document.getElementById("error-container");
      alert("Error al enviar el comentario: " + data["error"]);
    }

  })
  .catch(error => {
    console.error("Error submitting comment:", error);
  });
}

validateAndSubmitComment = () => {
  const name_input = document.getElementById("comment-name").value;
  const text_input = document.getElementById("comment-text").value;
  if (validateComment(name_input, text_input)) {
    const commentForm = new FormData();
    commentForm.append("name", name_input);
    commentForm.append("text", text_input);
    submitComment(commentForm);
  }
}

window.onload = () => {
  loadComments(activityId, 0);
}