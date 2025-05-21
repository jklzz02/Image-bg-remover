document.addEventListener("DOMContentLoaded", () => {
  const fileInput = document.getElementById("image_file");
  const fileNameDisplay = document.getElementById("file-name-display");
  const dropZone = document.getElementById("drop-container");

  dropZone.addEventListener("dragover", (event) => {
    event.preventDefault();
  });

  dropZone.addEventListener("drop", (event) => {
    event.preventDefault();

    const files = event.dataTransfer.files;

    if (files.length === 1) {
      const file = files[0];

      const dataTransfer = new DataTransfer();
      dataTransfer.items.add(file);
      fileInput.files = dataTransfer.files;

      fileNameDisplay.textContent = file.name;
    } else {
      fileNameDisplay.textContent = "Please drop only one file.";
    }
  });

  fileInput.addEventListener("change", () => {
    if (fileInput.files.length > 0) {
      fileNameDisplay.textContent = fileInput.files[0].name;
    }
  });
});
