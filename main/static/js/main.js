document.addEventListener("DOMContentLoaded", () => {
  const fileInput = document.getElementById("image_file");
  const fileNameDisplay = document.getElementById("file-name-display");

  fileInput.addEventListener("change", () => {
    if (fileInput.files.length > 0) {
      fileNameDisplay.textContent = fileInput.files[0].name;
    }
  });
});
