// Handle profile image upload
document.getElementById("profileUpload").addEventListener("change", function(event) {
  const file = event.target.files[0];
  if (file) {
    const img = document.getElementById("profileImg");
    img.src = URL.createObjectURL(file);
  }
});

// Show input field for editing
function editField(field) {
  document.getElementById(field + "Text").classList.add("hidden");
  document.getElementById(field + "Input").classList.remove("hidden");
  document.getElementById(field + "Input").focus();
}

// Save input field back to text
function saveField(field) {
  const input = document.getElementById(field + "Input");
  const text = document.getElementById(field + "Text");
  text.textContent = input.value;
  input.classList.add("hidden");
  text.classList.remove("hidden");
}