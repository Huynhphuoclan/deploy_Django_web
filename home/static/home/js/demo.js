document.addEventListener('DOMContentLoaded', () => {
  const dropZone = document.getElementById('drop-zone');
  const imageDisplay = document.getElementById('image-display');
  const fileInput = document.createElement('input');
  fileInput.type = 'file';
  fileInput.name = 'image';
  fileInput.style.display = 'none';
  fileInput.accept = 'image/*';

  const reader = new FileReader();

  if (window.FileList && window.File) {
      dropZone.addEventListener('dragover', event => {
          event.stopPropagation();
          event.preventDefault();
          event.dataTransfer.dropEffect = 'copy';
      });

      dropZone.addEventListener('drop', event => {
          imageDisplay.innerHTML = '';
          event.stopPropagation();
          event.preventDefault();
          const files = event.dataTransfer.files;
          if (files.length > 0) {
              fileInput.files = files;

              reader.readAsDataURL(files[0]);

              reader.addEventListener('load', (event) => {
                  imageDisplay.innerHTML = '';
                  const img = document.createElement('img');
                  img.style.height = '400px';
                  img.style.width = '400px';
                  imageDisplay.appendChild(img);
                  img.src = event.target.result;
                  img.alt = files[0].name;
              });
          }
      });
  }

  // Append the hidden file input to the form
  const form = document.querySelector('form[method="post"]');
  form.appendChild(fileInput);
});