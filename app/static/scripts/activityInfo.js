showPreview = function (element) {
  const preview = document.getElementById("preview-photo");
  preview.src = element.src;
  document.getElementById("preview-dialog").showModal();
}

closePreview = function () {
  document.getElementById("preview-dialog").close();
}
  