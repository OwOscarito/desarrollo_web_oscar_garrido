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
      for (const index in comments) {
        if (comments.hasOwnProperty(index)) {
          var comment = comments[index];
          
          
        }
      }
    })
    .catch(error => {
      console.error('Error loading comments:', error);
    });
}

validateAndSubmit = function () {
  
}

window.onload = () => {
  const activityId = document.getElementById("activity-id").value;
  const page = document.getElementById("page").value;
  loadComments(activityId, page);
}